"""Candidate extra Amalgamation rules, each tested on the post-sniper deck (cards removed) and on Idi's 44 picks
(picks a rule would have killed = evidence against it)."""
import json, os, collections
os.chdir(os.path.dirname(os.path.abspath(__file__)))
spec = json.load(open('spec_casing.json'))
names = sorted({v['name'] for v in spec.values()}, key=len, reverse=True)
def split(c):
    out, rest = [], c
    while rest:
        for n in names:
            if rest.lower().startswith(n.lower()) and (len(rest) == len(n) or rest[len(n)] == '_'):
                out.append(n.lower()); rest = rest[len(n) + 1:]; break
        else:
            return None
    return out
def w(k):
    v = spec[k]; return v['weapons'][0] if v['weapons'] else None
pool = [split(l.strip()) for l in open('pool_save.txt') if l.strip()]
picks = [split(l.split('\t')[0]) for l in open('roster_amalg.tsv') if l.strip()]
ALLOW = {"gremlin", "grenade_launcher", "psiamp", "bioamp", "sparkbit"}
snip = {k for k, v in spec.items() if v['slot'] == 'Primary' and any('sniper' in x for x in v['weapons'])}
def sniper_kill(c):
    p, s, t = c
    if p not in snip: return False
    if w(s) not in (None, 'empty') and w(s) not in ALLOW: return True
    v = spec[t]
    return bool(v['weapons']) and v['weapons'][0] != 'empty' and v['slots'][0] == 'eInvSlot_SecondaryWeapon' and v['weapons'][0] not in ALLOW
deck = [c for c in pool if c and not sniper_kill(c)]
print('deck after sniper rule', len(deck))
PISTOL = {'pistol', 'sidearm'}
rules = {
 'P1 pistol secondary only with a pistol primary': lambda c: w(c[1]) in PISTOL and w(c[0]) not in PISTOL,
 'P1b pistol secondary only with pistol primary OR pistol tertiary': lambda c: w(c[1]) in PISTOL and w(c[0]) not in PISTOL and w(c[2]) not in PISTOL,
 'P1c = P1b with Commissar counted as a pistol tertiary': lambda c: w(c[1]) in PISTOL and w(c[0]) not in PISTOL and w(c[2]) not in PISTOL and c[2] != 'commissar',
 'P2 generic passive tertiary (Sentinel/Retaliator/Keeper/TechMedic) with a weapon-less secondary': lambda c: c[2] in ('sentinel', 'retaliator', 'keepertertiary', 'techmedic') and w(c[1]) in (None, 'empty'),
 'P3 melee secondary (sword/knife/wristblade) on a long-range-device primary? (n/a) | melee secondary with a sniper-type primary already done': lambda c: False,
}
for name, f in rules.items():
    killed = [c for c in deck if f(c)]
    pk = [p for p in picks if p and f(p)]
    print('\n%s\n  deck cards removed: %d | his picks it would have removed: %d %s' % (name, len(killed), len(pk), ['_'.join(x) for x in pk][:8]))
# which of his picks have pistol secondaries, with primary weapon
print('\npicks with pistol/sidearm secondary:')
for p in picks:
    if p and w(p[1]) in PISTOL:
        print('  ', '_'.join(p), '| primary weapon', w(p[0]), '| tertiary weapon', w(p[2]))
# extras cut by the literal sniper whitelist that are arguably long-range
EXTRA = {'iri_rocket_launcher', 'holotargeter', 'supercomputer', 'bow', 'boltcaster', 'claymore'}
cnt = collections.Counter()
for c in pool:
    if c and c[0] in snip:
        for k in c[1:]:
            if w(k) in EXTRA:
                cnt[(spec[k]['name'], w(k))] += 1
print('\nsniper cards cut only by unlisted ranged gear:', dict(cnt), 'total', sum(cnt.values()))
