"""For every spec with 0 cards: design intent (mod description, weapons, abilities) and the block chain, plus revival counts."""
import json, re, glob, collections, itertools, sim
ZERO = ['Ravager', 'Savage', 'Brigand', 'SkvRaider', 'SwordMaster', 'XenoZoologist', 'XenoZoologistMM', 'Maniac',
        'Androctonus', 'AlienHunter2', 'DronePilot']
d = json.load(open(r'C:/XCOM2 AML 1.6.0-beta/settings.json', encoding='utf-8-sig'))
mods = {x['Name']: x for c in d['Mods']['Entries'].values() for x in c['Entries']}
spec = {v['name'].lower(): v for v in json.load(open('specs_now.json')).values()}
st = sim.load()
P, S, T = st['P'], st['S'], st['T']
slot_of = {x.lower(): 'P' for x in P}; slot_of.update({x.lower(): 'S' for x in S}); slot_of.update({x.lower(): 'T' for x in T})
# owner of each pair: W (jep 10-29 block), JEP (older jep), author mod
JF = open("C:/Program Files (x86)/Steam/steamapps/common/XCOM 2/XCom2-WarOfTheChosen/XComGame/Mods/jepFixes/Config/XComAmalgamation.ini", 'rb').read().decode('ascii')
w_start = JF.index("; jepFixes 2026-10-29")
wpairs = {frozenset(x.lower() for x in m) for m in re.findall(r'^\+IncompatibleSpecs=\(A="(\w+)", B="(\w+)"\)', JF[w_start:], re.M)}
own = collections.defaultdict(set)
for a, b, mod in st['inc']:
    pr = frozenset((a, b))
    own[pr].add('W' if (mod == 'jepFixes' and pr in wpairs) else ('JEP' if mod == 'jepFixes' else mod))
def blockers(tri):
    t = [x.lower() for x in tri]
    out = []
    for x, y in itertools.combinations_with_replacement(t, 2):
        pr = frozenset((x, y))
        if pr in own and (x != y or len(pr) == 1):
            out.append((tuple(sorted(pr)), sorted(own[pr])))
    return out
# ability names -> friendly names from every active .int
act = [x for x in mods.values() if x.get('isActive')]
fname = {}
for x in act:
    for p in glob.glob(x['Path'] + '/Localization/*.int'):
        t = sim.rd(p); cur = None
        for l in t.splitlines():
            m = re.match(r'^\[(\w+) X2AbilityTemplate\]', l)
            if m: cur = m.group(1).lower(); continue
            if l.startswith('['): cur = None; continue
            m = re.match(r'^LocFriendlyName\s*=\s*"?([^"]*)', l)
            if cur and m and cur not in fname: fname[cur] = m.group(1).strip()
T_ = '\n'.join(sim.rd(p) for x in act for p in glob.glob(x['Path'] + '/Config/**/XComAmalgamation.ini', recursive=True))
decks = {m.group(1).lower(): m.group(2) for m in re.finditer(r'\+AbilityDecks\s*=\s*\(\s*DeckName\s*=\s*"([^"]+)"(.*?)(?=^\s*\+\w+\s*=|^\s*\[\w|\Z)', T_, re.M | re.S)}
data = {}
for m in re.finditer(r'\+SpecDataset\s*=\s*\(\s*Spec\s*=\s*"([^"]+)"(.*?)(?=^\s*\+\w+\s*=|^\s*\[\w|\Z)', T_, re.M | re.S):
    data.setdefault(m.group(1).lower(), m.group(2))
def abilities(n):
    body = data.get(n.lower(), '')
    ds = re.findall(r'Deck\s*=\s*"([^"]+)"', body)
    names = re.findall(r'AbilityName\s*=\s*"([^"]+)"', body + ''.join(decks.get(x.lower(), '') for x in dict.fromkeys(ds)))
    return [fname.get(a.lower(), a) for a in dict.fromkeys(names)]
out = {}
for z in ZERO:
    zl = z.lower(); sl = slot_of[zl]; v = spec[zl]; m = mods.get(v['mod'], {})
    combos = [(p, s_, t) for p in ([z] if sl == 'P' else P) for s_ in ([z] if sl == 'S' else S) for t in ([z] if sl == 'T' else T)]
    rows = [(c, blockers(c)) for c in combos]
    only_w = [c for c, b in rows if b and all(o == ['W'] for _, o in b)]
    one = [(c, b) for c, b in rows if len(b) == 1]
    cnt = collections.Counter()
    for c, b in rows:
        for pr, o in b:
            if zl in pr: cnt[(pr, '/'.join(x if x in ('W', 'JEP') else x[:30] for x in o))] += 1
    partners = collections.Counter()
    for (pr, o), n in cnt.items():
        partners[o] += 1
    out[z] = dict(slot=sl, mod=v['mod'], wid=v['wid'], weapons=v['weapons'],
                  desc=re.sub(r'\[/?[a-z0-9=*]+[^\]]*\]', '', (m.get('Description') or ''))[:1500],
                  abilities=abilities(z), combos=len(combos), revive_if_W_exempt=len(only_w),
                  one_block_away=[('_'.join(c), b[0][0], b[0][1]) for c, b in one][:40],
                  own_pairs_by_owner={k: v for k, v in partners.items()})
json.dump(out, open('zero_out.json', 'w'), indent=1)
for z, o in out.items():
    print('\n#', z, o['slot'], '|', o['mod'], o['wid'], '|', o['weapons'])
    print('  combos', o['combos'], '| revive if exempt from W rules:', o['revive_if_W_exempt'], '| one block away:', len(o['one_block_away']))
    print('  own pairs by owner:', o['own_pairs_by_owner'])
    for r in o['one_block_away'][:8]: print('   ', r)
