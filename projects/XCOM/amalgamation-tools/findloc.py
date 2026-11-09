import glob, sys, re, json, sim
d = json.load(open(r'C:/XCOM2 AML 1.6.0-beta/settings.json', encoding='utf-8-sig'))
act = [x for c in d['Mods']['Entries'].values() for x in c['Entries'] if x.get('isActive')]
pats = [p.lower() for p in sys.argv[1:]]
for x in act:
    for p in glob.glob(x['Path'] + '/Localization/**/*.int', recursive=True) + glob.glob(x['Path'] + '/Config/**/*.ini', recursive=True):
        t = sim.rd(p); cur = None
        for i, l in enumerate(t.splitlines()):
            m = re.match(r'^\s*\[([^\]]+)\]', l)
            if m: cur = m.group(1)
            if any(q in l.lower() for q in pats):
                print('%s | %s:%d [%s] %s' % (x['Name'][:30], p.split('268500')[-1][-70:], i + 1, cur, l.strip()[:200]))
