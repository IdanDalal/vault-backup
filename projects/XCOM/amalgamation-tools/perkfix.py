"""1109: undo config collisions that delete guaranteed perks spec-wide.
 - ShadowOps_SlamFire / ShadowOps_Fearsome: Sentry 3318688033 + Drumax 3330436783 restrict them to a rifle primary
   (Amalgamation AbilityRestrictions = remove unless ANY entry matches), killing them on Pathfinder (hunter rifle),
   Maniac and others. Add one entry per primary category the specs use.
 - NimbleHands: only entry is Modular Sparks' SparkRifles set; Rook (3315321306) gets it as a squaddie perk on a rifle.
   Add AllMainWeapons (Musashi's Mods Fixes unions every set an ability is listed under)."""
import json, shutil
C = "C:/Program Files (x86)/Steam/steamapps/common/XCOM 2/XCom2-WarOfTheChosen/XComGame/Mods/jepFixes/Config/"
TMP = "C:/Users/jep/.claude/jobs/94ad0c55/tmp/"
spec = json.load(open(TMP + 'specs_now.json'))
pcats = sorted({w for v in spec.values() if v['slot'] == 'Primary' for w, s in v['weapons'] if s == 'PrimaryWeapon' and w != 'empty'})
f = C + 'XComAmalgamation.ini'
shutil.copyfile(f, TMP + 'XComAmalgamation.ini.bak-1109a')
txt = open(f, 'rb').read().decode('ascii').rstrip('\r\n')
HDR = '[AmalgamationClassesWOTC.X2DownloadableContentInfo_AmalgamationClassesWOTC]'
assert txt.count(HDR) == 1 and txt.rindex('[') == txt.index(HDR), 'DLC section must be the last section'
add = ['', "; jepFixes 2026-11-09: Sentry and Drumax restrict Slam Fire and Fearsome to a rifle primary for their own rifle specs;",
       "; AbilityRestrictions removes the perk unless ANY entry matches, so Pathfinder (hunter rifle) and Maniac lost guaranteed perks.",
       "; One entry per primary weapon category used by any spec keeps both perks alive everywhere (rifle specs unchanged)."]
for perk in ('ShadowOps_SlamFire', 'ShadowOps_Fearsome'):
    for c in pcats:
        if c == 'rifle': continue
        add.append('+AbilityRestrictions=(AbilityName="%s", WeaponCat="%s", InvSlot=eInvSlot_PrimaryWeapon)' % (perk, c))
open(f, 'wb').write((txt + '\r\n' + '\r\n'.join(add) + '\r\n').encode('ascii'))
g = C + 'XComAbilityToSlotReassignment.ini'
assert not __import__('os').path.exists(g)
open(g, 'wb').write('\r\n'.join([
    "; jepFixes 2026-11-09: Nimble Hands' only weapon entry is Modular Sparks' SparkRifles set, so Ability To Slot Reassignment",
    "; deleted it from Rook (rifle squaddie perk) and two other specs. Musashi's Mods Fixes unions every set an ability is listed",
    "; under (X2DLCInfo_WOTCMusashiModFixes.uc:463), so this line adds every main weapon to it.", '',
    '[AbilityToSlotReassignment.AbilityToSlotReassignmentLib]',
    '+AbilityWeaponCategories=(AbilityName=NimbleHands, WeaponCategorySetName=AllMainWeapons)', '']).encode('ascii'))
print('primary cats', len(pcats), pcats, '| restriction lines', len(add) - 4)
