"""Sniper whitelist rule for Amalgamation (Idi 2026-09-28): sniper primaries only with gremlin / grenade launcher /
psi amp / bio amp / BIT. Pairwise IncompatibleSpecs lines, exact casing from configs, simulated on the saved deck."""
import re, os, glob, json, collections
os.chdir(os.path.dirname(os.path.abspath(__file__)))
W = "C:/Program Files (x86)/Steam/steamapps/workshop/content/268500/"
JF = "C:/Program Files (x86)/Steam/steamapps/common/XCOM 2/XCom2-WarOfTheChosen/XComGame/Mods/jepFixes/Config/XComAmalgamation.ini"
ALLOW = {"gremlin", "grenade_launcher", "psiamp", "bioamp", "sparkbit"}
active = [l.split('\t')[0] for l in open('active.tsv', encoding='utf-8')]

def rd(p):
    b = open(p, 'rb').read()
    if b[:2] in (b'\xff\xfe', b'\xfe\xff'):
        return b.decode('utf-16')
    return b.decode('utf-8', errors='replace')

spec = {}  # lower -> dict(name, slot, weapons[list, displayed first])
for wid in active:
    if wid == '0':
        continue
    for p in glob.glob(W + wid + '/Config/**/*.ini', recursive=True):
        t = rd(p)
        for m in re.finditer(r'^\s*\+(Primary|Secondary|Tertiary)Specs\s*=\s*\(\s*Spec\s*=\s*"([^"]+)"(.*?)(?=^\s*\+\w+\s*=|\Z)', t, re.M | re.S):
            slot, name, body = m.group(1), m.group(2), m.group(3)
            weps = re.findall(r'AllowedWeapons\[(\d+)\]\s*=\s*\(\s*WeaponType\s*=\s*"([^"]+)"\s*,\s*SlotType\s*=\s*(\w+)', body)
            weps = sorted(weps, key=lambda x: int(x[0]))
            spec.setdefault(name.lower(), dict(name=name, slot=slot, weapons=[w.lower() for _, w, _s in weps],
                                               slots=[s for _, _w, s in weps]))
prim = {k: v for k, v in spec.items() if v['slot'] == 'Primary'}
sec = {k: v for k, v in spec.items() if v['slot'] == 'Secondary'}
ter = {k: v for k, v in spec.items() if v['slot'] == 'Tertiary'}
snip = sorted(k for k, v in prim.items() if any('sniper' in w for w in v['weapons']))
print('specs parsed P/S/T', len(prim), len(sec), len(ter), '| sniper primaries', [prim[k]['name'] for k in snip])

def disp(v):
    return v['weapons'][0] if v['weapons'] else None
EMPTY = {k for k, v in sec.items() if disp(v) in (None, 'empty')}
bad_sec = sorted(k for k, v in sec.items() if k not in EMPTY and disp(v) not in ALLOW)
def ter_bad(v):
    # only a weapon that takes the secondary slot competes with the sniper's secondary
    if not v['weapons'] or v['weapons'][0] == 'empty':
        return False
    return v['slots'][0] == 'eInvSlot_SecondaryWeapon' and v['weapons'][0] not in ALLOW
bad_ter = sorted(k for k, v in ter.items() if ter_bad(v))
print('tertiary weapon slots:', ', '.join('%s[%s@%s]' % (v['name'], v['weapons'][0], v['slots'][0].replace('eInvSlot_', '')) for v in ter.values() if v['weapons'] and v['weapons'][0] != 'empty'))
print('empty-slot secondaries kept:', sorted(sec[k]['name'] for k in EMPTY))
print('secondaries excluded vs snipers (%d):' % len(bad_sec), ', '.join('%s[%s]' % (sec[k]['name'], disp(sec[k])) for k in bad_sec))
print('weapon tertiaries excluded vs snipers (%d):' % len(bad_ter), ', '.join('%s[%s]' % (ter[k]['name'], disp(ter[k])) for k in bad_ter))

# existing pairs
ex = set()
for a, b in re.findall(r'IncompatibleSpecs\s*=\s*\(\s*A\s*=\s*"([^"]+)"\s*,\s*B\s*=\s*"([^"]+)"', rd(JF)):
    ex.add(frozenset((a.lower(), b.lower())))
new = []
for p in snip:
    for s in bad_sec + bad_ter:
        pair = frozenset((p, s))
        if pair in ex:
            continue
        other = sec.get(s) or ter.get(s)
        new.append('+IncompatibleSpecs=(A="%s", B="%s")' % (prim[p]['name'], other['name']))
print('new lines', len(new), '| already present', len(snip) * len(bad_sec + bad_ter) - len(new))
open('sniper_lines.ini', 'w', newline='').write('\r\n'.join(new) + '\r\n')

# simulate on the saved deck (names in the save use exact spec casing joined by _)
pool = [l.strip() for l in open('pool_save.txt') if l.strip()]
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
kill = set(frozenset((p, s)) for p in snip for s in bad_sec + bad_ter)
tot = snipc = left = 0; unparsed = 0; keptcat = collections.Counter()
for c in pool:
    parts = split(c)
    if not parts or len(parts) != 3:
        unparsed += 1; continue
    tot += 1
    if parts[0] in snip:
        snipc += 1
        if not any(frozenset((parts[0], x)) in kill for x in parts[1:]):
            left += 1
            keptcat[disp(sec[parts[1]]) or 'empty+' + (disp(ter[parts[2]]) or 'utility')] += 1
print('deck', tot, '(unparsed %d) | sniper cards %d -> %d' % (unparsed, snipc, left))
print('kept sniper cards by secondary:', dict(keptcat))
json.dump({k: v for k, v in spec.items()}, open('spec_casing.json', 'w'))
