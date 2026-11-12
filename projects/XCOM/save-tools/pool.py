"""Faction covert-action pools in the decompressed save (audit/save_blob.bin): every serialized AvailableCovertActions array,
with the nearest preceding Faction_ template name, split into jep-blocked / CI-blocked / other names."""
import struct, re, sys
blob = open('C:/Users/jep/.claude/jobs/0815ca4d/tmp/audit/save_blob.bin', 'rb').read()
JEP = {'FormSoldierBond', 'GatherIntel', 'GatherSupplies', 'SharedAbilityPoints', 'AlienLoot', 'AlienCorpses', 'ExperimentalItem', 'PatrolWilderness', 'UtilityItems'}
CI = {'RecruitExtraFactionSoldier', 'RecruitScientist', 'RecruitEngineer', 'IncreaseIncome', 'RescueSoldier', 'ResistanceContact', 'FacilityLead', 'AlienLoot', 'PrepareCounterDE'}
ODD = {'ExhaustiveTraining', 'IRI_Nuke'}
key = b'AvailableCovertActions\x00'
p, n = 0, 0
while True:
    p = blob.find(key, p)
    if p < 0: break
    q = p + len(key) + 4
    tl = struct.unpack_from('<i', blob, q)[0]
    typ = blob[q + 4:q + 4 + tl - 1].decode('latin1') if 0 < tl < 40 else '?'
    q2 = q + 4 + tl + 4
    size, idx = struct.unpack_from('<ii', blob, q2)
    body = blob[q2 + 8:q2 + 8 + max(0, min(size, 20000))]
    cnt = struct.unpack_from('<i', body, 0)[0] if len(body) >= 4 else -1
    names = [m.decode() for m in re.findall(rb'CovertAction_(\w+)', body)]
    back = blob[max(0, p - 6000):p]
    fac = re.findall(rb'Faction_(Reapers|Skirmishers|Templars)', back)
    f = fac[-1].decode() if fac else '?'
    print('@%d %s %-12s count %d | jep-blocked: %s | CI-blocked: %s | Odd-blocked: %s | other: %s' % (
        p, typ, f, cnt, sorted(set(names) & JEP), sorted(set(names) & CI - {'AlienLoot'}), sorted(set(names) & ODD), sorted(set(names) - JEP - CI - ODD)))
    p += 1; n += 1
print('arrays found', n)
