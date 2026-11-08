import json, glob, re, sim
d = json.load(open(r'C:/XCOM2 AML 1.6.0-beta/settings.json', encoding='utf-8-sig'))
act = [x for c in d['Mods']['Entries'].values() for x in c['Entries'] if x.get('isActive')]
st = sim.load()
want = {x.lower(): x for x in st['P'] + st['S'] + st['T']}
name = {}
for x in act:
    for p in glob.glob(x['Path'] + '/Localization/**/Amalgamation.int', recursive=True):
        cur = None
        for l in sim.rd(p).splitlines():
            m = re.match(r'^\s*\[(\w+)\]', l)
            if m: cur = m.group(1).lower(); continue
            m = re.match(r'^\s*SpecName\s*=\s*"?([^"\r\n]*)', l)
            if cur in want and m: name[want[cur]] = m.group(1).strip()
missing = [v for v in want.values() if v not in name]
print('named', len(name), 'missing', missing)
json.dump(name, open('names.json', 'w'), indent=0)
print({k: v for k, v in name.items() if k.lower() != v.lower().replace(' ', '')})
