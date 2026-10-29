"""Parse every +Primary/Secondary/TertiarySpecs entry from active AML mods (workshop + local) into specs_now.json."""
import json, re, glob, os, collections
d = json.load(open(r'C:/XCOM2 AML 1.6.0-beta/settings.json', encoding='utf-8-sig'))
allm = [x for c in d['Mods']['Entries'].values() for x in c['Entries'] if x.get('isActive')]
def rd(p):
    b = open(p, 'rb').read()
    if b[:2] in (b'\xff\xfe', b'\xfe\xff'):
        return b.decode('utf-16')
    return b.decode('utf-8', errors='replace')
ENTRY = re.compile(r'^\s*\+(Primary|Secondary|Tertiary)Specs\s*=\s*\(\s*Spec\s*=\s*"([^"]+)"(.*?)(?=^\s*[+\-!]\w+\s*=|^\s*\[\w|\Z)', re.M | re.S)
WEP = re.compile(r'AllowedWeapons\[(\d+)\]\s*=\s*\(\s*WeaponType\s*=\s*"([^"]+)"\s*,\s*SlotType\s*=\s*(\w+)')
spec = {}; seen = collections.defaultdict(list)
for x in allm:
    for p in glob.glob(x['Path'] + '/Config/**/*.ini', recursive=True):
        t = rd(p)
        for m in ENTRY.finditer(t):
            slot, name, body = m.group(1), m.group(2), m.group(3)
            weps = sorted(WEP.findall(body), key=lambda w: int(w[0]))
            k = '%s|%s' % (slot, name.lower())
            seen[k].append(x['Name'])
            spec.setdefault(k, dict(name=name, slot=slot, weapons=[(w.lower(), s.replace('eInvSlot_', '')) for _, w, s in weps],
                                    mod=x['Name'], wid=x.get('WorkshopID'), file=p, raw=m.group(0)))
json.dump(spec, open('specs_now.json', 'w'), indent=0)
print(collections.Counter(v['slot'] for v in spec.values()))
for k, v in sorted(spec.items()):
    print(v['slot'][0], v['name'], '|', ' '.join('%s@%s' % w for w in v['weapons']), '|', v['mod'][:45])
