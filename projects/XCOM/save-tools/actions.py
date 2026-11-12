"""Every covert action state in the decompressed save: template name, bStarted / bCompleted if serialized nearby, offset.
A state object's template is serialized as property m_TemplateName (NameProperty)."""
import struct, re, collections
blob = open('C:/Users/jep/.claude/jobs/0815ca4d/tmp/audit/save_blob.bin', 'rb').read()
JEP = {'FormSoldierBond', 'GatherIntel', 'GatherSupplies', 'SharedAbilityPoints', 'AlienLoot', 'AlienCorpses', 'ExperimentalItem', 'PatrolWilderness', 'UtilityItems'}
CI = {'RecruitExtraFactionSoldier', 'RecruitScientist', 'RecruitEngineer', 'IncreaseIncome', 'RescueSoldier', 'ResistanceContact', 'FacilityLead', 'PrepareCounterDE'}
ODD = {'ExhaustiveTraining', 'IRI_Nuke'}
rows = collections.Counter(); where = collections.defaultdict(list)
for m in re.finditer(rb'CovertAction_(\w+)\x00', blob):
    p = m.start()
    back = blob[max(0, p - 60):p]
    kind = 'template of a state object' if b'm_TemplateName' in back else 'other reference'
    n = m.group(1).decode()
    rows[(n, kind)] += 1; where[(n, kind)].append(p)
for (n, kind), c in sorted(rows.items()):
    tag = 'JEP-BLOCKED' if n in JEP else 'CI-BLOCKED' if n in CI else 'ODD-BLOCKED' if n in ODD else ''
    seg = ''
    if kind.startswith('template'):
        flags = []
        for p in where[(n, kind)]:
            fwd = blob[p:p + 2500]
            flags.append('S' if b'bStarted\x00' in fwd[:fwd.find(b'm_TemplateName', 20) if fwd.find(b'm_TemplateName', 20) > 0 else 2500] else '-')
        seg = 'started flags per state: ' + ''.join(flags)
    print('%-34s %-28s x%d %-12s %s' % (n, kind, c, tag, seg))
