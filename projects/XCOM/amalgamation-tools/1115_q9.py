"""Stygian Slayer (SnapShotRS on the primary: useful only on a sniper rifle). Which sniper primaries may pair with it, who bans the rest,
and what a release of the jepFixes-only bans would build."""
import json, os, sys, re, collections
os.chdir('C:/Users/jep/.claude/jobs/94ad0c55/tmp'); sys.path.insert(0, '.')
exec(open('audit2.py').read().split("if __name__")[0])
exec(open('tiers.py').read().split("deck = ")[1].split("rows = collections")[0].split("\n", 1)[1].replace("spec[n.lower()]", "SPEC[n.lower()]").replace("- {'empty'}", "- {'empty', 'canister'}"))
st = sim.load()
before = {tuple(x[:3]) for x in sim.deck(st)}
live = {tuple(x[:3]) for x in sim.deck(st) if not x[3]}
sq = {x: {a for a, r, f in tree(x) if r == 0 and f} for x in st['P'] + st['S'] + st['T']}
def dup(c): return (sq[c[0]] & sq[c[1]]) | (sq[c[0]] & sq[c[2]]) | (sq[c[1]] & sq[c[2]])
pairs = collections.defaultdict(list)
for a, b, m in st['inc']: pairs[frozenset((a, b))].append(m)
SEC = 'SkvStygian'
snipers = [p for p in st['P'] if any(w == 'sniper_rifle' and sl == 'PrimaryWeapon' for w, sl in SPEC[p.lower()]['weapons'])]
rel = []
n = collections.Counter()
for c in live:
    for x in c: n[x] += 1
for p in snipers:
    ban = pairs.get(frozenset((p.lower(), SEC.lower())))
    own = [w for w, sl in SPEC[p.lower()]['weapons'] if sl == 'PrimaryWeapon']
    print('%-14s cards now %2d primary %s | %s' % (p, n[p], own, ('BANNED by ' + '; '.join(sorted({b[:40] for b in ban}))) if ban else 'allowed'))
    if ban and set(ban) == {'jepFixes'}: rel.append(p)
print('jepFixes-only bans:', rel)
st2 = dict(st); st2['inc'] = [x for x in st['inc'] if not (x[2] == 'jepFixes' and {x[0], x[1]} in [{p.lower(), SEC.lower()} for p in rel])]
new = [tuple(x[:3]) for x in sim.deck(st2) if tuple(x[:3]) not in before]
print('newly built by releasing them:', len(new))
for c in new:
    a = audit(c)
    print('    %-44s tier %s | loadout %s+%s dead %s | shared start perk %s' % ('_'.join(c), tier(*c)[:2], a[1], a[2], a[0], sorted(dup(c)) or '-'))
