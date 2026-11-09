C = "C:/Program Files (x86)/Steam/steamapps/common/XCOM 2/XCom2-WarOfTheChosen/XComGame/Mods/jepFixes/Config/XComAmalgamation.ini"
import shutil
shutil.copyfile(C, "C:/Users/jep/.claude/jobs/94ad0c55/tmp/XComAmalgamation.ini.bak-1109b")
txt = open(C, 'rb').read().decode('ascii').rstrip('\r\n')
assert txt.rindex('[') == txt.index('[AmalgamationClassesWOTC.X2DownloadableContentInfo_AmalgamationClassesWOTC]')
add = ['', "; jepFixes 2026-11-09: Savage & Maniac 3080030743 restricts Hamstring to a sword primary (for Savage); Agent 2811335882",
       "; gets Hamstring as a guaranteed knife perk on the secondary slot, so it was deleted on every gun-primary Agent card.",
       '+AbilityRestrictions=(AbilityName="Hamstring", WeaponCat="combatknife", InvSlot=eInvSlot_SecondaryWeapon)']
open(C, 'wb').write((txt + '\r\n' + '\r\n'.join(add) + '\r\n').encode('ascii'))
print('ok')
