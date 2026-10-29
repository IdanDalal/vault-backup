"""Idi 2026-10-29 'weapon slot optimization' rules for Amalgamation, as IncompatibleSpecs pairs.
A spec 'carries' W when W sits in its own slot: primary spec -> PrimaryWeapon entries, secondary/tertiary spec ->
SecondaryWeapon entries (checked against where each tree's abilities land, slotuse.json)."""
import json, collections, sys
import sim
spec = json.load(open('specs_now.json'))
st = sim.load()
P, S, T = st['P'], st['S'], st['T']
lk = {}
for k, v in spec.items():
    lk[v['name'].lower()] = v
def own(n, slot):
    v = lk[n.lower()]
    want = 'PrimaryWeapon' if slot == 'P' else 'SecondaryWeapon'
    return {w for w, s in v['weapons'] if s == want}
def grp(names, slot, cats):
    return sorted(n for n in names if own(n, slot) & cats)
SWORD, PISTOL, GAUNT, GREM, CANNON, SHIELD = {'sword'}, {'pistol', 'sidearm'}, {'lw_gauntlet'}, {'gremlin'}, {'cannon'}, {'shield'}
G = dict(
    SwP=grp(P, 'P', SWORD), SwS=grp(S, 'S', SWORD),
    PiP=grp(P, 'P', PISTOL), PiS=grp(S, 'S', PISTOL),
    PiAny=sorted(n for n in S if {w for w, _ in lk[n.lower()]['weapons']} & PISTOL),  # Ironclad: shield + pistol kit
    GaS=grp(S, 'S', GAUNT), GaT=grp(T, 'T', GAUNT),
    GrS=grp(S, 'S', GREM), GrT=grp(T, 'T', GREM),
    CaP=grp(P, 'P', CANNON), CaS=['SkvSiegeGunner'],
    ShS=grp(S, 'S', SHIELD), ShT=grp(T, 'T', SHIELD))
SLOT = dict(P=P, S=S, T=T)
# (rule id, members, member slot, partner slot, allowed partners, note)
RULES = [
    ('W1a', G['SwP'], 'P', 'S', G['SwS'], 'sword primary only with a sword secondary'),
    ('W1b', G['SwS'], 'S', 'P', G['SwP'], 'sword secondary only with a sword primary'),
    ('W2a', G['PiP'], 'P', 'S', G['PiAny'], 'pistol primary only with a secondary whose kit holds a pistol'),
    ('W2b', G['PiS'], 'S', 'P', G['PiP'], 'pistol secondary only with a pistol primary (replaces P1c)'),
    ('W3a', G['GaS'], 'S', 'T', G['GaT'], 'gauntlet secondary only with a gauntlet tertiary'),
    ('W3b', G['GaT'], 'T', 'S', G['GaS'], 'gauntlet tertiary only with a gauntlet secondary'),
    ('W4', G['GrT'], 'T', 'S', G['GrS'], 'gremlin tertiary only with a gremlin secondary'),
    ('W5a', G['CaP'], 'P', 'S', G['CaS'], 'cannon primary only with a cannon secondary'),
    ('W5b', G['CaS'], 'S', 'P', G['CaP'], 'cannon secondary only with a cannon primary'),
    ('W6a', G['ShS'], 'S', 'T', G['ShT'], 'shield secondary only with a shield tertiary'),
    ('W6b', G['ShT'], 'T', 'S', G['ShS'], 'shield tertiary only with a shield secondary'),
]
existing = {frozenset((a, b)) for a, b, _ in st['inc']}
lines = collections.OrderedDict(); per_rule = {}
for rid, mem, ms, ps, allow, note in RULES:
    al = {x.lower() for x in allow}; cnt = 0
    for m in mem:
        for y in SLOT[ps]:
            if y.lower() in al:
                continue
            pr = frozenset((m.lower(), y.lower()))
            if pr in existing or pr in lines:
                continue
            lines[pr] = (rid, '+IncompatibleSpecs=(A="%s", B="%s")' % (m, y)); cnt += 1
    per_rule[rid] = cnt
if __name__ == '__main__':
    for k, v in G.items():
        print(k, v)
    print('new pairs per rule', per_rule, 'total', len(lines))
    json.dump({'G': G, 'lines': [v for v in lines.values()]}, open('slotrule_out.json', 'w'), indent=0)
