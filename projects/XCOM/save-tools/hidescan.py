"""Do any of the 509 hidden weapon templates exist as item states in the latest save (audit/save_blob.bin)?
An item state serializes its template as m_TemplateName; count those, and other references, per hidden name."""
import re, collections
blob = open('C:/Users/jep/.claude/jobs/0815ca4d/tmp/audit/save_blob.bin', 'rb').read()
ini = open("C:/Program Files (x86)/Steam/steamapps/common/XCOM 2/XCom2-WarOfTheChosen/XComGame/Mods/jepFixes/Config/XComWeaponSkinReplacer.ini", encoding='latin1').read()
names = sorted({m.group(1).strip().strip('"') for m in re.finditer(r'^\+WEAPONS_TO_HIDE\s*=\s*(\S+)', ini, re.M)})
print('hidden names', len(names))
low = blob.lower()
state, other = collections.Counter(), collections.Counter()
for n in names:
    key = n.lower().encode() + b'\x00'
    p = 0
    while True:
        p = low.find(key, p)
        if p < 0: break
        if low[p - 1:p] not in (b'_',) and not low[p - 1:p].isalnum():
            (state if b'm_templatename' in low[max(0, p - 60):p] else other)[n] += 1
        p += len(key)
print('hidden names present as item states:', len(state), '| total states', sum(state.values()))
for n, c in state.most_common(25): print('   ', n, c)
print('hidden names referenced otherwise:', len(other), list(other.items())[:10])
# control: a weapon that must exist
for ctl in (b'AssaultRifle_CV', b'Shotgun_CV', b'Sword_CV'):
    c = sum(1 for m in re.finditer(re.escape(ctl) + b'\x00', blob) if b'm_TemplateName' in blob[max(0, m.start() - 60):m.start()])
    print('control', ctl.decode(), 'item states:', c)
