"""For each P+S pair in the built deck whose best WORKING tertiary is below tier A, find tertiaries that would make a working
tier-A card (0 dead guaranteed, <=1 dead random-roll perk) and are blocked by exactly one pair. Report blocker owners."""
import collections, itertools, json, sim
exec(open('audit.py').read().split("if __name__")[0])
exec(open('tiers.py').read().split("deck = ")[0].split("import json, collections, sim")[1])
exec('def sw(n):\n    return {w for w, s in SPEC[n.lower()]["weapons"] if s == "SecondaryWeapon"} - {"empty"}')
exec(open('tiers.py').read().split("DEVICE =")[1].split("rows = collections")[0].join(["DEVICE =", ""]) if False else '')
DEVICE = {'gremlin', 'grenade_launcher', 'psiamp', 'sparkbit', 'arcthrower', 'supercomputer', 'iri_rocket_launcher', 'holotargeter', 'bioamp'}
def tierA(s, t):
    S, Tw = sw(s), sw(t)
    return bool(Tw) and (not S or bool(Tw & S))
st = sim.load()
src = collections.defaultdict(list)
for a, b, mod in st['inc']: src[frozenset((a, b))].append(mod)
A = json.load(open('audit_all.json'))
built = [tuple(v['c']) for v in A.values()]
work = {tuple(v['c']) for v in A.values() if v['fixed'] == 0}
byPS = collections.defaultdict(list)
for c in built: byPS[(c[0], c[1])].append(c)
out = []
for (p, s), cs in byPS.items():
    if any(tierA(s, c[2]) for c in cs if c in work): continue
    for t in st['T']:
        if (p, s, t) in cs or not tierA(s, t): continue
        bl = [q for q in (frozenset((p.lower(), t.lower())), frozenset((s.lower(), t.lower()))) if q in src]
        if len(bl) != 1: continue
        (fx, tot), pc, sc, dead = audit((p, s, t))
        if fx or tot > 1: continue
        out.append(('%s_%s_%s' % (p, s, t), tuple(sorted(bl[0])), src[bl[0]], tot))
own = collections.Counter('jep' if o[2] == ['jepFixes'] else 'author' for o in out)
print('upgrade candidates', len(out), dict(own))
for o in sorted(out, key=lambda o: o[1]): print('  ', o)
json.dump(out, open('upgrades_out.json', 'w'))
