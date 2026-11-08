"""Idi 11-08: cut combos he would never pick (rule D4) as Amalgamation DisableClass names; verify every spec keeps >=1 card."""
import json, shutil, collections, sim
JFP = "C:/Program Files (x86)/Steam/steamapps/common/XCOM 2/XCom2-WarOfTheChosen/XComGame/Mods/jepFixes/Config/XComAmalgamation.ini"
TMP = "C:/Users/jep/.claude/jobs/94ad0c55/tmp/"
shutil.copyfile(JFP, TMP + 'XComAmalgamation.ini.bak-1108c')
deck = [tuple(x[:3]) for x in sim.deck(sim.load()) if not x[3]]
keep = {tuple(x) for x in json.load(open(TMP + 'deck_d4.json'))}
assert keep <= set(deck)
cut = sorted('_'.join(c) for c in deck if c not in keep)
txt = open(JFP, 'rb').read().decode('ascii').rstrip('\r\n')
assert '[AmalgamationClassesWOTC.X2DownloadableContentInfo_AmalgamationClassesWOTC]' not in txt
block = ['', '[AmalgamationClassesWOTC.X2DownloadableContentInfo_AmalgamationClassesWOTC]',
         "; jepFixes 2026-11-08, Idi: cut the combos he would never pick (amalgamation-card-tiers-2026-11-08.md, rule D4).",
         "; Within each primary+secondary pair only the best tertiary tier stays (A weapon stacks on / fills the secondary slot >",
         "; B utility > C passive/healing). A pair that only offers passive/healing tertiaries keeps one card: passive before healer",
         "; (R8), rarest tertiary first. Every spec keeps >=1 card. %d classes cut, %d stay. Built from the 11-08 deck: a mod" % (len(cut), len(keep)),
         "; change needs a regenerate (amalgamation-tools/cuts.py + applycut.py); a stale name only logs 'No class template'."]
block += ['+DisableClass="%s"' % n for n in cut]
open(JFP, 'wb').write((txt + '\r\n' + '\r\n'.join(block) + '\r\n').encode('ascii'))
st = sim.load(); d = sim.deck(st)
live = [x[:3] for x in d if not x[3]]
n = collections.Counter()
for p, s, t in live: n[p] += 1; n[s] += 1; n[t] += 1
print('cut', len(cut), '| live deck', len(live), '| equals D4:', set(map(tuple, live)) == keep,
      '| specs at 0:', [x for x in st['P'] + st['S'] + st['T'] if n[x] == 0], '| DisableClass total', len(st['dis']))
