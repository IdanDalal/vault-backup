"""Tier every card in the live deck by Idi's pick rules R1-R8 (amalgamation-pick-rules.md)."""
import json, collections, sim
spec = {v['name'].lower(): v for v in json.load(open('specs_now.json')).values()}
deck = [x[:3] for x in sim.deck(sim.load()) if not x[3]]
def sw(n):
    return {w for w, s in spec[n.lower()]['weapons'] if s == 'SecondaryWeapon'} - {'empty'}
DEVICE = {'gremlin', 'grenade_launcher', 'psiamp', 'sparkbit', 'arcthrower', 'supercomputer', 'iri_rocket_launcher', 'holotargeter', 'bioamp'}
MEDIC = {'techmedic', 'fieldsurgeon', 'skvmedic'}
PASSIVE = {'sentinel', 'retaliator', 'keepertertiary'}
UTIL = {'combatengineer', 'saboteur', 'daeva', 'haresootsman'}
def tier(p, s, t):
    S, Tw = sw(s), sw(t)
    if Tw and S and (Tw & S): return 'A1 stack: tertiary feeds the weapon the secondary carries'
    if Tw and not S: return 'A2 fill: tertiary weapon fills an empty secondary slot'
    if Tw: return 'A3 tertiary weapon beside a different secondary weapon (exemption)'
    tl = t.lower()
    if tl in UTIL: return 'B1 utility tertiary' + (' on a device secondary (R3)' if S & DEVICE else '')
    if tl in PASSIVE: return 'C1 generic passive tertiary (R2 low priority)'
    if tl in MEDIC: return 'C2 healing tertiary (R8 accepted, never sought)'
    return 'B2 other'
rows = collections.defaultdict(list)
for p, s, t in deck:
    rows[tier(p, s, t)].append((t, s, p))
json.dump({k: v for k, v in rows.items()}, open('tiers_out.json', 'w'))
for k in sorted(rows):
    c = collections.Counter(t for t, _, _ in rows[k])
    print('%-70s %5d  %s' % (k, len(rows[k]), dict(c.most_common(8))))
print('total', len(deck))
