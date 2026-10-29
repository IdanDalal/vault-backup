"""2026-10-29 (Idi): weapon slot optimization. Inserts the W1-W6 pairs, the Commissar self-pair and the author-ban releases
at the end of the [AmalgamationClassesWOTC.X2SoldierClass_Amalgamation] section of jepFixes XComAmalgamation.ini, and drops
the 09-28 P1c DisableClass block (W2b is strictly wider). Inputs from the job tmp: slotrule_out.json, release_out.json.
Every '-' line is a byte copy of an author '+' line (release.py). Usage: python slotapply.py <tmpdir>"""
import json, os, shutil, sys
TMP = sys.argv[1]
JF = "C:/Program Files (x86)/Steam/steamapps/common/XCOM 2/XCom2-WarOfTheChosen/XComGame/Mods/jepFixes/Config/XComAmalgamation.ini"
o = json.load(open(os.path.join(TMP, 'slotrule_out.json')))
rel = json.load(open(os.path.join(TMP, 'release_out.json')))
shutil.copyfile(JF, os.path.join(TMP, 'XComAmalgamation.ini.bak-1029'))
lines = open(JF, 'rb').read().decode('ascii').split('\r\n')
i_pexm = lines.index('[AmalgamationPexmBridge.X2DownloadableContentInfo_AmalgamationPexmBridge]')
i_dlc = lines.index('[AmalgamationClassesWOTC.X2DownloadableContentInfo_AmalgamationClassesWOTC]')
assert i_pexm < i_dlc and all(l.startswith(('+DisableClass=', ';')) or l == '' for l in lines[i_dlc + 1:])
# the PexmBridge comment block sits right above its header; insert above that comment
ins = i_pexm
while ins > 0 and lines[ins - 1].startswith(';'):
    ins -= 1
G = o['G']
block = ['',
         "; jepFixes 2026-10-29, Idi's weapon slot optimization. A spec 'carries' a weapon in its own slot (primary spec: primary",
         "; slot; secondary/tertiary spec: secondary slot), checked against where each tree's abilities land.",
         '; W1 sword primary (%s) <-> sword secondary (%s).' % (', '.join(G['SwP']), ', '.join(G['SwS'])),
         '; W2 pistol primary (%s) only with a secondary whose kit holds a pistol (adds Ironclad: pistol + shield);' % ', '.join(G['PiP']),
         ';    pistol secondary (%s) only with a pistol primary. Replaces the 09-28 P1c DisableClass list.' % ', '.join(G['PiS']),
         '; W3 gauntlet: Burner <-> Heavy, SkvFirebug.  W4 gremlin tertiary (SkvArtisan, HareModernPirate) only with a gremlin secondary.',
         '; W5 cannon primary (%s) only with SkvSiegeGunner (the reverse was already the authors\' rule).' % ', '.join(G['CaP']),
         '; W6 shield secondary (%s) <-> shield tertiary (%s).' % (', '.join(G['ShS']), ', '.join(G['ShT'])),
         '; Commissar: self-pair; AreSpecsIncompatible (X2SoldierClass_Amalgamation.uc:548) then matches every class holding it.',
         '; Releases: authors banned most same-weapon pairings (taste, no shared squaddie skill). Each - line is a byte copy of',
         "; the author's + line; jepFixes loads after the workshop mods. jep's own 09-16..09-28 pairs stay. Tools: slotrule.py, release.py.",
         '; Deck simulation (active mods 2026-10-29): 1,888 -> 1,497 classes. New campaign only.']
block += [l for _, l in rel]
block += ['+IncompatibleSpecs=(A="Commissar", B="Commissar")']
block += [l for _, l in o['lines']]
block += ['']
out = lines[:ins] + block + lines[ins:i_dlc]
while out and out[-1] == '':
    out.pop()
data = ('\r\n'.join(out) + '\r\n').encode('ascii')
open(JF, 'wb').write(data)
print('inserted', len(block), 'lines at', ins, '| dropped P1c block lines', len(lines) - i_dlc, '| bytes', len(data))
