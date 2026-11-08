"""Price revival options: each option drops a set of jepFixes pairs; simulate the deck; report spec counts and side effects."""
import json, re, collections, sim
JFP = "C:/Program Files (x86)/Steam/steamapps/common/XCOM 2/XCom2-WarOfTheChosen/XComGame/Mods/jepFixes/Config/XComAmalgamation.ini"
JTXT = open(JFP, 'rb').read().decode('ascii')
LINES = JTXT.split('\r\n')
W0 = LINES.index("; jepFixes 2026-10-29, Idi's weapon slot optimization. A spec 'carries' a weapon in its own slot (primary spec: primary")
spec = {v['name'].lower(): v for v in json.load(open('specs_now.json')).values()}
slotuse = {k.split('|')[1]: v for k, v in json.load(open('slotuse.json')).items()}
G = {k: [x.lower() for x in v] for k, v in json.load(open('slotrule_out.json'))['G'].items()}
orig_files = sim.files
def run(drop):
    """drop(a, b, idx) -> True to remove that jep pair line"""
    out = []
    for i, l in enumerate(LINES):
        m = re.match(r'^\+IncompatibleSpecs=\(A="(\w+)", B="(\w+)"\)', l)
        if m and drop(m.group(1).lower(), m.group(2).lower(), i):
            continue
        out.append(l)
    txt = '\r\n'.join(out)
    def files():
        for mod, p, t in orig_files():
            yield (mod, p, txt) if 'jepfixes' in p.lower() else (mod, p, t)
    sim.files = files
    d = [x[:3] for x in sim.deck(sim.load()) if not x[3]]
    sim.files = orig_files
    return d
def cnt(d):
    c = collections.Counter()
    for p, s, t in d: c[p.lower()] += 1; c[s.lower()] += 1; c[t.lower()] += 1
    return c
base = run(lambda a, b, i: False); cb = cnt(base)
isW = lambda i: i > W0
prim = lambda n: {w for w, s in spec[n]['weapons'] if s == 'PrimaryWeapon'} - {'empty'}
sec = lambda n: {w for w, s in spec[n]['weapons'] if s == 'SecondaryWeapon'} - {'empty'}
SL = {}
st = sim.load()
for k in 'PST':
    for x in st[k]: SL[x.lower()] = k
def r3pair(a, b, who):
    """pair is an R3 hit on spec `who` (S/T listing a primary weapon the primary lacks)"""
    o = b if a == who else a
    return who in (a, b) and SL.get(o) == 'P' and SL.get(who) in 'ST' and prim(who) and not (prim(who) & prim(o))
SLOTS = {'P': [x.lower() for x in st['P']], 'S': [x.lower() for x in st['S']], 'T': [x.lower() for x in st['T']]}
RULES = [('SwP','S','SwS'),('SwS','P','SwP'),('PiP','S','PiAny'),('PiS','P','PiP'),('GaS','T','GaT'),('GaT','S','GaS'),('GrT','S','GrS'),('CaP','S','CaS'),('CaS','P','CaP'),('ShS','T','ShT'),('ShT','S','ShS')]
WFULL = {}
for g, ps, al in RULES:
    for m in G[g]:
        for y in SLOTS[ps]:
            if y not in G[al]: WFULL.setdefault(frozenset((m, y)), g)
