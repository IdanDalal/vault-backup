import json, sys
a = json.load(open(sys.argv[1], encoding='utf-8-sig')); b = json.load(open(r'C:/XCOM2 AML 1.6.0-beta/settings.json', encoding='utf-8-sig'))
fa = {x['ID']: x for c in a['Mods']['Entries'].values() for x in c['Entries']}
fb = {x['ID']: x for c in b['Mods']['Entries'].values() for x in c['Entries']}
print('added:', [(k, fb[k]['isActive'], fb[k]['Path']) for k in fb if k not in fa])
print('changed existing entries:', [k for k in fa if fa[k] != fb.get(k)])
print('top-level equal except Mods:', all(a[k] == b[k] for k in a if k != 'Mods'))
