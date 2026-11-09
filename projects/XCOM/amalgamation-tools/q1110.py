import json, collections, sim
exec(open('audit.py').read().split("if __name__")[0])
# 1 SwordMaster card: every loadout
c = ('Marauder', 'Vengeance2', 'SwordMaster')
cats = class_cats(c); print('class weapons', {k: sorted(v) for k, v in cats.items()})
for pc in sorted(cats['PrimaryWeapon']):
    for sc in sorted(cats['SecondaryWeapon']):
        dead = [(x, a, r, f) for x in c for a, r, f in tree(x) if not alive(a, pc, sc)]
        print('  %s + %s: dead guaranteed %s | dead random %s' % (pc, sc, [d[1] for d in dead if d[3]], [d[1] for d in dead if not d[3]]))
print('SwordMaster tree:', [(a, r, 'fixed' if f else 'roll', sorted(M1.get(a, set()))[:5], M2.get(a)) for a, r, f in tree('SwordMaster')][:20])
# 3 Raider with knife vs sword
for sc in ('sword', 'combatknife'):
    dead = [a for a, r, f in tree('SkvRaider') if not alive(a, 'rifle', sc)]
    print('Raider tree with rifle +', sc, '-> dead:', dead)
print('Raider perks needing weapons:', [(a, 'fixed' if f else 'roll', sorted(M1.get(a, set()) & {'sword', 'combatknife', 'pistol', 'sidearm'}), M2.get(a)) for a, r, f in tree('SkvRaider') if a in M1 or a in M2])
# 2 identical starting perks in the live deck
sq = {x: {a for a, r, f in tree(x) if r == 0 and f} for x in set(sim.load()['P'] + sim.load()['S'] + sim.load()['T'])}
live = [tuple(x[:3]) for x in sim.deck(sim.load()) if not x[3]]
dup = [(c, sorted((sq[c[0]] & sq[c[1]]) | (sq[c[0]] & sq[c[2]]) | (sq[c[1]] & sq[c[2]]))) for c in live]
dup = [d for d in dup if d[1]]
print('live cards with an identical starting perk:', len(dup), 'of', len(live))
print('by perk:', collections.Counter(p for _, ps in dup for p in ps).most_common(10))
json.dump({'sq': {k: sorted(v) for k, v in sq.items()}}, open('squaddie.json', 'w'))
