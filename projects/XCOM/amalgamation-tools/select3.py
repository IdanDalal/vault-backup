"""1110 selection (replaces select2's cut block). Releases stay as they are.
 1 working cards only (no dead guaranteed perk)                                  [audit.py]
 2 NEW (Idi 11-10): no two specs share a guaranteed starting perk (e.g. Fire Pistol, Haywire Protocol)
 3 best tertiary tier per primary+secondary; a filler-only pair keeps one card
 4 floor: a spec under 3 cards gains cards from NEW primary+secondary pairs only; a spec at 0 may take the best card of an existing pair
 5 rare alternatives (Idi 11-10): a spec with exactly 2 cards that differ in one slot keeps one: fewer dead perks, then the
   alternative with more tier-A cards elsewhere gives way, then the scarcer alternative stays; never zeroes the alternative."""
import json, shutil, collections, sim
TMP = "C:/Users/jep/.claude/jobs/94ad0c55/tmp/"
JF = "C:/Program Files (x86)/Steam/steamapps/common/XCOM 2/XCom2-WarOfTheChosen/XComGame/Mods/jepFixes/Config/XComAmalgamation.ini"
FLOOR = 3
shutil.copyfile(JF, TMP + 'XComAmalgamation.ini.bak-1110a')
lines = open(JF, 'rb').read().decode('ascii').split('\r\n')
out, skip = [], False
for l in lines:
    if l.startswith("; jepFixes 2026-11-09, cut (replaces the 11-08 D4 list)") or l.startswith("; jepFixes 2026-11-10, cut"):
        skip = True; continue
    if skip and (l.startswith(';') or l.startswith('+DisableClass=')): continue
    skip = False; out.append(l)
while out and out[-1] == '': out.pop()
open(JF, 'wb').write(('\r\n'.join(out) + '\r\n').encode('ascii'))
exec(open(TMP + 'audit.py').read().split("if __name__")[0])
exec(open(TMP + 'tiers.py').read().split("deck = ")[1].split("rows = collections")[0].split("\n", 1)[1].replace("spec[n.lower()]", "SPEC[n.lower()]"))
st = sim.load()
built = [tuple(x[:3]) for x in sim.deck(st)]
aud = {c: audit(c) for c in built}
sq = {x: {a for a, r, f in tree(x) if r == 0 and f} for x in st['P'] + st['S'] + st['T']}
def dup(c): return (sq[c[0]] & sq[c[1]]) | (sq[c[0]] & sq[c[2]]) | (sq[c[1]] & sq[c[2]])
work = [c for c in built if aud[c][0][0] == 0]
nodup = [c for c in work if not dup(c)]
rank = lambda c: (lambda k: 0 if k.startswith('A') else (1 if k.startswith('B') else 2))(tier(*c))
dead = lambda c: aud[c][0][1]
tcount = collections.Counter(c[2] for c in nodup)
def select(pool):
    byPS = collections.defaultdict(list)
    for c in pool: byPS[(c[0], c[1])].append(c)
    keep = set()
    for ps, cs in byPS.items():
        best = min(rank(c) for c in cs)
        top = [c for c in cs if rank(c) == best]
        if best < 2: keep |= set(top)
        else: keep.add(sorted(top, key=lambda c: (0 if tier(*c).startswith('C1') else 1, dead(c), tcount[c[2]]))[0])
    return keep
keep = select(nodup)
log = collections.defaultdict(list)
def count(i, x): return sum(1 for c in keep if c[i] == x)
for i, sl in enumerate(('P', 'S', 'T')):
    for x in st[sl]:
        have = count(i, x)
        if have >= FLOOR: continue
        pairs_in = {(c[0], c[1]) for c in keep}
        new = sorted((c for c in nodup if c[i] == x and c not in keep and (c[0], c[1]) not in pairs_in), key=lambda c: (rank(c), dead(c), c))
        for c in new[:FLOOR - have]: keep.add(c); pairs_in.add((c[0], c[1])); log['floor new pair'].append('_'.join(c))
        if count(i, x) == 0:
            for pool, why in ((nodup, 'floor min 1'), (work, 'floor min 1, allows shared starting perk')):
                cand = sorted((c for c in pool if c[i] == x), key=lambda c: (rank(c), dead(c), c))
                if cand: keep.add(cand[0]); log[why].append('_'.join(cand[0])); break
