"""Re-run only the selection + cut (releases already applied), with a floor: every spec keeps >= FLOOR working cards."""
import json, re, shutil, collections, sim
TMP = "C:/Users/jep/.claude/jobs/94ad0c55/tmp/"
JF = "C:/Program Files (x86)/Steam/steamapps/common/XCOM 2/XCom2-WarOfTheChosen/XComGame/Mods/jepFixes/Config/XComAmalgamation.ini"
FLOOR = 3
shutil.copyfile(JF, TMP + 'XComAmalgamation.ini.bak-1109d')
lines = open(JF, 'rb').read().decode('ascii').split('\r\n')
out, skip = [], False
for l in lines:
    if l.startswith("; jepFixes 2026-11-09, cut (replaces the 11-08 D4 list)"): skip = True; continue
    if skip and (l.startswith(';') or l.startswith('+DisableClass=')): continue
    skip = False; out.append(l)
while out and out[-1] == '': out.pop()
open(JF, 'wb').write(('\r\n'.join(out) + '\r\n').encode('ascii'))
exec(open(TMP + 'audit.py').read().split("if __name__")[0])
exec(open(TMP + 'tiers.py').read().split("deck = ")[1].split("rows = collections")[0].split("\n", 1)[1].replace("spec[n.lower()]", "SPEC[n.lower()]"))
st = sim.load()
built = [tuple(x[:3]) for x in sim.deck(st)]
aud = {c: audit(c) for c in built}
work = [c for c in built if aud[c][0][0] == 0]
rank = lambda c: (lambda k: 0 if k.startswith('A') else (1 if k.startswith('B') else 2))(tier(*c))
tcount = collections.Counter(c[2] for c in work)
byPS = collections.defaultdict(list)
for c in work: byPS[(c[0], c[1])].append(c)
keep = set()
for ps, cs in byPS.items():
    best = min(rank(c) for c in cs)
    top = [c for c in cs if rank(c) == best]
    if best < 2: keep |= set(top)
    else: keep.add(sorted(top, key=lambda c: (0 if tier(*c).startswith('C1') else 1, aud[c][0][1], tcount[c[2]]))[0])
added = []
for i, sl in enumerate(('P', 'S', 'T')):
    for x in st[sl]:
        have = sum(1 for c in keep if c[i] == x)
        if have >= FLOOR: continue
        cand = sorted((c for c in work if c[i] == x and c not in keep), key=lambda c: (aud[c][0][1], rank(c), c))
        for c in cand[:FLOOR - have]: keep.add(c); added.append('_'.join(c))
cut = sorted('_'.join(c) for c in built if c not in keep)
blk = ['', "; jepFixes 2026-11-09, cut (replaces the 11-08 D4 list): a card stays only if no guaranteed perk dies in tactical (perk audit",
       "; of Ability To Slot Reassignment + Musashi's Mods Fixes + Amalgamation AbilityRestrictions over the best loadout) and it holds",
       "; the best tertiary tier its primary+secondary pair offers (A weapon > B utility > C passive/healing); a filler-only pair keeps",
       "; one card; every spec keeps >= %d working cards. %d cut, %d stay. Regenerate after any mod change (pipeline.py, select2.py)." % (FLOOR, len(cut), len(keep))]
blk += ['+DisableClass="%s"' % n for n in cut]
txt = open(JF, 'rb').read().decode('ascii').rstrip('\r\n')
assert txt.rindex('[') == txt.index('[AmalgamationClassesWOTC.X2DownloadableContentInfo_AmalgamationClassesWOTC]')
open(JF, 'wb').write((txt + '\r\n' + '\r\n'.join(blk) + '\r\n').encode('ascii'))
st2 = sim.load(); live = [tuple(x[:3]) for x in sim.deck(st2) if not x[3]]
n = collections.Counter()
for p, s, t in live: n[p] += 1; n[s] += 1; n[t] += 1
print('floor added', len(added), added[:12])
print('deck', len(live), '| equals selection:', set(live) == keep, '| broken in deck:', sum(1 for c in live if aud[c][0][0]))
print('specs at 0:', [x for x in st2['P'] + st2['S'] + st2['T'] if n[x] == 0], '| specs under 3:', sorted((n[x], x) for x in st2['P'] + st2['S'] + st2['T'] if n[x] < 3))
tc = collections.Counter(rank(c) for c in live); print('tiers A/B/C', tc[0], tc[1], tc[2], '| DisableClass total', len(st2['dis']))
json.dump([list(c) for c in live], open(TMP + 'deck_1109.json', 'w'))
json.dump({'_'.join(c): [v[0][0], v[0][1], v[1], v[2], [[d[0], d[1], d[2], d[3]] for d in v[3]]] for c, v in aud.items()}, open(TMP + 'audit_1109.json', 'w'))
