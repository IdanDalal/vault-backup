"""1109 pipeline: releases (upgrades_out + Swash), rebuild, perk audit, select, rewrite the DisableClass cut, floor check."""
import json, re, shutil, collections, itertools, sim
TMP = "C:/Users/jep/.claude/jobs/94ad0c55/tmp/"
JF = "C:/Program Files (x86)/Steam/steamapps/common/XCOM 2/XCom2-WarOfTheChosen/XComGame/Mods/jepFixes/Config/XComAmalgamation.ini"
shutil.copyfile(JF, TMP + 'XComAmalgamation.ini.bak-1109c')
up = json.load(open(TMP + 'upgrades_out.json'))
rel = {frozenset(x[1]) for x in up}
SWASH = {frozenset(('hareswash', p)) for p in ('fusilier', 'harequartermaster', 'pistoleer')}
lines = open(JF, 'rb').read().decode('ascii').split('\r\n')
# 1. delete jep pair lines for released pairs (+ Swash), and the old D4 DisableClass block
out, dropped_jep, in_d4 = [], 0, False
for l in lines:
    if l.startswith("; jepFixes 2026-11-08, Idi: cut the combos he would never pick"):
        in_d4 = True; continue
    if in_d4:
        if l.startswith(';') or l.startswith('+DisableClass='): continue
        in_d4 = False
    m = re.match(r'^\+IncompatibleSpecs=\(A="(\w+)", B="(\w+)"\)', l)
    if m and frozenset((m.group(1).lower(), m.group(2).lower())) in (rel | SWASH):
        dropped_jep += 1; continue
    out.append(l)
# 2. author releases: byte copies of every author + line for released pairs, inserted before the PexmBridge block
minus = []
for mod, p, t in sim.files():
    if 'jepfixes' in p.lower(): continue
    sec = ''
    for l in t.splitlines():
        m = re.match(r'^\s*\[([^\]]+)\]', l)
        if m: sec = m.group(1).strip().lower(); continue
        if sec != sim.SEC_CLS or not l.lstrip().startswith('+IncompatibleSpecs'): continue
        mm = re.search(r'A\s*=\s*"?(\w+)"?\s*,\s*B\s*=\s*"?(\w+)"?', l)
        if mm and frozenset((mm.group(1).lower(), mm.group(2).lower())) in rel:
            minus.append('-' + l.lstrip()[1:])
ins = out.index('[AmalgamationPexmBridge.X2DownloadableContentInfo_AmalgamationPexmBridge]')
while out[ins - 1].startswith(';'): ins -= 1
block = ['', "; jepFixes 2026-11-09 (perk audit, Idi's Samurai/Ninja/Assassin report): released %d author bans that were the only" % len(minus),
         "; block on a WORKING tier-A card (tertiary weapon stacks on / fills the secondary slot; 0 dead guaranteed perks, <=1 dead",
         "; random-roll perk) for a primary+secondary pair that had no tier-A card. Byte copies of the author lines. Swash exempt",
         "; from W1/W2 under pistol primaries (Fusilier, Quartermaster, Pistoleer): its squaddie Buckle Your Swash needs a pistol.",
         "; %d jep pair lines deleted for the same reasons. Tools: audit.py, upgrades.py, pipeline.py." % dropped_jep] + minus + ['']
out = out[:ins] + block + out[ins:]
while out and out[-1] == '': out.pop()
open(JF, 'wb').write(('\r\n'.join(out) + '\r\n').encode('ascii'))
# 3. rebuild + audit
exec(open(TMP + 'audit.py').read().split("if __name__")[0])
st = sim.load()
built = [tuple(x[:3]) for x in sim.deck(st)]
aud = {}
for c in built:
    (fx, tot), pc, sc, dead = audit(c)
    aud[c] = (fx, tot, pc, sc)
work = [c for c in built if aud[c][0] == 0]
# 4. select: best tier per P+S among working cards; filler-only pair keeps one (passive before healer, fewest dead, rarest)
DEV = None
exec(open(TMP + 'tiers.py').read().split("deck = ")[1].split("rows = collections")[0].split("\n", 1)[1].replace("spec[n.lower()]", "SPEC[n.lower()]"))
rank = lambda c: (lambda k: 0 if k.startswith('A') else (1 if k.startswith('B') else 2))(tier(*c))
tcount = collections.Counter(c[2] for c in work)
byPS = collections.defaultdict(list)
for c in work: byPS[(c[0], c[1])].append(c)
keep = []
for ps, cs in byPS.items():
    best = min(rank(c) for c in cs)
    top = [c for c in cs if rank(c) == best]
    if best < 2: keep += top
    else: keep.append(sorted(top, key=lambda c: (0 if tier(*c).startswith('C1') else 1, aud[c][1], tcount[c[2]]))[0])
cut = sorted('_'.join(c) for c in built if c not in set(keep))
txt = open(JF, 'rb').read().decode('ascii').rstrip('\r\n')
assert txt.rindex('[') == txt.index('[AmalgamationClassesWOTC.X2DownloadableContentInfo_AmalgamationClassesWOTC]')
blk = ['', "; jepFixes 2026-11-09, cut (replaces the 11-08 D4 list): a card stays only if no guaranteed perk dies in tactical (perk audit",
       "; of Ability To Slot Reassignment + Musashi's Mods Fixes + Amalgamation AbilityRestrictions over the best loadout) and it holds",
       "; the best tertiary tier its primary+secondary pair offers (A weapon > B utility > C passive/healing); a filler-only pair keeps",
       "; one card. %d cut, %d stay. Regenerate after any mod change (pipeline.py)." % (len(cut), len(keep))]
blk += ['+DisableClass="%s"' % n for n in cut]
open(JF, 'wb').write((txt + '\r\n' + '\r\n'.join(blk) + '\r\n').encode('ascii'))
# 5. verify
st2 = sim.load(); live = [tuple(x[:3]) for x in sim.deck(st2) if not x[3]]
n = collections.Counter()
for p, s, t in live: n[p] += 1; n[s] += 1; n[t] += 1
print('author minus lines', len(minus), '| jep lines deleted', dropped_jep)
print('built', len(built), '| working', len(work), '| deck', len(live), '| equals selection:', set(live) == set(keep))
print('broken in deck:', [c for c in live if aud.get(c, (1,))[0]])
print('specs at 0:', [x for x in st2['P'] + st2['S'] + st2['T'] if n[x] == 0])
tc = collections.Counter(rank(c) for c in live); print('tiers A/B/C', tc[0], tc[1], tc[2])
json.dump([list(c) for c in live], open(TMP + 'deck_1109.json', 'w'))
json.dump({'_'.join(c): list(v) for c, v in aud.items()}, open(TMP + 'audit_1109.json', 'w'))
