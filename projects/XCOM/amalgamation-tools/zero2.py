"""Per zero spec: author-approved combos (no author pair) and which jep rule blocks kill them."""
import json, re, collections, itertools, sim
ZERO = ['Ravager', 'Savage', 'Brigand', 'SkvRaider', 'SwordMaster', 'XenoZoologist', 'XenoZoologistMM', 'Maniac',
        'Androctonus', 'AlienHunter2', 'DronePilot']
JFP = "C:/Program Files (x86)/Steam/steamapps/common/XCOM 2/XCom2-WarOfTheChosen/XComGame/Mods/jepFixes/Config/XComAmalgamation.ini"
lines = open(JFP, 'rb').read().decode('ascii').split('\r\n')
# rule block by comment headers
BLOCKS = [(1, 'R1-R5 09-16 (R1 no weapon S x no weapon T, R2 two secondary weapons, R3 foreign primary weapon, R4 same squaddie skill)'),
          (723, 'R6 09-16 overwatch spec on no-firearm primary'),
          (734, '09-17/18 displayed-weapon rules (R2d two displayed secondary weapons, R2p dual-wield, R5 locked perks, R7 Commissar)'),
          (820, '09-28 sniper whitelist (gremlin/GL/psi/bio/BIT only)'),
          (1229, '09-28 audit DronePilot x Interceptor'),
          (1232, '10-29 weapon slot rules W1-W6 + Commissar')]
def block_of(i):
    b = None
    for start, name in BLOCKS:
        if i + 1 >= start: b = name
    return b
jep = collections.defaultdict(set)
for i, l in enumerate(lines):
    m = re.match(r'^\+IncompatibleSpecs=\(A="(\w+)", B="(\w+)"\)', l)
    if m:
        jep[frozenset((m.group(1).lower(), m.group(2).lower()))].add(block_of(i))
st = sim.load()
P, S, T = st['P'], st['S'], st['T']
slot_of = {x.lower(): 'P' for x in P}; slot_of.update({x.lower(): 'S' for x in S}); slot_of.update({x.lower(): 'T' for x in T})
auth = set()
for a, b, mod in st['inc']:
    if mod != 'jepFixes': auth.add(frozenset((a, b)))
def pairs(c):
    t = [x.lower() for x in c]
    return [frozenset(p) for p in itertools.combinations(t, 2)] + [frozenset((x,)) for x in t]
before = {tuple(x) for x in json.load(open('deck_before.json'))}
res = {}
for z in ZERO:
    sl = slot_of[z.lower()]
    combos = [(p, s, t) for p in ([z] if sl == 'P' else P) for s in ([z] if sl == 'S' else S) for t in ([z] if sl == 'T' else T)]
    appr = [c for c in combos if not any(p in auth for p in pairs(c))]
    killers = collections.Counter(); only = collections.defaultdict(list)
    for c in appr:
        bl = set()
        for p in pairs(c):
            bl |= jep.get(p, set())
        key = ' + '.join(sorted(b[:12] for b in bl))
        only[key].append('_'.join(c))
    partners = collections.Counter()
    for c in appr:
        for x in c:
            if x != z: partners[(slot_of[x.lower()], x)] += 1
    res[z] = dict(slot=sl, approved=len(appr), before=sorted('_'.join(c) for c in before if z in c),
                  by_killer={k: (len(v), v[:6]) for k, v in sorted(only.items(), key=lambda kv: -len(kv[1]))},
                  approved_partners=sorted(f'{s}:{x}' for (s, x) in partners))
json.dump(res, open('zero2_out.json', 'w'), indent=1)
for z, r in res.items():
    print('\n#', z, r['slot'], '| author-approved combos', r['approved'], '| in deck before 10-29:', len(r['before']), r['before'][:8])
    print('  approved partners:', ', '.join(r['approved_partners'])[:600])
    for k, (n, ex) in list(r['by_killer'].items())[:6]:
        print('   killed by [%s]: %d  e.g. %s' % (k, n, ex[:3]))
