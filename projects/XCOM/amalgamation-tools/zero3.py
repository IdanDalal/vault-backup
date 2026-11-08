"""Classify the 09-16 block pairs that kill author-approved combos of the zero specs (R1/R2/R3/R4 by re-testing each rule)."""
import json, re, collections, itertools, sim
exec(open('zero2.py').read().split("res = {}")[0])
spec = {v['name'].lower(): v for v in json.load(open('specs_now.json')).values()}
slotuse = json.load(open('slotuse.json'))
def wps(n, slot):
    return {w for w, s in spec[n]['weapons'] if s == slot}
# squaddie skills
T_ = '\n'.join(sim.rd(p) for x in json.load(open(r'C:/XCOM2 AML 1.6.0-beta/settings.json', encoding='utf-8-sig'))['Mods']['Entries'].values() for x in x['Entries'] if x.get('isActive') for p in __import__('glob').glob(x['Path'] + '/Config/**/XComAmalgamation.ini', recursive=True))
sq = {}
for m in re.finditer(r'\+SpecDataset\s*=\s*\(\s*Spec\s*=\s*"([^"]+)"(.*?)Ranks\[1\]', T_, re.S):
    sq.setdefault(m.group(1).lower(), set(a.lower() for a in re.findall(r'AbilityName\s*=\s*"([^"]+)"', m.group(2))))
def classify(a, b):
    sa, sb = slot_of[a], slot_of[b]
    out = []
    if 'P' in (sa, sb):
        p, o = (a, b) if sa == 'P' else (b, a)
        dem = wps(o, 'PrimaryWeapon') - {'empty'}
        if dem and not (dem & wps(p, 'PrimaryWeapon')):
            out.append('R3 %s lists primary %s, %s carries %s' % (o, sorted(dem), p, sorted(wps(p, 'PrimaryWeapon'))))
    else:
        ws = {w for w in wps(a, 'SecondaryWeapon')} - {'empty'}; wt = {w for w in wps(b, 'SecondaryWeapon')} - {'empty'}
        if not ws and not wt: out.append('R1 no secondary weapon on either')
        elif ws and wt and not (ws & wt): out.append('R2 %s %s vs %s %s' % (a, sorted(ws), b, sorted(wt)))
    if sq.get(a, set()) & sq.get(b, set()): out.append('R4 shared squaddie %s' % sorted(sq[a] & sq[b]))
    return '; '.join(out) or 'unclassified'
for z in ZERO:
    sl = slot_of[z.lower()]
    combos = [(p, s, t) for p in ([z] if sl == 'P' else P) for s in ([z] if sl == 'S' else S) for t in ([z] if sl == 'T' else T)]
    appr = [c for c in combos if not any(p in auth for p in pairs(c))]
    cnt = collections.Counter()
    for c in appr:
        for p in pairs(c):
            if any(b and b.startswith('R1-R5') for b in jep.get(p, ())):
                cnt[p] += 1
    rule = collections.Counter()
    print('\n#', z)
    for p, n in cnt.most_common():
        a, b = sorted(p) if len(p) == 2 else (list(p)[0],) * 2
        c = classify(a, b); rule[c.split(' ')[0]] += n
    print('  by rule:', dict(rule))
    for p, n in cnt.most_common(8):
        a, b = sorted(p) if len(p) == 2 else (list(p)[0],) * 2
        print('   %3d  %s x %s : %s' % (n, a, b, classify(a, b)))
