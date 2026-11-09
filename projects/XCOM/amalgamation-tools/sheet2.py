"""Idi's alt-tab pick sheet for Choose My Class, from the live (cut) deck, in in-game names."""
import json, collections, sim
exec(open('tiers.py').read().split("rows = collections")[0])
N = json.load(open('names.json'))
n = lambda x: N.get(x, x)
card = lambda c: '%s - %s - %s' % (n(c[0]), n(c[1]), n(c[2]))
AUD = json.load(open('audit_1110b.json'))
WN = {'combatknife': 'combat knife', 'sniper_rifle': 'sniper rifle', 'vektor_rifle': 'vektor rifle', 'grenade_launcher': 'grenade launcher', 'sidearm': 'autopistol', 'psiamp': 'psi amp', 'sparkbit': 'BIT', 'hunterrifle': 'hunter rifle', 'supercomputer': 'super computer', 'lw_gauntlet': 'gauntlet', 'empty': 'empty slot', 'sawedoffshotgun': 'sawed-off', 'arcthrower': 'arc thrower', 'iri_rocket_launcher': 'rocket launcher'}
wn = lambda w: WN.get(w, w) if w else 'none'
equip = lambda c: '%s + %s' % (wn(AUD['_'.join(c)][2]) + (' (canister in its own slot)' if AUD['_'.join(c)][2] == 'chemthrower' else ''), wn(AUD['_'.join(c)][3]))
LIE = []
for v in json.load(open('specs_now.json')).values():
    if v['slot'] != 'Primary' and v['weapons'] and v['weapons'][0][1] == 'PrimaryWeapon' and v['name'] in {x for c in deck for x in c}:
        own = [w for w, sl in v['weapons'] if sl == 'SecondaryWeapon']
        LIE.append('%s (label says %s; it carries %s in the secondary slot)' % (n(v['name']), wn(v['weapons'][0][0]), ' or '.join(wn(w) for w in own) or 'nothing'))
LIE.append('Raider (label says sword; a combat knife keeps every perk, a sword loses Slash and Dash)')
LIE = [x for x in LIE if not x.startswith('Phoenix')] + ['Phoenix (label says chemthrower; its canister rides in the chemthrower\'s own canister slot, so the secondary slot takes the tertiary\'s weapon)']
cnt = collections.Counter()
for p, s, t in deck: cnt[('Primary', p)] += 1; cnt[('Secondary', s)] += 1; cnt[('Tertiary', t)] += 1
rare = sorted((k for k in cnt if cnt[k] <= 2), key=lambda k: (cnt[k], k[0], n(k[1])))
seen = collections.OrderedDict()
for sl, x in rare:
    for c in deck:
        if x in c and ((sl == 'Primary' and c[0] == x) or (sl == 'Secondary' and c[1] == x) or (sl == 'Tertiary' and c[2] == x)):
            seen.setdefault(c, []).append('%s %s (%d card%s)' % (n(x), sl.lower(), cnt[(sl, x)], '' if cnt[(sl, x)] == 1 else 's'))
tierT = collections.defaultdict(set)
for p, s, t in deck: tierT[tier(p, s, t)[:2]].add(t)
A = sorted({n(t) for k, v in tierT.items() if k.startswith('A') for t in v})
B = sorted({n(t) for k, v in tierT.items() if k.startswith('B') for t in v})
C1 = sorted({n(t) for t in tierT.get('C1', ())}); C2 = sorted({n(t) for t in tierT.get('C2', ())})
L = ['---', 'type: reference', 'created: 2026-11-09', 'author: jep', '---',
     '# Pick sheet: Choose My Class (100 offers)', '',
     'Card = Primary - Secondary - Tertiary. %d cards left in the game. Every one has all its guaranteed perks working (checked against the in-game weapon rules of every perk) and is the best its primary + secondary can get.' % len(deck), '',
     '**The weapon line under each card lies sometimes**: it prints the first weapon each spec lists, which can belong to the other slot. Trust the class, then equip: ' + '; '.join(sorted(LIE)) + '.', '',
     '## 1. Take on sight', '',
     'These specs exist on 1 or 2 cards only. If one shows up and the spec is new to you, take it.', '']
for c, why in seen.items():
    L.append('- **%s**: %s. Equip %s.' % (card(c), '; '.join(why), equip(c)))
L += ['', '## 2. Read the tertiary', '',
      '| Tertiary | Verdict |', '|---|---|',
      '| %s | **perfect**: its weapon stacks on the secondary or fills an empty slot |' % ', '.join(A),
      '| %s | good: utility tree |' % ', '.join(B),
      '| %s | filler: passive; take only for a new primary or secondary |' % ', '.join(C1),
      '| %s | filler: healing; take only for a new primary or secondary |' % ', '.join(C2),
      '', '## 3. Tie-break', '',
      '- More specs you have not run yet > perfect > good > filler.',
      '- At every later promotion: a perk whose yellow weapon list names nothing the soldier carries is deleted in missions. Pick another (201 of the cards have at least one such optional perk; guaranteed perks are all fine).', '',
      '## 4. Spec tracker (tick when a soldier gets it; fewest cards first)', '']
for sl in ('Primary', 'Secondary', 'Tertiary'):
    ks = sorted((k for k in cnt if k[0] == sl), key=lambda k: (cnt[k], n(k[1])))
    L.append('**%s** (%d)' % (sl, len(ks)))
    L += ['- [ ] %s (%d)' % (n(k[1]), cnt[k]) for k in ks]
    L.append('')
open('D:/work/vault/.claude/worktrees/xcom-slot-rules-1029/projects/XCOM/pick-sheet.md', 'w', encoding='utf-8', newline='\n').write('\n'.join(L))
print('take-on-sight cards', len(seen), '| perfect T', len(A), A, '| lines', len(L))
