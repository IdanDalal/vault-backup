"""Add stable CHL 1134256495 to IgnoredDependencies of the 7 red mods (beta CHL 1796402257 is active). Text-level edit,
backup first, then verify only those fields changed."""
import json, re, shutil
S = r'C:/XCOM2 AML 1.6.0-beta/settings.json'
PRE = r'D:/work/aml-settings-2026-10-29-pre.json'
POST = r'D:/work/aml-settings-2026-10-29.json'
IDS = [1539496987, 1662019265, 3810810829, 3813053768, 3818392160, 3818445197, 3820228421]
shutil.copyfile(S, PRE)
txt = open(S, 'rb').read().decode('utf-8')
for wid in IDS:
    m = re.search(r'"WorkshopID": %d,' % wid, txt); assert m, wid
    start = txt.rfind('"Index":', 0, m.start()); end = txt.find('"Index":', m.end())
    seg = txt[start:end]
    mm = re.search(r'"IgnoredDependencies": \[\]', seg); assert mm, ('not empty', wid)
    indent = re.search(r'\n( *)"IgnoredDependencies"', seg).group(1)
    new = '"IgnoredDependencies": [\r\n%s  1134256495\r\n%s]' % (indent, indent)
    txt = txt[:start] + seg[:mm.start()] + new + seg[mm.end():] + txt[end:]
open(S, 'wb').write(txt.encode('utf-8'))
a = json.load(open(PRE, encoding='utf-8-sig')); b = json.load(open(S, encoding='utf-8-sig'))
fa = {x['ID']: x for c in a['Mods']['Entries'].values() for x in c['Entries']}
fb = {x['ID']: x for c in b['Mods']['Entries'].values() for x in c['Entries']}
print('changed fields:', [(k, f, fb[k][f]) for k in fa for f in fa[k] if fa[k][f] != fb[k].get(f)])
print('top-level equal except Mods:', all(a[k] == b[k] for k in a if k != 'Mods'))
act = {x.get('WorkshopID') for x in fb.values() if x.get('isActive')}
red = [x['Name'] for x in fb.values() if x.get('isActive') and
       [d for d in x.get('Dependencies') or [] if d not in act and d not in (x.get('IgnoredDependencies') or [])]]
print('active mods still missing a dependency:', red)
shutil.copyfile(S, POST)
