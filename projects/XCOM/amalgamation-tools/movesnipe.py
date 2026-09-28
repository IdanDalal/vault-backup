"""Move jep's 09-28 sniper block (and its round-2 note) out of the [AmalgamationPexmBridge...] section, where it was
appended by mistake, into [AmalgamationClassesWOTC.X2SoldierClass_Amalgamation], right before the Pexm comment."""
import shutil, re
JF = "C:/Program Files (x86)/Steam/steamapps/common/XCOM 2/XCom2-WarOfTheChosen/XComGame/Mods/jepFixes/Config/XComAmalgamation.ini"
shutil.copyfile(JF, "C:/Users/jep/.claude/jobs/d60d4ae0/tmp/XComAmalgamation.ini.bak-0928c")
L = open(JF, 'rb').read().decode('ascii').split('\r\n')
pexm_c = next(i for i, l in enumerate(L) if l.startswith('; jepFixes 2026-09-18: Amalgamation Pexm Bridge'))
s0 = next(i for i, l in enumerate(L) if l.startswith("; jepFixes 2026-09-28, Idi's R6 sniper whitelist"))
dls = next(i for i, l in enumerate(L) if l.startswith('[AmalgamationClassesWOTC.X2DownloadableContentInfo_AmalgamationClassesWOTC]'))
# block = from sniper comment to the line before the DLCInfo section header, trailing blanks trimmed
block = L[s0:dls]
while block and block[-1] == '':
    block.pop()
rest = L[:s0] + L[dls:]
while rest[s0 - 1] == '' and rest[s0 - 2] == '':
    rest.pop(s0 - 1);
# insert before the Pexm comment (index unchanged, it precedes s0)
new = rest[:pexm_c] + block + [''] + rest[pexm_c:]
open(JF, 'wb').write('\r\n'.join(new).encode('ascii'))
# report section per line
sec = None; counts = {}
for l in new:
    m = re.match(r'^\[(.+)\]$', l)
    if m: sec = m.group(1); continue
    if l.startswith('+IncompatibleSpecs'): counts[(sec, 'pairs')] = counts.get((sec, 'pairs'), 0) + 1
    if l.startswith('+PsionicSpecs'): counts[(sec, 'psionic')] = counts.get((sec, 'psionic'), 0) + 1
    if l.startswith('+DisableClass'): counts[(sec, 'disable')] = counts.get((sec, 'disable'), 0) + 1
for k, v in counts.items():
    print(k, v)
print('lines', len(L), '->', len(new))
