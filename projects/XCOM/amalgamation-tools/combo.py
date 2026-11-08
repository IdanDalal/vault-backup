exec(open('opt.py').read().split("res = {}")[0])
REC = ['Ravager A: sword primary may take an empty-slot secondary (tertiary fills it)',
 'Savage A: Savage may take a knife secondary (its author: "allows Combat Knife as a secondary")',
 'Brigand A: Brigand may sit under shotgun primaries (its tree feeds the primary: 8 shotgun-slot perks)',
 'SkvRaider A: Raider exempt from W1 (sword-or-knife secondary under any primary)',
 'SwordMaster A: SwordMaster may sit with sword secondaries (it carries a sword too)',
 'SwordMaster B: sword primaries may take shield secondaries (sword-and-board)',
 'Xeno A: both Xeno Zoologists may take pistol/autopistol secondaries (author lists them)',
 'Androctonus A: sniper whitelist + W2 exempt for Androctonus with pistol/autopistol secondaries',
 'AlienHunter2 A: R3 fix + AlienHunter2 exempt from W1']
sm = lambda a, b, i: OPTS[REC[4]][1](a, b, i) or OPTS[REC[5]][1](a, b, i)
d = run(sm); c = cnt(d); print('SwordMaster A+B: deck', len(d), 'swordmaster', c['swordmaster'])
allf = lambda a, b, i: any(OPTS[r][1](a, b, i) for r in REC)
d = run(allf); c = cnt(d)
print('ALL REC: deck', len(d), '(%+d)' % (len(d) - len(base)))
zero = [x for x in SLOTS['P'] + SLOTS['S'] + SLOTS['T'] if c[x] == 0]
print('specs at 0:', zero)
low = sorted((c[x], x) for x in SLOTS['P'] + SLOTS['S'] + SLOTS['T'] if 0 < c[x] <= 3)
print('specs at 1-3:', low)
json.dump([list(x) for x in d], open('deck_rec.json', 'w'))