WFULL[frozenset(('commissar',))] = 'C'
EMPTY_S = [x for x in G['SwS'][:0]] + [n for n in st['S'] if not sec(n.lower())]
EMPTY_S = [x.lower() for x in EMPTY_S]
KNIFE_S = [n.lower() for n in st['S'] if sec(n.lower()) & {'combatknife'} and not sec(n.lower()) & {'sword'}]
SHOT_P = [n.lower() for n in st['P'] if prim(n.lower()) & {'shotgun'}]
OPTS = {
 'Ravager A: sword primary may take an empty-slot secondary (tertiary fills it)': ('ravager', lambda a, b, i: isW(i) and 'ravager' in (a, b) and ({a, b} - {'ravager'}) <= set(EMPTY_S)),
 'Ravager B: Ravager exempt from W1 entirely': ('ravager', lambda a, b, i: isW(i) and 'ravager' in (a, b)),
 'Savage A: Savage may take a knife secondary (its author: "allows Combat Knife as a secondary")': ('savage', lambda a, b, i: isW(i) and 'savage' in (a, b) and ({a, b} - {'savage'}) <= set(KNIFE_S)),
 'Savage B: Savage exempt from W1 entirely': ('savage', lambda a, b, i: isW(i) and 'savage' in (a, b)),
 'Brigand A: Brigand may sit under shotgun primaries (its tree feeds the primary: 8 shotgun-slot perks)': ('brigand', lambda a, b, i: isW(i) and 'brigand' in (a, b) and ({a, b} - {'brigand'}) <= set(SHOT_P)),
 'Brigand B: Brigand exempt from W1 entirely': ('brigand', lambda a, b, i: isW(i) and 'brigand' in (a, b)),
 'SkvRaider A: Raider exempt from W1 (sword-or-knife secondary under any primary)': ('skvraider', lambda a, b, i: isW(i) and 'skvraider' in (a, b)),
 'SwordMaster A: SwordMaster may sit with sword secondaries (it carries a sword too)': ('swordmaster', lambda a, b, i: isW(i) and 'swordmaster' in (a, b) and ({a, b} - {'swordmaster'}) <= set(G['SwS'])),
 'SwordMaster B: sword primaries may take shield secondaries (sword-and-board)': ('swordmaster', lambda a, b, i: isW(i) and ({a, b} & set(G['SwP'])) and ({a, b} & set(G['ShS']))),
 'Xeno A: both Xeno Zoologists may take pistol/autopistol secondaries (author lists them)': ('xenozoologist', lambda a, b, i: isW(i) and ({a, b} & {'xenozoologist', 'xenozoologistmm'}) and ({a, b} & set(G['PiS']))),
 'Maniac A = Savage A (Maniac lives on Savage + Butterfly)': ('maniac', lambda a, b, i: isW(i) and 'savage' in (a, b) and ({a, b} - {'savage'}) <= set(KNIFE_S)),
 'Androctonus A: sniper whitelist + W2 exempt for Androctonus with pistol/autopistol secondaries': ('androctonus', lambda a, b, i: 'androctonus' in (a, b) and ({a, b} & set(G['PiS']))),
 'R3 fix: drop R3 pairs for specs whose trees never use the primary slot (AlienHunter2, DronePilot, SwordMaster, Riot, Ironclad, LegendaryWarrior)': ('dronepilot', lambda a, b, i: (not isW(i)) and frozenset((a, b)) not in WFULL and any(r3pair(a, b, w) for w in ['alienhunter2', 'dronepilot', 'swordmaster', 'riot', 'ironclad', 'legendarywarrior'])),
}
OPTS['AlienHunter2 A: R3 fix + AlienHunter2 exempt from W1'] = ('alienhunter2', lambda a, b, i: OPTS['R3 fix: drop R3 pairs for specs whose trees never use the primary slot (AlienHunter2, DronePilot, SwordMaster, Riot, Ironclad, LegendaryWarrior)'][1](a, b, i) or ('alienhunter2' in (a, b) and (isW(i) or (frozenset((a, b)) in WFULL and any(r3pair(a, b, 'alienhunter2') for _ in [0])))))
res = {}
for name, (focus, f) in OPTS.items():
    d = run(f); c = cnt(d)
    gained = {k: c[k] - cb[k] for k in c if c[k] != cb[k]}
    ex = sorted('_'.join(x) for x in set(map(tuple, d)) - set(map(tuple, base)))
    res[name] = dict(deck=len(d), delta=len(d) - len(base), gained=gained, new=ex)
    print('\n%s\n  deck %d (%+d) | spec changes %s\n  e.g. %s' % (name, len(d), len(d) - len(base), dict(sorted(gained.items(), key=lambda kv: -kv[1])[:12]), ex[:6]))
json.dump(res, open('opt_out.json', 'w'), indent=1)
print('\nbase deck', len(base), 'EMPTY_S', EMPTY_S, 'KNIFE_S', KNIFE_S, 'SHOT_P', SHOT_P)
