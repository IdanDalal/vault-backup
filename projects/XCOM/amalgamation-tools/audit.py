"""Ground-truth perk audit. A perk dies in tactical if
 M1 Ability To Slot Reassignment (AbilityToSlotReassignmentLib.uc:164-255): it has an AbilityWeaponCategories entry and
    no inventory item matches its set (sets: first definition by name wins, Find at :307), or
 M2 Amalgamation AbilityRestrictions (X2DownloadableContentInfo_AmalgamationClassesWOTC.uc:285-340): it has entries and
    the weapon in none of the named slots has the named category.
Per card: try every loadout (one primary cat x one secondary cat from the class's allowed weapons, GetClassWeapons merges
P+S+T + ExtraAllowedWeapons) and keep the loadout that leaves the fewest dead perks."""
import json, re, glob, os, collections, itertools, sim
AML = json.load(open(r'C:/XCOM2 AML 1.6.0-beta/settings.json', encoding='utf-8-sig'))
act = [x for c in AML['Mods']['Entries'].values() for x in c['Entries'] if x.get('isActive')]
order = {p.rstrip('\\/').lower(): i for i, p in enumerate(AML['ModPaths'])}
def key(x):
    path = x['Path'].replace('/', '\\')
    parent, folder = os.path.split(path.rstrip('\\'))
    return (order.get(parent.lower(), 99), folder.lower())
act.sort(key=key)
def lines_of(fname):
    for x in act:
        for p in sorted(glob.glob(x['Path'] + '/Config/**/' + fname, recursive=True)):
            sec = ''
            for l in sim.logical_lines(sim.rd(p)):
                s = l.strip()
                m = re.match(r'^\[([^\]]+)\]', s)
                if m: sec = m.group(1).strip().lower(); continue
                yield x['Name'], sec, s
# M1 tables
SETS, AWC = [], []
for mod, sec, s in lines_of('XComAbilityToSlotReassignment.ini'):
    if sec != 'abilitytoslotreassignment.abilitytoslotreassignmentlib': continue
    m = re.match(r'^([+\-]?)WeaponCategorySets\s*=\s*\(\s*WeaponCategorySetName\s*=\s*"?(\w+)"?\s*,\s*WeaponCategories\s*=\s*\(([^)]*)\)', s, re.I)
    if m:
        item = (m.group(2).lower(), tuple(c.strip().strip('"').lower() for c in m.group(3).split(',') if c.strip()))
        if m.group(1) == '-':
            if item in SETS: SETS.remove(item)
        else: SETS.append(item)
        continue
    m = re.match(r'^([+\-]?)AbilityWeaponCategories\s*=\s*\(\s*AbilityName\s*=\s*"?(\w+)"?\s*,\s*WeaponCategorySetName\s*=\s*"?(\w+)"?', s, re.I)
    if m:
        item = (m.group(2).lower(), m.group(3).lower())
        if m.group(1) == '-':
            if item in AWC: AWC.remove(item)
        else: AWC.append(item)
# Musashi's Mods Fixes 2569592723 (X2DLCInfo_WOTCMusashiModFixes.uc:341-536): default-entry fixes, then same-name
# sets are unioned and an ability listed under several sets gets the union of all of them.
FIX = {('longwatch', 'siperrifles'): 'precisionrifles', ('rapidfire', 'rifles'): 'allmainweapons',
       ('sharpshooteraim', 'precisionrifles'): 'allmainweapons', ('inthezone', 'precisionrifles'): 'allmainweapons',
       ('demolition', 'cannon'): 'allmainweapons'}
AWC = [(a, FIX.get((a, n), n)) for a, n in AWC]
setmap = collections.defaultdict(set)
for n, cats in SETS: setmap[n] |= {('psionicreaper' if c == 'psionicrepeater' else c) for c in cats}
abl_sets = collections.defaultdict(set)
for a, n in AWC: abl_sets[a].add(n)
M1 = {a: set().union(*(setmap.get(n, set()) for n in ns)) for a, ns in abl_sets.items()}
abl_set = {a: '+'.join(sorted(ns)) for a, ns in abl_sets.items()}
# M2 + specs/abilities from Amalgamation configs
M2 = collections.defaultdict(list); EXTRA = collections.defaultdict(list)
for mod, sec, s in lines_of('XComAmalgamation.ini'):
    if sec == sim.SEC_DLC:
        m = re.match(r'^\+AbilityRestrictions\s*=\s*\(\s*AbilityName\s*=\s*"?(\w+)"?\s*,\s*WeaponCat\s*=\s*"?(\w+)"?\s*,\s*InvSlot\s*=\s*eInvSlot_(\w+)', s, re.I)
        if m: M2[m.group(1).lower()].append((m.group(3), m.group(2).lower()))
    if sec == sim.SEC_CLS:
        m = re.match(r'^\+ExtraAllowedWeapons\s*=\s*\(\s*SpecName\s*=\s*"?(\w+)"?\s*,\s*Weapon\s*=\s*\(\s*WeaponType\s*=\s*"?(\w+)"?\s*,\s*SlotType\s*=\s*eInvSlot_(\w+)', s, re.I)
        if m: EXTRA[m.group(1).lower()].append((m.group(2).lower(), m.group(3)))
