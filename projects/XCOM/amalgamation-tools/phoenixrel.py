"""Release jep's 09-16 R2 pairs Phoenix x weapon tertiaries: R2 counted Phoenix's canister as a secondary-slot weapon, but a canister
beside a chemthrower sits in Mitzruti's aux slot (Idi 11-10, MZ_StrategyElement_MZAuxSlot.uc:84). Firebug stays (W3 gauntlet rule)."""
import re, shutil
JF = "C:/Program Files (x86)/Steam/steamapps/common/XCOM 2/XCom2-WarOfTheChosen/XComGame/Mods/jepFixes/Config/XComAmalgamation.ini"
shutil.copyfile(JF, "C:/Users/jep/.claude/jobs/94ad0c55/tmp/XComAmalgamation.ini.bak-1110c")
REL = {frozenset(('phoenix', t)) for t in ('agent', 'commando', 'engineer', 'executioner', 'liquidator', 'officer')}
lines = open(JF, 'rb').read().decode('ascii').split('\r\n')
out, gone = [], []
for l in lines:
    m = re.match(r'^\+IncompatibleSpecs=\(A="(\w+)", B="(\w+)"\)', l)
    if m and frozenset((m.group(1).lower(), m.group(2).lower())) in REL:
        gone.append(l); continue
    out.append(l)
k = out.index("; jepFixes 2026-10-29, Idi's weapon slot optimization. A spec 'carries' a weapon in its own slot (primary spec: primary")
out = out[:k] + ["; jepFixes 2026-11-10: %d R2 pairs Phoenix x weapon tertiary deleted (Agent, Commando, Engineer, Executioner, Liquidator," % len(gone),
                 ";    Officer): a canister beside a chemthrower sits in Mitzruti's aux slot, so Phoenix leaves the secondary slot free.", ''] + out[k:]
open(JF, 'wb').write('\r\n'.join(out).encode('ascii'))
print('deleted', len(gone), gone)