# 5 rare alternatives
aTier = collections.Counter()
for c in keep:
    if rank(c) == 0:
        for i, x in enumerate(c): aTier[(i, x)] += 1
for i, sl in enumerate(('P', 'S', 'T')):
    for x in st[sl]:
        cs = sorted(c for c in keep if c[i] == x)
        if len(cs) != 2: continue
        diff = [j for j in range(3) if cs[0][j] != cs[1][j]]
        if len(diff) != 1: continue
        j = diff[0]
        def key(c):
            alt = c[j]
            return (dead(c), -(aTier[(j, alt)] - (1 if rank(c) == 0 else 0)), sum(1 for k in keep if k[j] == alt))
        # the alternative with MORE tier-A cards elsewhere gives way: sort so the card to keep comes first
        ranked = sorted(cs, key=lambda c: (dead(c), aTier[(j, c[j])] - (1 if rank(c) == 0 else 0), sum(1 for k in keep if k[j] == c[j])))
        drop = ranked[1]
        if sum(1 for k in keep if k[j] == drop[j]) <= 1: continue
        keep.discard(drop); log['rare alternative dropped'].append('%s (kept %s)' % ('_'.join(drop), '_'.join(ranked[0])))
cut = sorted('_'.join(c) for c in built if c not in keep)
blk = ['', "; jepFixes 2026-11-10, cut (replaces the 11-09 list): working cards only (perk audit); no two specs sharing a guaranteed",
       "; starting perk (Idi 11-10); best tertiary tier per primary+secondary pair; floor of %d cards per spec from NEW pairs only" % FLOOR,
       "; (min 1); a rare spec's two near-identical cards resolved to one (Idi 11-10). %d cut, %d stay. Tools: pipeline.py, select3.py." % (len(cut), len(keep))]
blk += ['+DisableClass="%s"' % n for n in cut]
txt = open(JF, 'rb').read().decode('ascii').rstrip('\r\n')
assert txt.rindex('[') == txt.index('[AmalgamationClassesWOTC.X2DownloadableContentInfo_AmalgamationClassesWOTC]')
open(JF, 'wb').write((txt + '\r\n' + '\r\n'.join(blk) + '\r\n').encode('ascii'))
st2 = sim.load(); live = [tuple(x[:3]) for x in sim.deck(st2) if not x[3]]
n = collections.Counter()
for p, s, t in live: n[p] += 1; n[s] += 1; n[t] += 1
prev = {tuple(x) for x in json.load(open(TMP + 'deck_1109.json'))}
print('deck', len(live), '(was %d) | equals selection:' % len(prev), set(live) == keep, '| broken:', sum(1 for c in live if aud[c][0][0]),
      '| shared starting perk:', sum(1 for c in live if dup(c)))
print('specs at 0:', [x for x in st2['P'] + st2['S'] + st2['T'] if n[x] == 0])
for k, v in log.items(): print(k, len(v), v[:14])
print('removed vs 11-09:', len(prev - set(live)), '| added:', len(set(live) - prev))
tc = collections.Counter(rank(c) for c in live); print('tiers A/B/C', tc[0], tc[1], tc[2], '| DisableClass total', len(st2['dis']))
json.dump([list(c) for c in live], open(TMP + 'deck_1110.json', 'w'))
json.dump({'_'.join(c): [v[0][0], v[0][1], v[1], v[2], [[d[0], d[1], d[2], d[3]] for d in v[3]]] for c, v in aud.items()}, open(TMP + 'audit_1110.json', 'w'))
