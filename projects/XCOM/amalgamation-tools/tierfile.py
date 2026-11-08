"""Write the tier list (every card) as a vault markdown file."""
import json, collections
exec(open('tiers.py').read().split("rows = collections")[0])
rows = collections.defaultdict(list)
for p, s, t in deck:
    rows[tier(p, s, t)].append((p, s, t))
order = sorted(rows)
best = collections.defaultdict(list); anyc = collections.Counter()
for k in order:
    for p, s, t in rows[k]:
        for sl, x in (('P', p), ('S', s), ('T', t)):
            anyc[(sl, x)] += 1
            if k.startswith('A'): best[(sl, x)].append('%s / %s / %s' % (p, s, t))
L = ['---', 'type: reference', 'created: 2026-11-08', 'author: jep', '---',
     '# Amalgamation card tiers (every card in the deck, 2026-11-08)', '',
     "Deck after Idi's 'all rec' of 11-08: 1,645 cards. Tier = Idi's pick rules (`amalgamation-pick-rules.md`): R1 every tree feeds a carried weapon, tertiary stacks on a weapon already carried or fills an empty secondary slot; R2 generic passive tertiaries low priority; R3 utility tertiary rides an active-device secondary; R8 healing accepted, never sought.",
     "Tiers rank the tertiary's job only. The weapon slot rules (W1-W6) already hold for every card, so the primary and secondary always fit each other.", '',
     '| Tier | Means | Cards |', '|---|---|---|']
for k in order:
    code, _, desc = k.partition(' ')
    L.append('| %s | %s | %d |' % (code, desc, len(rows[k])))
L += ['', '## Specs with no tier A card (best they get is B or C)', '']
noA = sorted('%s %s (%d cards)' % (sl, x, n) for (sl, x), n in anyc.items() if not best[(sl, x)])
L.append(', '.join(noA))
L += ['', '## Best cards per primary and secondary (tier A)', '']
for sl in 'PS':
    for (s2, x) in sorted(k for k in best if k[0] == sl):
        L.append('- %s **%s** (%d of %d): %s' % (sl, x, len(best[(s2, x)]), anyc[(s2, x)], '; '.join(best[(s2, x)])))
for k in order:
    code, _, desc = k.partition(' ')
    L += ['', '## %s %s (%d)' % (code, desc, len(rows[k])), '', 'Grouped by tertiary; each entry is primary + secondary.', '']
    byT = collections.defaultdict(list)
    for p, s, t in rows[k]: byT[t].append('%s + %s' % (p, s))
    for t in sorted(byT, key=lambda t: len(byT[t])):
        L.append('- **%s** (%d): %s' % (t, len(byT[t]), '; '.join(sorted(byT[t]))))
open('D:/work/vault/.claude/worktrees/xcom-slot-rules-1029/projects/XCOM/amalgamation-card-tiers-2026-11-08.md', 'w', encoding='utf-8', newline='\n').write('\n'.join(L) + '\n')
print('lines', len(L), '| specs without tier A:', len(noA))
print(noA)
