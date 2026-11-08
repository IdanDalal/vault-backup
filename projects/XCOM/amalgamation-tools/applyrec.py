"""Idi 11-08 'all rec': delete the jep pair lines selected by combo.py's recommended options; verify against deck_rec.json."""
import json, shutil
exec(open('combo.py').read().split("sm = lambda")[0])
TMP = "C:/Users/jep/.claude/jobs/94ad0c55/tmp/"
shutil.copyfile(JFP, TMP + 'XComAmalgamation.ini.bak-1108b')
allf = lambda a, b, i: any(OPTS[r][1](a, b, i) for r in REC)
out, gone = [], []
for i, l in enumerate(LINES):
    m = re.match(r'^\+IncompatibleSpecs=\(A="(\w+)", B="(\w+)"\)', l)
    if m and allf(m.group(1).lower(), m.group(2).lower(), i):
        gone.append(l); continue
    out.append(l)
k = out.index("; jepFixes 2026-10-29, Idi's weapon slot optimization. A spec 'carries' a weapon in its own slot (primary spec: primary")
note = ["; jepFixes 2026-11-08 (Idi: 'all rec', amalgamation-zero-specs-2026-11-08.md): %d pairs deleted below and above." % len(gone),
        '; X1 R3 fix: R3 pairs dropped for AlienHunter2, DronePilot, SwordMaster, Riot, Ironclad, LegendaryWarrior (their trees never fire',
        ';    from the primary slot; listed primary weapons are permissions). W-rule pairs kept.',
        '; Exemptions by design: Ravager + empty-slot secondaries; Savage + Butterfly knife; Brigand under shotgun primaries; SkvRaider any',
        ';    primary; SwordMaster with sword secondaries and sword primaries with shield secondaries; both Xeno Zoologists + pistol/autopistol',
        ';    secondaries; Androctonus + pistol/autopistol secondaries (sniper whitelist + W2); AlienHunter2 exempt from W1.', '']
out = out[:k] + note + out[k:]
open(JFP, 'wb').write('\r\n'.join(out).encode('ascii'))
sim.files = orig_files
d = [x[:3] for x in sim.deck(sim.load()) if not x[3]]
rec = json.load(open(TMP + 'deck_rec.json'))
print('deleted', len(gone), '| deck', len(d), '| identical to priced set:', sorted(map(tuple, d)) == sorted(map(tuple, rec)))
