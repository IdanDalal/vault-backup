"""Two log switches in jepFixes so the next launch proves two unproven blocks (2026-11-12 block audit). Keeps each file's line ends."""
import shutil
JD = "C:/Program Files (x86)/Steam/steamapps/common/XCOM 2/XCom2-WarOfTheChosen/XComGame/Mods/jepFixes/Config/"
TMP = 'C:/Users/jep/.claude/jobs/0815ca4d/tmp/'
def append(name, lines, must_end_section):
    p = JD + name
    b = open(p, 'rb').read()
    nl = b'\r\n' if b'\r\n' in b else b'\n'
    txt = b.decode('ascii')
    for l in lines:
        assert l not in txt or l.startswith(';') or l == '', l
    last = [l for l in txt.replace('\r\n', '\n').split('\n') if l.startswith('[')][-1]
    assert last == must_end_section or must_end_section is None, last
    shutil.copyfile(p, TMP + name + '.bak-1112')
    out = b.rstrip(b'\r\n') + nl + nl.join(l.encode('ascii') for l in lines) + nl
    open(p, 'wb').write(out)
    print('appended', len(lines), 'lines to', name, 'eol', 'CRLF' if nl == b'\r\n' else 'LF')
append('XComELR.ini', ['; jepFixes 2026-11-12 (block audit): three more lists printed, to prove FrostAbomination and AdvGeneralM1_LW/M2_LW reach them.',
                       '+ListsToLog="ForcedBossLeader"', '+ListsToLog="ForcedBossLeader_PsionicStorm"', '+ListsToLog="NeutralizeFieldCommander_FieldLeader"'],
       '[EncounterListReplacerWOTC.X2DownloadableContentInfo_EncounterListReplacerWOTC]')
append('XComLootPostMover.ini', ['', '; jepFixes 2026-11-12 (block audit): logging on until a psi loot drop is seen in Launch.log ("Loot Drop was PsiLoot - Timer set at 3").',
                                 '; bEnableLogging is a config bool on the DLCInfo class (X2DownloadableContentInfo_WOTCLootPostMover.uc:11-13). Switch off after the proof.',
                                 '[WOTCLootPostMover.X2DownloadableContentInfo_WOTCLootPostMover]', 'bEnableLogging = true'], None)
