"""What-if: release pairs in memory (no file touched) and list the classes that would be newly built."""
import json, os, sys, re, collections
os.chdir('C:/Users/jep/.claude/jobs/94ad0c55/tmp'); sys.path.insert(0, '.')
exec(open('audit2.py').read().split("if __name__")[0])
exec(open('tiers.py').read().split("deck = ")[1].split("rows = collections")[0].split("\n", 1)[1].replace("spec[n.lower()]", "SPEC[n.lower()]").replace("- {'empty'}", "- {'empty', 'canister'}"))
st = sim.load()
before = {tuple(x[:3]) for x in sim.deck(st)}
sq = {x: {a for a, r, f in tree(x) if r == 0 and f} for x in st['P'] + st['S'] + st['T']}
def dup(c): return (sq[c[0]] & sq[c[1]]) | (sq[c[0]] & sq[c[2]]) | (sq[c[1]] & sq[c[2]])
def whatif(rel):
    st2 = dict(st); st2['inc'] = list(st['inc'])
    for a, b in rel:
        hit = [x for x in st2['inc'] if {x[0], x[1]} == {a.lower(), b.lower()}]
        print('release %s x %s: %d pair line(s) by %s' % (a, b, len(hit), sorted({h[2][:45] for h in hit})))
        st2['inc'] = [x for x in st2['inc'] if x not in hit]
    new = [tuple(x[:3]) for x in sim.deck(st2) if tuple(x[:3]) not in before]
    print('  newly built classes:', len(new))
    for c in new:
        a = audit(c)
        print('    %-44s tier %s | loadout %s+%s dead %s | shared start perk %s' % ('_'.join(c), tier(*c)[:2], a[1], a[2], a[0], sorted(dup(c)) or '-'))
whatif([('HareCaptain', 'HareBuckler')])
whatif([('Ravager', 'HareBuckler')])
whatif([('Pistoleer', 'SkvAssassin')])
