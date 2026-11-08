"""Class ticket weights that equalise spec exposure per slot (IPF over P, S, T margins), integer 1..CAP; simulate
Choose My Class (100 offers, without replacement over tickets, a class shown once) to compare coverage."""
import json, random, collections, sim
deck = [tuple(x[:3]) for x in sim.deck(sim.load()) if not x[3]]
cnt = collections.Counter()
for p, s, t in deck: cnt['P|' + p] += 1; cnt['S|' + s] += 1; cnt['T|' + t] += 1
print('1-3 card specs now:') if False else None
for k, v in sorted(cnt.items(), key=lambda kv: kv[1]):
    if False: print('  %-22s %d  %s' % (k, v, ['_'.join(c) for c in deck if k[2:] in c]))
CAP = 50
M = max(v for k, v in cnt.items() if k.startswith('T|'))
MX = {sl: max(v for k, v in cnt.items() if k.startswith(sl + '|')) for sl in 'PST'}
tick = {c: max(1, min(CAP, max(round(MX['T'] / cnt['T|' + c[2]]), round(MX['S'] / cnt['S|' + c[1]]), round(MX['P'] / cnt['P|' + c[0]])))) for c in deck}
for _ in range(3):
    ts = collections.Counter()
    for c in deck: ts[c[1]] += tick[c]
    tot = sum(ts.values())
    for c in deck:
        sh = ts[c[1]] / tot
        if sh > 0.08: tick[c] = max(1, round(tick[c] * 0.08 / sh))
def share(t):
    out = {}
    for sl, idx in (('P', 0), ('S', 1), ('T', 2)):
        tot = collections.Counter()
        for c in deck: tot[c[idx]] += t[c]
        s = sum(tot.values()); out[sl] = (min(tot.values()) / s, max(tot.values()) / s, len(tot))
    return out
one = {c: 1 for c in deck}
print('tickets total now', len(deck), '| weighted', sum(tick.values()), '| max per class', max(tick.values()))
for name, t in (('now', one), ('weighted', tick)):
    sh = share(t)
    print(name, {k: 'min %.2f%% max %.2f%% of %d specs' % (a * 100, b * 100, n) for k, (a, b, n) in sh.items()})
def offer(t, rng, n=100):
    pool = [c for c in deck for _ in range(t[c])]
    seen, out = set(), []
    while len(out) < n and pool:
        c = pool[rng.randrange(len(pool))]
        out.append(c); pool = [x for x in pool if x != c]
    return out
def coverage(t, runs=40):
    rng = random.Random(7); res = []
    allT = {('P', c[0]) for c in deck} | {('S', c[1]) for c in deck} | {('T', c[2]) for c in deck}
    for r in range(runs):
        seen = set(); k = 0
        while seen != allT and k < 200:
            k += 1; seen |= {x for c in offer(t, rng) for x in (('P', c[0]), ('S', c[1]), ('T', c[2]))}
        res.append(k)
    res.sort(); return res[len(res) // 2], res[-1]
def passive_share(t):
    P = {'Sentinel', 'Retaliator', 'KeeperTertiary', 'TechMedic', 'SkvMedic', 'FieldSurgeon', 'CombatEngineer', 'Saboteur'}
    a = sum(t[c] for c in deck if c[2] in P); return a / sum(t.values())
for name, t in (('now', one), ('weighted', tick)):
    med, worst = coverage(t)
    print('%-9s 8 weaponless tertiaries share %.0f%% | promotions to see all 141 specs: median %d, worst of 40 runs %d' % (name, 100 * passive_share(t), med, worst))
json.dump([['_'.join(c), tick[c]] for c in deck], open('weights_out.json', 'w'))
