"""Static check of jepFixes sitrep / dark-event filters against the current active mod set."""
import json, glob, re, os
d = json.load(open(r'C:/XCOM2 AML 1.6.0-beta/settings.json', encoding='utf-8-sig'))
allm = [x for c in d['Mods']['Entries'].values() for x in c['Entries']]
byws = {x.get('WorkshopID'): x for x in allm}
for wid, what in [(3739636065, 'Multiple Sitreps REDUX'), (3078247580, 'Scaling Dark Events (More Dark Events)'),
                  (2567230730, 'Covert Infiltration'), (2608952868, 'CI bridge'), (2608960168, 'CI bridge'),
                  (2795578857, 'ARFM Dark Events'), (2974710943, 'AbiziOTS (4 blocked names)')]:
    x = byws.get(wid); print('%-40s %s' % (what, (x['Name'], 'ACTIVE' if x['isActive'] else 'off') if x else 'NOT SUBSCRIBED'))
JF = "C:/Program Files (x86)/Steam/steamapps/common/XCOM 2/XCom2-WarOfTheChosen/XComGame/Mods/jepFixes/Config/"
act = [x for x in allm if x.get('isActive') and 'jepFixes' not in x['Path']]
def rd(p):
    b = open(p, 'rb').read()
    return b.decode('utf-16') if b[:2] in (b'\xff\xfe', b'\xfe\xff') else b.decode('utf-8', 'replace')
plus = {}
for x in act:
    for p in glob.glob(x['Path'] + '/Config/**/*.ini', recursive=True):
        base = os.path.basename(p).lower()
        for l in rd(p).splitlines():
            if l.lstrip().startswith('+'):
                plus.setdefault(base, set()).add(l.lstrip()[1:])
for f in sorted(os.listdir(JF)):
    if not f.endswith('.ini'):
        continue
    lines = [l for l in rd(JF + f).splitlines() if l.startswith('-')]
    if not lines:
        continue
    miss = [l for l in lines if l[1:] not in plus.get(f.lower(), set())]
    print('%-32s minus lines %3d | no exact + twin in an active mod: %d %s' % (f, len(lines), len(miss), [m[:90] for m in miss[:4]]))
# every sitrep template name that active mods define, vs block list
names = set()
for x in act:
    for p in glob.glob(x['Path'] + '/Src/**/*.uc', recursive=True):
        t = rd(p)
        names |= set(re.findall(r"CREATE_X2TEMPLATE\(class'X2SitRepTemplate',\s*\w+,\s*'(\w+)'", t))
    for p in glob.glob(x['Path'] + '/Config/**/*.ini', recursive=True):
        names |= set(re.findall(r'^\s*\+?SitReps?\s*=\s*"?(\w+)', rd(p), re.M))
blocked = re.findall(r'\+BlockedSitReps = "(\w+)"', rd(JF + 'XCom_Sitrep_Categories_REDUX.ini'))
print('blocked names', len(blocked), '| blocked names no active mod defines:', [b for b in blocked if b not in names])
# new mods touching sitreps or dark events
new = [1215333362, 1539496987, 1662019265, 3810810829, 3813053768, 3813477158, 3817729073, 3817769424, 3818382586,
       3818382631, 3818382710, 3818392160, 3818445197, 3820228421, 3822004642, 3822286199, 3825121780]
for wid in new:
    x = byws[wid]; hits = []
    for p in glob.glob(x['Path'] + '/**/*.*', recursive=True):
        if p.endswith(('.ini', '.uc')):
            t = rd(p)
            n = len(re.findall(r'sitrep|darkevent', t, re.I))
            if n:
                hits.append('%s:%d' % (os.path.relpath(p, x['Path']), n))
    if hits:
        print('NEW MOD', x['Name'], hits[:6])
