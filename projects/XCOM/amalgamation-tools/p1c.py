"""09-28 round 2 (Idi): release sniper x Officer (holotargeter) and sniper x ChryssalidWhisperer (summoner) from jep's
09-28 block; add P1c as exact class names under DisableClass (NumInDeck 0 -> Choose My Class skips them,
UIChooseClass_WOTC_ChooseMyClass.uc:355). P1c: pistol/autopistol secondary only with a pistol primary or a pistol
tertiary (Commissar counts)."""
import json, os, re, shutil
os.chdir(os.path.dirname(os.path.abspath(__file__)))
JF = "C:/Program Files (x86)/Steam/steamapps/common/XCOM 2/XCom2-WarOfTheChosen/XComGame/Mods/jepFixes/Config/XComAmalgamation.ini"
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
ALLOW = {"gremlin", "grenade_launcher", "psiamp", "bioamp", "sparkbit"}
RELEASE = {"officer", "chryssalidwhisperer"}
snip = {k for k, v in spec.items() if v['slot'] == 'Primary' and any('sniper' in x for x in v['weapons'])}
def sniper_kill(c):
    p, s, t = c
    if p not in snip: return False
    if s not in RELEASE and w(s) not in (None, 'empty') and w(s) not in ALLOW: return True
    v = spec[t]
    return t not in RELEASE and bool(v['weapons']) and v['weapons'][0] != 'empty' and v['slots'][0] == 'eInvSlot_SecondaryWeapon' and v['weapons'][0] not in ALLOW
PISTOL = {'pistol', 'sidearm'}
def p1c(c):
    p, s, t = c
    return w(s) in PISTOL and w(p) not in PISTOL and w(t) not in PISTOL and t != 'commissar'

raw = [l.strip() for l in open('pool_save.txt') if l.strip()]
deck = [(r, split(r)) for r in raw]
assert all(c for _, c in deck)
after_snipe = [(r, c) for r, c in deck if not sniper_kill(c)]
dis = sorted(r for r, c in after_snipe if p1c(c))
final = [(r, c) for r, c in after_snipe if not p1c(c)]
print('deck', len(deck), '-> after sniper rule (with releases)', len(after_snipe), '-> after P1c', len(final))
print('sniper cards now', sum(1 for _, c in after_snipe if c[0] in snip), '| P1c classes', len(dis))
picks = [split(l.split('\t')[0]) for l in open('roster_amalg.tsv') if l.strip()]
print('his picks hit by P1c:', ['_'.join(p) for p in picks if p1c(p)])

# edit the file
B = 'XComAmalgamation.ini.bak-0928b'
shutil.copyfile(JF, B)
data = open(JF, 'rb').read().decode('ascii')
lines = data.split('\r\n')
start = next(i for i, l in enumerate(lines) if l.startswith("; jepFixes 2026-09-28, Idi's R6 sniper whitelist"))
snipnames = {spec[k]['name'].lower() for k in snip}
out, removed = [], 0
for i, l in enumerate(lines):
    m = re.match(r'\+IncompatibleSpecs=\(A="([^"]+)", B="([^"]+)"\)$', l)
    if i > start and m and m.group(1).lower() in snipnames and m.group(2).lower() in RELEASE:
        removed += 1; continue
    out.append(l)
while out and out[-1] == '':
    out.pop()
out += ['',
        "; jepFixes 2026-09-28 (round 2, Idi): released for snipers: Officer (holotargeter, acts from the sniper's tile) and",
        "; ChryssalidWhisperer (summons a Chryssalid; its perks buff the pet). Rockets stay excluded. %d pairs removed above." % removed,
        '',
        '[AmalgamationClassesWOTC.X2DownloadableContentInfo_AmalgamationClassesWOTC]',
        "; jepFixes 2026-09-28, Idi's P1c (R5): a pistol or autopistol secondary only with a pistol primary or a pistol tertiary",
        "; (SkvScout, Smoker; Commissar counts, its perks fire from the pistol). Pairs cannot express a three-spec rule, so these are",
        "; exact class names: DisableClass sets NumInDeck 0 and Choose My Class skips NumInDeck 0 (UIChooseClass_WOTC_ChooseMyClass.uc:355).",
        "; Generated from the 09-27 deck by p1c.py: %d classes. A name missing in a future deck only logs 'No class template'." % len(dis)]
out += ['+DisableClass="%s"' % r for r in dis]
open(JF, 'wb').write(('\r\n'.join(out) + '\r\n').encode('ascii'))
print('pairs removed', removed, '| DisableClass lines', len(dis))
