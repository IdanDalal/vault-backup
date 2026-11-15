"""2026-11-15: cut the 12 pistol-primary Stygian Slayer cards (Idi's SNAPSHOT.png). Dry run by default; --apply writes."""
import os, sys, shutil, json, collections
OLD = 'C:/Users/jep/.claude/jobs/94ad0c55/tmp'; TMP = 'C:/Users/jep/.claude/jobs/0815ca4d/tmp/'
sys.path.insert(0, OLD); os.chdir(OLD)
import sim
JF = "C:/Program Files (x86)/Steam/steamapps/common/XCOM 2/XCom2-WarOfTheChosen/XComGame/Mods/jepFixes/Config/XComAmalgamation.ini"
st0 = sim.load(); live0 = {tuple(x[:3]) for x in sim.deck(st0) if not x[3]}
cut = sorted('_'.join(c) for c in live0 if c[1] == 'SkvStygian' and c[0] != 'Androctonus')
print('cut', len(cut), cut)
assert len(cut) == 12
raw = open(JF, 'rb').read().decode('ascii')
assert raw.endswith('\r\n') and raw[raw.rindex('['):].split('\r\n')[0] == '[AmalgamationClassesWOTC.X2DownloadableContentInfo_AmalgamationClassesWOTC]'
for n in cut: assert ('+DisableClass="%s"' % n) not in raw
blk = ['', "; jepFixes 2026-11-15 (Idi's screenshot SNAPSHOT.png): Stygian Slayer's starting perk Snapshot is a penalised shot bound to the primary weapon",
       "; that hides whenever a standard shot is available (X2Ability_SharedPerksRSAbilitySet.uc:1679-1688). It only does something on a sniper",
       "; rifle, which cannot fire after moving. The 12 pistol-primary cards are cut; Androctonus_SkvStygian_SkvScout stays."]
blk += ['+DisableClass="%s"' % n for n in cut]
new = raw.rstrip('\r\n') + '\r\n' + '\r\n'.join(blk) + '\r\n'
orig = sim.files
def files2():
    for mod, p, t in orig():
        yield (mod, p, new if os.path.normcase(os.path.abspath(p)) == os.path.normcase(os.path.abspath(JF)) else t)
sim.files = files2
st1 = sim.load(); live1 = {tuple(x[:3]) for x in sim.deck(st1) if not x[3]}
sim.files = orig
n0, n1 = collections.Counter(), collections.Counter()
for c in live0:
    for x in c: n0[x] += 1
for c in live1:
    for x in c: n1[x] += 1
print('deck %d -> %d | added %s' % (len(live0), len(live1), sorted(live1 - live0)))
print('spec count changes:', {k: (n0[k], n1[k]) for k in sorted(n0) if n0[k] != n1[k]})
print('specs newly under 3:', [(k, n1[k]) for k in n0 if n0[k] >= 3 and n1[k] < 3])
assert len(live1) == len(live0) - 12 and not (live1 - live0)
if '--apply' in sys.argv:
    shutil.copyfile(JF, TMP + 'XComAmalgamation.ini.bak-1115')
    open(JF, 'wb').write(new.encode('ascii'))
    json.dump([list(c) for c in sorted(live1)], open(TMP + 'deck_1115.json', 'w'))
    print('APPLIED. DisableClass lines:', new.count('+DisableClass='))
