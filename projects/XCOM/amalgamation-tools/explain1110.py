import json, collections
TMP = "C:/Users/jep/.claude/jobs/94ad0c55/tmp/"
A = json.load(open(TMP + 'audit_1110.json'))
d10 = {'_'.join(c) for c in json.load(open(TMP + 'deck_1110.json'))}
d09 = {'_'.join(c) for c in json.load(open(TMP + 'deck_1109.json'))}
for k in ['HareVeilWalker_HareWaterVein_KeeperTertiary', 'HareVeilWalker_HareWaterVein_Cryo', 'MusaSamurai_Corsair_KeeperTertiary', 'MusaSamurai_Corsair_SkvAssassin', 'Gunfighter_Hotshot_Smoker']:
    print(k, 'IN' if k in d10 else 'out')
exec(open(TMP + 'tiers.py').read().split("rows = collections")[0].replace("deck = [x[:3] for x in sim.deck(sim.load()) if not x[3]]", "deck = []"))
rank = lambda c: 0 if tier(*c).startswith('A') else (1 if tier(*c).startswith('B') else 2)
aT = collections.Counter()
for k in d10:
    c = k.split('_') if k.count('_') == 2 else None
cards = [tuple(x) for x in json.load(open(TMP + 'deck_1110.json'))]
for c in cards:
    if rank(c) == 0:
        for i, x in enumerate(c): aT[(i, x)] += 1
tot = collections.Counter((i, x) for c in cards for i, x in enumerate(c))
pairs = [('Impaler_Ironclad_AegisDefender', 'Impaler_Vengeance2_AegisDefender', 1), ('Salamander_Rocketeer_Saboteur', 'Salamander_Bombarder_Saboteur', 1),
         ('XenoZoologist_Gunslinger_SkvScout', 'XenoZoologist_Hotshot_SkvScout', 1), ('XenoZoologistMM_Gunslinger_SkvScout', 'XenoZoologistMM_Hotshot_SkvScout', 1),
         ('Infantry_Gripsman_Blaster', 'Marauder_Gripsman_Blaster', 0), ('BountyHunter_ReconOfficer_SkvClay', 'Predator_ReconOfficer_SkvClay', 0)]
for a, b, j in pairs:
    for k in (a, b):
        alt = k.split('_')[j]
        print('  %-42s %s | dead random %d %s | %s: %d cards now, %d tier-A' % (k, 'KEPT' if k in d10 else 'cut ', A[k][1], [x[1] for x in A[k][4]], alt, tot[(j, alt)], aT[(j, alt)]))
gone = sorted(d09 - d10)
print('removed', len(gone)); print(gone)
