"""Register a local jep mod in AML settings.json (clone of the jepFixes entry). Usage: aml_add.py <ModName> <description>"""
import json, copy, datetime, sys
N, D = sys.argv[1], sys.argv[2]
P = r"C:\XCOM2 AML 1.6.0-beta\settings.json"
raw = open(P, 'rb').read()
bom = raw.startswith(b'\xef\xbb\xbf')
s = json.loads(raw.decode('utf-8-sig'))
ents = s['Mods']['Entries']['Unsorted']['Entries']
allents = [e for c in s['Mods']['Entries'].values() for e in c['Entries']]
if any(e['ID'] == N for e in allents):
    raise SystemExit('already present')
src = next(e for e in ents if e['ID'] == 'jepFixes')
e = copy.deepcopy(src)
now = datetime.datetime.now().astimezone().isoformat()
e.update(ID=N, Name=N, Path=src['Path'].replace('jepFixes', N), Size=0, isActive=True,
         DateAdded=now, DateCreated=now, DateUpdated=now,
         Index=max(x['Index'] for x in allents) + 1, Description=D)
ents.append(e)
out = json.dumps(s, indent=2, ensure_ascii=False).replace('\n', '\r\n')
open(P, 'wb').write((b'\xef\xbb\xbf' if bom else b'') + out.encode('utf-8'))
chk = json.load(open(P, encoding='utf-8-sig'))
n = [x for c in chk['Mods']['Entries'].values() for x in c['Entries']]
print('entries', len(allents), '->', len(n), 'active', sum(1 for x in n if x['isActive']))