T_ = '\n'.join(sim.rd(p) for x in act for p in glob.glob(x['Path'] + '/Config/**/XComAmalgamation.ini', recursive=True))
decks = {}
for m in re.finditer(r'\+AbilityDecks\s*=\s*\(\s*DeckName\s*=\s*"([^"]+)"(.*?)(?=^\s*\+\w+\s*=|^\s*\[\w|\Z)', T_, re.M | re.S):
    decks.setdefault(m.group(1).lower(), m.group(2))
data = {}
for m in re.finditer(r'\+SpecDataset\s*=\s*\(\s*Spec\s*=\s*"([^"]+)"(.*?)(?=^\s*\+\w+\s*=|^\s*\[\w|\Z)', T_, re.M | re.S):
    data.setdefault(m.group(1).lower(), m.group(2))
def tree(spec):
    body = data.get(spec.lower(), '')
    ranks = re.split(r'Ranks\[\d+\]', body)[1:]
    out = []  # (ability, rank, fixed?)
    for r, rb in enumerate(ranks):
        for a in re.findall(r'Skill\s*=\s*\(\s*AbilityName\s*=\s*"([^"]+)"', rb):
            out.append((a.lower(), r, True))
        for dname in re.findall(r'Deck\s*=\s*"([^"]+)"', rb):
            for a in re.findall(r'AbilityName\s*=\s*"([^"]+)"', decks.get(dname.lower(), '')):
                out.append((a.lower(), r, False))
    seen, res = set(), []
    for a, r, f in out:
        if (a, f) not in seen: seen.add((a, f)); res.append((a, r, f))
    return res
SPEC = {v['name'].lower(): v for v in json.load(open('specs_now.json')).values()}
def class_cats(c):
    cats = {'PrimaryWeapon': set(), 'SecondaryWeapon': set()}
    for x in c:
        for w, sl in SPEC[x.lower()]['weapons'] + EXTRA.get(x.lower(), []):
            if sl in cats: cats[sl].add(w)
    return cats
def alive(a, pcat, scat):
    inv = {pcat, scat} - {None, 'empty'}
    if a in M1 and M1[a] and not (M1[a] & inv): return False
    if a in M2:
        slot = {'PrimaryWeapon': pcat, 'SecondaryWeapon': scat}
        if not any(slot.get(sl) == cat for sl, cat in M2[a]): return False
    return True
TREES = {}
def audit(c):
    cats = class_cats(c)
    P = sorted(cats['PrimaryWeapon']) or [None]; S = sorted(cats['SecondaryWeapon'] | {'empty'}) or [None]
    trees = [TREES.setdefault(x, tree(x)) for x in c]
    best = None
    for pc, sc in itertools.product(P, S):
        dead = [(c[i], a, r, f) for i, t in enumerate(trees) for a, r, f in t if not alive(a, pc, sc)]
        score = (sum(1 for d in dead if d[3]), len(dead))
        if best is None or score < best[0]: best = (score, pc, sc, dead)
    return best
if __name__ == '__main__':
    print('M1 sets', len(setmap), '| M1 abilities', len(M1), '| M2 abilities', len(M2), '| specs with trees', sum(1 for k in SPEC if data.get(k)))
    for c in [('HareCaptain', 'HareSwash', 'HareSootsman'), ('Marathonist', 'AlienHunter2', 'Sentinel'), ('Desolator', 'Phoenix', 'TechMedic'),
              ('MusaSamurai', 'NinjaWarrior', 'CombatEngineer'), ('MusaSamurai', 'NinjaWarrior', 'SkvAssassin')]:
        (fx, tot), pc, sc, dead = audit(c)
        print('%-45s best loadout %s + %s | dead fixed %d, dead total %d %s' % ('_'.join(c), pc, sc, fx, tot, [(d[0], d[1], 'squaddie' if d[2] == 0 else 'rank%d' % d[2], 'fixed' if d[3] else 'deck') for d in dead][:6]))
