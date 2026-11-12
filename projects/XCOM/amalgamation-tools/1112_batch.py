"""2026-11-12 batch on Idi's 'all rec' (K2, K3, K4). Dry run by default; --apply writes.
K2 new jepFixes XComIsmsRogue.ini: Blindside accepts pistol + sidearm.
K3 delete jepFixes pair HareCaptain x HareBuckler; DisableClass the 12 pistol-primary Buckler cards + Captain_Buckler_Sootsman.
K4 byte-copied -IncompatibleSpecs for the Pistoleer author's Pistoleer x SkvAssassin ban; DisableClass Pistoleer_HareSwash_Sentinel."""
import os, sys, re, shutil, json, collections
OLD = 'C:/Users/jep/.claude/jobs/94ad0c55/tmp'
TMP = 'C:/Users/jep/.claude/jobs/0815ca4d/tmp/'
sys.path.insert(0, OLD); os.chdir(OLD)
import sim
JD = "C:/Program Files (x86)/Steam/steamapps/common/XCOM 2/XCom2-WarOfTheChosen/XComGame/Mods/jepFixes/Config/"
JF = JD + 'XComAmalgamation.ini'
APPLY = '--apply' in sys.argv
st0 = sim.load()
built0 = {tuple(x[:3]) for x in sim.deck(st0)}
live0 = {tuple(x[:3]) for x in sim.deck(st0) if not x[3]}
# --- K4: find the author's raw line
rel = []
for mod, p, t in sim.files():
    if 'jepfixes' in p.lower(): continue
    sec = ''
    for l in t.splitlines():
        s = l.strip()
        m = re.match(r'^\[([^\]]+)\]', s)
        if m: sec = m.group(1).strip().lower(); continue
        if sec != sim.SEC_CLS or not l.lstrip().startswith('+IncompatibleSpecs'): continue
        mm = re.search(r'A\s*=\s*"?(\w+)"?\s*,\s*B\s*=\s*"?(\w+)"?', l)
        if mm and {mm.group(1).lower(), mm.group(2).lower()} == {'pistoleer', 'skvassassin'}:
            rel.append((mod, '-' + l.lstrip()[1:].rstrip('\r\n')))
print('K4 author lines found:', [(m[:50], repr(l)) for m, l in rel])
assert len(rel) == 1
# --- edit the jepFixes text
raw = open(JF, 'rb').read().decode('ascii')
assert '\r\n' in raw and raw.endswith('\r\n')
L = raw[:-2].split('\r\n')
pair = '+IncompatibleSpecs=(A="HareCaptain", B="HareBuckler")'
assert L.count(pair) == 1
i = L.index(pair)
L[i] = "; jepFixes 2026-11-12 (Idi K3): the pair HareCaptain x HareBuckler stood here (W1, 10-29). Deleted: Buckler's starting perk Buckle Your Swash fires only after a melee attack, so it needs a melee primary beside its pistol."
j = next(k for k, l in enumerate(L) if l.startswith('; jepFixes 2026-09-18: Amalgamation Pexm Bridge'))
assert L[j + 2].startswith('[AmalgamationPexmBridge'), L[j:j + 3]
while L[j - 1] == '': j -= 1
ins = ['', "; jepFixes 2026-11-12 (Idi K4): released the Pistoleer author's ban on Assassin. Only one class gets built by it,",
       "; Pistoleer_HareSwash_SkvAssassin (sword tertiary on Swash's sword); it replaces the filler card Pistoleer_HareSwash_Sentinel.",
       rel[0][1]]
L[j:j] = ins
BUCK = ['%s_HareBuckler_%s' % (p, t) for p in ('Fusilier', 'Pistoleer', 'Gunfighter', 'Vigilante', 'HareQuartermaster', 'Akimbo') for t in ('SkvScout', 'Smoker')]
cut = BUCK + ['HareCaptain_HareBuckler_HareSootsman', 'Pistoleer_HareSwash_Sentinel']
for n in BUCK + ['Pistoleer_HareSwash_Sentinel']: assert tuple(n.split('_')) in live0, n
for n in cut: assert ('+DisableClass="%s"' % n) not in raw, n
L += ['', "; jepFixes 2026-11-12 (Idi 'all rec', screens-audit-2026-11-12.md). K3: the 12 pistol-primary Buckler cards (no melee attack to",
      "; trigger Buckle Your Swash; Akimbo's Pistol Whip arrives at the 4th rank) and the lower-tier Sootsman card of the released Captain x",
      "; Buckler pair. K4: the Sentinel filler on Pistoleer + Swash. 14 cut."]
L += ['+DisableClass="%s"' % n for n in cut]
new = '\r\n'.join(L) + '\r\n'
assert new[new.rindex('['):].split('\r\n')[0] == '[AmalgamationClassesWOTC.X2DownloadableContentInfo_AmalgamationClassesWOTC]'
rogue = ("; jepFixes 2026-11-12 (Idi K2). Rogue's starting perk Blindside adds flanking damage only when the firing weapon's category is on this\r\n"
         "; list (Isms_Effect_Blindside.uc:15; Mitzruti's Perk Pack 1561030099 ships SMG, Bullpup, Vektor_Rifle). Every Rogue card sits on a\r\n"
         "; pistol primary, so pistol and sidearm (autopistol) join the list.\r\n\r\n"
         "[MitzrutiPerkPack.Isms_Effect_Blindside]\r\n+Blindside_WeaponCats=pistol\r\n+Blindside_WeaponCats=sidearm\r\n")
# --- simulate the candidate without touching the live file: swap sim.files for one that substitutes the new text
orig_files = sim.files
def files2():
    for mod, p, t in orig_files():
        yield (mod, p, new if os.path.normcase(os.path.abspath(p)) == os.path.normcase(os.path.abspath(JF)) else t)
sim.files = files2
st1 = sim.load()
built1 = {tuple(x[:3]) for x in sim.deck(st1)}
live1 = {tuple(x[:3]) for x in sim.deck(st1) if not x[3]}
sim.files = orig_files
print('built %d -> %d | newly built: %s | no longer built: %s' % (len(built0), len(built1), sorted('_'.join(c) for c in built1 - built0), sorted('_'.join(c) for c in built0 - built1)))
print('deck %d -> %d | added: %s' % (len(live0), len(live1), sorted('_'.join(c) for c in live1 - live0)))
print('removed:', sorted('_'.join(c) for c in live0 - live1))
n0, n1 = collections.Counter(), collections.Counter()
for c in live0:
    for x in c: n0[x] += 1
for c in live1:
    for x in c: n1[x] += 1
print('spec count changes:', {k: (n0[k], n1[k]) for k in sorted(set(n0) | set(n1)) if n0[k] != n1[k]})
print('specs at 0:', [x for x in st1['P'] + st1['S'] + st1['T'] if n1[x] == 0])
assert live1 - live0 == {('HareCaptain', 'HareBuckler', 'SkvScout'), ('HareCaptain', 'HareBuckler', 'Smoker'), ('Pistoleer', 'HareSwash', 'SkvAssassin')}
assert len(live1) == 707
if APPLY:
    shutil.copyfile(JF, TMP + 'XComAmalgamation.ini.bak-1112b')
    open(JF, 'wb').write(new.encode('ascii'))
    assert not os.path.exists(JD + 'XComIsmsRogue.ini')
    open(JD + 'XComIsmsRogue.ini', 'wb').write(rogue.encode('ascii'))
    json.dump([list(c) for c in sorted(live1)], open(TMP + 'deck_1112.json', 'w'))
    print('APPLIED. DisableClass lines:', new.count('+DisableClass='))
else:
    print('dry run only')
