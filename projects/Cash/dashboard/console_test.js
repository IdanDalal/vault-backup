// Unit tests for the Core block of Cash-Console.html. Run: node console_test.js
const fs = require('fs'), path = require('path'), assert = require('assert');
const html = fs.readFileSync(path.join(__dirname, 'Cash-Console.html'), 'utf8');
const core = html.match(/<script id="core">([\s\S]*?)<\/script>/)[1];
const EMB = JSON.parse(html.match(/<script id="embedded" type="application\/json">([\s\S]*?)<\/script>/)[1].replace(/<\\\//g, '</'));
const mod = { exports: {} };
new Function('module', core)(mod);
const Core = mod.exports;
let n = 0; const ok = (name, f) => { f(); n++; console.log('ok', name); };
const close = (a, b, eps = 0.011) => assert.ok(Math.abs(a - b) < eps, `${a} vs ${b}`);

const settings = { ...EMB.settings };
const prices = Object.fromEntries(Object.entries(EMB.tickers).map(([k, v]) => [k, v.ref]));
const G = EMB.plan.find(s => s.step === 'sell').ref; // GOOGL reference at plan time (sale price once executed)
const SEED_PRE = EMB.seed.filter(t => t.date < EMB.plan_date); // the ledger before the plan date: the original 55 GOOGL
const GOOGL_PRICE_NOW = EMB.tickers.GOOGL.ref;

ok('v3 retPct: exact, carried, short, one-year edge', () => {
  const h = [['2026-01-01', 100], ['2026-01-02', 110], ['2026-01-05', 120], ['2026-02-02', 150]];
  close(Core.retPct(h, 28), 25);           // cut 01-05 → base 120
  close(Core.retPct(h, 30), 36.3636);      // cut 01-03 → base 01-02 = 110
  assert.equal(Core.retPct(h, 365), null); // series shorter than the window
  const y = [['2025-09-12', 100], ['2026-03-01', 90], ['2026-09-11', 130]];
  close(Core.retPct(y, 365), 30);          // starts 1 day after the cut → first point
  assert.equal(Core.retPct([['2026-01-01', 1]], 1), null);
});
ok('v3 poolSeries: shares × close, carry forward, partial days dropped', () => {
  const H = { A: [['d1', 10], ['d2', 11], ['d4', 12]], B: [['d2', 100], ['d3', 101], ['d4', 102]] };
  const s = Core.poolSeries([{ ticker: 'A', shares: 2 }, { ticker: 'B', shares: 1 }, { ticker: 'C', shares: 5 }], H);
  assert.deepEqual(s, [['d2', 122], ['d3', 123], ['d4', 126]]); // d1 dropped (B has no close yet); d3 carries A=11; C has no history and is ignored
  assert.deepEqual(Core.poolSeries([], H), []);
});
ok('v3 poolIndex: chain-linked, a late listing joins without a jump, equals poolSeries when histories are complete', () => {
  const H = { A: [['d1', 10], ['d2', 11], ['d4', 12]], B: [['d2', 100], ['d3', 101], ['d4', 102]] };
  const ix = Core.poolIndex([{ ticker: 'A', shares: 2 }, { ticker: 'B', shares: 1 }], H);
  assert.deepEqual(ix.map(p => p[0]), ['d1', 'd2', 'd3', 'd4']);
  close(ix[0][1], 100); close(ix[1][1], 110); close(ix[2][1], 110 * 123 / 122, 1e-3); close(ix[3][1], 110 * 123 / 122 * 126 / 123, 1e-3);
  assert.deepEqual(ix[0][2], ['A']); assert.deepEqual(ix[1][2], ['B']); assert.deepEqual(ix[2][2], []);
  const F = { A: [['d1', 10], ['d2', 11], ['d3', 12]], B: [['d1', 100], ['d2', 101], ['d3', 102]] }, hs = [{ ticker: 'A', shares: 2 }, { ticker: 'B', shares: 1 }];
  const s = Core.poolSeries(hs, F), i2 = Core.poolIndex(hs, F);
  for (let i = 0; i < s.length; i++) close(i2[i][1] / 100 * s[0][1], s[i][1], 1e-3);
});
ok('v3 ladderImplied: median by interpolation, monotonic flag', () => {
  const L = [{ g: '$100', yes: 0.9 }, { g: '$110', yes: 0.7 }, { g: '$120', yes: 0.3 }, { g: '$130', yes: 0.1 }];
  const r = Core.ladderImplied(L); assert.equal(r.monotonic, true); close(r.median, 115);
  const bad = Core.ladderImplied([{ g: '$100', yes: 0.9 }, { g: '$110', yes: 0.95 }, { g: '$120', yes: 0.3 }]); assert.equal(bad.monotonic, false);
  assert.equal(Core.ladderImplied([{ g: '$100', yes: 0.9 }]).median, null);
  assert.equal(Core.ladderImplied([{ g: '$100', yes: 0.9 }, { g: '$110', yes: 0.8 }, { g: '$120', yes: 0.7 }]).median, null); // never crosses 50%
});
if (EMB.market) ok('v3 embedded market data: every held ticker has a year of closes, fx history, odds groups', () => {
  const M = EMB.market;
  for (const T of Object.keys(EMB.tickers)) assert.ok(M.history[T] && M.history[T].length > 20, T + ' history'); // SKHY and SPCX listed mid-2026: 45 and 63 closes on 09-14
  assert.ok(Object.keys(EMB.tickers).filter(T => M.history[T].length > 200).length >= 15, 'most names carry a full year');
  assert.ok(M.fx.history.length > 200 && M.fx.now > 2 && M.fx.now < 5);
  assert.ok(M.polymarket.groups.length >= 1 && M.polymarket.groups.some(g => g.events.length));
  const A = Core.analyze(EMB.seed, EMB, settings, prices);
  const s = Core.poolSeries(A.holdings, M.history); assert.ok(s.length > 20 && s[s.length - 1][1] > 1000);
  const ix = Core.poolIndex(A.holdings, M.history); assert.ok(ix.length > 200, 'chain-linked index spans the year'); assert.ok(ix.every((p, i) => !i || Math.abs(p[1] / ix[i - 1][1] - 1) < 0.15), 'no daily jump above 15%');
});

ok('embedded data shape', () => {
  assert.equal(Object.keys(EMB.tickers).length, 19);
  assert.equal(Object.values(EMB.tickers).reduce((a, t) => a + t.target, 0), 100);
  assert.ok(EMB.plan.length >= 3 && EMB.plan[0].step === 'fx' && EMB.plan[1].step === 'sell');
  assert.equal(SEED_PRE.length, 1);
});

ok('pre-plan seed: 55 GOOGL held, cost 18,417.85, cash zero', () => {
  const A = Core.analyze(SEED_PRE, EMB, settings, prices);
  const g = A.holdings.find(h => h.ticker === 'GOOGL');
  assert.equal(g.shares, 55); close(g.cost, 18417.85); close(A.marketValue, 55 * GOOGL_PRICE_NOW);
  close(A.cashUsd, 0); // usd_start offsets the pre-pool buy
  close(A.poolValue, 55 * GOOGL_PRICE_NOW + settings.nis_start / settings.fx_now, 0.02);
  assert.equal(A.planDone, 0); assert.equal(A.warnings.length, 0);
});

if (EMB.executed) ok('executed ledger: 20 steps done, 19 positions, fees pending overdraw the dollar account', () => {
  const A = Core.analyze(EMB.seed, EMB, settings, prices);
  assert.equal(A.planDone, EMB.plan.length);
  assert.equal(A.holdings.filter(h => h.shares > 0).length, 19);
  const g = A.holdings.find(h => h.ticker === 'GOOGL'); assert.equal(g.shares, 9);
  const fxIn = EMB.seed.filter(t => t.type === 'fx').reduce((a, t) => a + t.usd_in, 0);
  close(A.cashUsd, fxIn + 15088.60 - 27946.87 - 18 * 24, 0.02); // +$66.45 once the ₪1,000 fee cover of 09-11 is in
  close(A.cashNis, 0, 0.02); // every ₪ that entered the pool was converted; the ₪ start balance is the sum of the conversions
  const idiFx = EMB.seed.filter(t => t.type === 'fx' && t.owner === 'idi').reduce((a, t) => a + t.usd_in, 0);
  close(A.ownership.momStake, 13031.69 / (13031.69 + 18049.60 + idiFx) * 100, 0.01); // 41.49% after Idi's ₪1,000 fee cover
  close(A.feesUsd, 45.40 + 18 * 24, 0.01);
  assert.equal(A.warnings.length, 0);
});

const fxRow = { id: 'fx1', date: '2026-09-10', type: 'fx', owner: 'mom', nis_out: 40000, usd_in: 13200, fee_nis: 60, note: '' };
const sellRow = { id: 's1', date: '2026-09-10', type: 'sell', ticker: 'GOOGL', shares: 46, price_usd: 331, fee_usd: 5, usd_in: 0 };

ok('fx: effective rate, cash, stake', () => {
  const A = Core.analyze([...SEED_PRE, fxRow], EMB, settings, prices);
  const f = A.fx[0]; close(f.eff, (40000 + 60) / 13200, 1e-4);
  close(A.cashNis, settings.nis_start - 40060); close(A.cashUsd, 13200);
  close(A.ownership.momUsd, 13200);
  close(A.ownership.momStake, 13200 / (13200 + settings.idi_value_at_pooling) * 100, 0.01);
});

ok('sell: average-cost realized P&L, FIFO lots, plan step done', () => {
  const A = Core.analyze([...SEED_PRE, fxRow, sellRow], EMB, settings, prices);
  const g = A.holdings.find(h => h.ticker === 'GOOGL');
  assert.equal(g.shares, 9);
  const avg = 18417.85 / 55; close(g.realized, 46 * 331 - 5 - 46 * avg); close(g.cost, 9 * avg);
  assert.equal(A.lots.length, 1); assert.equal(A.lots[0].shares, 9);
  const step = A.plan.find(s => s.step === 'sell'); assert.equal(step.status, 'done'); close(step.avgPx, 331); close(step.slip, (331 / G - 1) * 100, 0.01);
  close(A.cashUsd, 13200 + 46 * 331 - 5);
});

ok('buys: partial then complete, drift falls, slippage sign', () => {
  const b1 = { id: 'b1', date: '2026-09-10', type: 'buy', ticker: 'NVDA', shares: 6, price_usd: 224, fee_usd: 3 };
  const b2 = { id: 'b2', date: '2026-09-10', type: 'buy', ticker: 'NVDA', shares: 7, price_usd: 225, fee_usd: 3 };
  const A1 = Core.analyze([...SEED_PRE, fxRow, sellRow, b1], EMB, settings, prices);
  const s1 = A1.plan.find(s => s.ticker === 'NVDA'); assert.equal(s1.status, 'partial'); assert.equal(s1.done, 6);
  const A2 = Core.analyze([...SEED_PRE, fxRow, sellRow, b1, b2], EMB, settings, prices);
  const s2 = A2.plan.find(s => s.ticker === 'NVDA'); assert.equal(s2.status, 'done'); assert.equal(s2.done, 13);
  close(s2.avgPx, (6 * 224 + 7 * 225) / 13); assert.ok(A2.driftSum < A1.driftSum);
  const h = A2.holdings.find(h => h.ticker === 'NVDA'); close(h.cost, 6 * 224 + 7 * 225 + 6); assert.equal(h.lots.length, 2);
  assert.equal(A2.planDone, 3);
});

if (!EMB.executed) ok('full plan executed at reference prices: drift equals the sheet, cash left equals the sheet', () => {
  const rows = [...SEED_PRE, { ...fxRow, usd_in: EMB.pool.mom, fee_nis: 0 }, { ...sellRow, price_usd: G, fee_usd: 0 }];
  for (const s of EMB.plan) if (s.step === 'buy') rows.push({ id: 'p' + s.ticker, date: '2026-09-10', type: 'buy', ticker: s.ticker, shares: s.shares, price_usd: s.ref, fee_usd: 0 });
  const A = Core.analyze(rows, EMB, settings, prices);
  assert.equal(A.planDone, EMB.plan.length);
  close(A.driftSum, EMB.pool.drift - 0.5 * (EMB.pool.total - EMB.pool.spent) / EMB.pool.total * 100, 0.05); // sheet objective adds 0.5 x idle cash %
  close(A.marketValue, EMB.pool.spent, 0.02);
  close(A.cashUsd, EMB.pool.total - EMB.pool.spent, 0.02);
  for (const h of A.holdings) assert.ok(h.shares > 0, h.ticker + ' should be held');
});

ok('fx rate for lots: explicit, then latest conversion, then settings', () => {
  const rows = [{ id: 'a', date: '2026-01-29', type: 'buy', ticker: 'GOOGL', shares: 1, price_usd: 100, fx_rate: 3.0968 },
    fxRow, { id: 'b', date: '2026-09-11', type: 'buy', ticker: 'NVDA', shares: 1, price_usd: 100 },
    { id: 'c', date: '2026-01-01', type: 'buy', ticker: 'AMD', shares: 1, price_usd: 100 }];
  const A = Core.analyze(rows, EMB, { ...settings, fx_now: 3.5 }, prices);
  const by = Object.fromEntries(A.lots.map(l => [l.ticker, l]));
  close(by.GOOGL.fxAtBuy, 3.0968, 1e-4); close(by.NVDA.fxAtBuy, (40060) / 13200, 1e-4); close(by.AMD.fxAtBuy, 3.5, 1e-4);
  close(by.AMD.costNis, 350); close(by.AMD.valueNis, prices.AMD * 3.5, 0.02);
});

ok('warnings: overselling and unknown type', () => {
  const A = Core.analyze([{ date: '2026-09-10', type: 'sell', ticker: 'VRT', shares: 1, price_usd: 10 }, { date: '2026-09-10', type: 'zzz' }], EMB, settings, prices);
  assert.equal(A.warnings.length, 2);
});

ok('dividend and fee types', () => {
  const A = Core.analyze([{ date: '2026-09-10', type: 'dividend', ticker: 'MSFT', usd_in: 10, fee_usd: 2.5 }, { date: '2026-09-10', type: 'fee', fee_usd: 1, fee_nis: 4 }], EMB, { ...settings, nis_start: 100, usd_start: 100 }, prices);
  close(A.cashUsd, 109); close(A.cashNis, 96); close(A.dividends, 10); close(A.feesUsd, 3.5); close(A.feesNis, 4);
});

ok('vault markdown export round-trips the template fields', () => {
  const md = Core.toVaultMarkdown([Core.normalize(fxRow), Core.normalize(sellRow)]);
  assert.ok(md.includes('=== transactions/2026-09-10 fx 13200usd.md ==='));
  assert.ok(md.includes('=== transactions/2026-09-10 sell GOOGL.md ==='));
  for (const k of ['date:', 'type:', 'ticker:', 'nis_out:', 'usd_in:', 'fee_nis:', 'fee_usd:', 'shares:', 'price_usd:', 'note:', 'author: jep', '- cash-tx']) assert.ok(md.includes(k), k);
  assert.ok(!md.includes('author: Idi'), 'never author: Idi');
  assert.ok(!md.includes('—'), 'no em dashes in exported files');
});

ok('vault markdown export: seed rows skipped, same-day partial fills get distinct filenames', () => {
  const b = { date: '2026-09-10', type: 'buy', ticker: 'NVDA', shares: 6, price_usd: 224 };
  const md = Core.toVaultMarkdown([Core.normalize(SEED_PRE[0]), Core.normalize({ ...b, id: 'a' }), Core.normalize({ ...b, id: 'b', shares: 7 })]);
  assert.ok(!md.includes('2026-01-29 buy GOOGL'), 'seed row must not be re-exported');
  assert.ok(md.includes('=== transactions/2026-09-10 buy NVDA.md ===') && md.includes('=== transactions/2026-09-10 buy NVDA (2).md ==='));
});

ok('normalize: numeric id becomes a string, local date is YYYY-MM-DD', () => {
  assert.strictEqual(Core.normalize({ id: 42 }).id, '42');
  assert.match(Core.localDate(), /^\d{4}-\d{2}-\d{2}$/);
});

ok('csv escapes commas and quotes', () => {
  const csv = Core.toCsv([Core.normalize({ ...sellRow, note: 'a, "b"' })]);
  assert.ok(csv.split('\n')[1].endsWith('"a, ""b""",' + Core.normalize(sellRow).created));
});

ok('price paste parser', () => {
  const p = Core.parsePrices('NVDA 223.67\nMSFT: 491.65\n  ASML: 1 sh x $1,729.52 = $1,729.52  actual 5.5% vs target 4%\nfoo bar');
  assert.equal(p.NVDA, 223.67); assert.equal(p.MSFT, 491.65); assert.equal(p.ASML, 1729.52); assert.equal(Object.keys(p).length, 3);
});

ok('normalize: uppercase ticker, numeric coercion, id kept', () => {
  const t = Core.normalize({ id: 'x', ticker: 'nvda', shares: '3', price_usd: '', fee_usd: 'abc' });
  assert.equal(t.id, 'x'); assert.equal(t.ticker, 'NVDA'); assert.equal(t.shares, 3); assert.equal(t.price_usd, 0); assert.equal(t.fee_usd, 0);
});

console.log(`\n${n} tests passed`);
