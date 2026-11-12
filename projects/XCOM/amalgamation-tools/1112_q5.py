import json, os, sys, re, collections
os.chdir('C:/Users/jep/.claude/jobs/94ad0c55/tmp'); sys.path.insert(0, '.')
exec(open('audit2.py').read().split("if __name__")[0])
exec(open('tiers.py').read().split("deck = ")[1].split("rows = collections")[0].split("\n", 1)[1].replace("spec[n.lower()]", "SPEC[n.lower()]").replace("- {'empty'}", "- {'empty', 'canister'}"))
st = sim.load()
built = [tuple(x[:3]) for x in sim.deck(st)]
live = {tuple(x[:3]) for x in sim.deck(st) if not x[3]}
sq = {x: {a for a, r, f in tree(x) if r == 0 and f} for x in st['P'] + st['S'] + st['T']}
def dup(c): return (sq[c[0]] & sq[c[1]]) | (sq[c[0]] & sq[c[2]]) | (sq[c[1]] & sq[c[2]])
print('built', len(built), 'live', len(live))
want = sys.argv[1:]
for c in built:
    if all(w in c for w in want):
        a = audit(c)
        print('%-44s %s | %-4s | loadout %s+%s dead %s | dup %s | %s' % ('_'.join(c), 'LIVE' if c in live else 'cut ', tier(*c)[:2], a[1], a[2], a[0], sorted(dup(c)), sorted(sq[c[2]])))
pairs = collections.defaultdict(set)
for a, b, m in st['inc']:
    pairs[a].add((b, m)); pairs[b].add((a, m))
if len(want) == 2:
    print('--- tertiaries banned against either spec:')
    for t in st['T']:
        why = [(x, m) for w in want for x, m in pairs[w.lower()] if x == t.lower()]
        if why: print('   ', t, [m[:40] for _, m in why], '|', tier(want[0], want[1], t)[:2])
