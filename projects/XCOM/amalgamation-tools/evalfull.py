import json, collections, sim
o = json.load(open('slotrule_out.json')); G = o['G']; rel = json.load(open('release_out.json'))
hdr = '[AmalgamationClassesWOTC.X2SoldierClass_Amalgamation]\n'
cand = hdr + '\n'.join(l for _, l in rel) + '\n' + '+IncompatibleSpecs=(A="Commissar", B="Commissar")\n' + '\n'.join(l for _, l in o['lines']) + '\n'
open('candidate.ini', 'w', newline='\r\n').write(cand)
def live(extra):
    st = sim.load(extra); return [x[:3] for x in sim.deck(st) if not x[3]], st
base, st0 = live(None); full, st1 = live(cand)
print('deck', len(base), '->', len(full), '| pairs', len(st0['inc']), '->', len(st1['inc']))
def cnt(dk):
    c = collections.Counter()
    for p, s, t in dk: c['P|'+p] += 1; c['S|'+s] += 1; c['T|'+t] += 1
    return c
c0, c1 = cnt(base), cnt(full)
for g, mem in G.items():
    sl = g[-1]
    print(' ', g, ', '.join('%s %d->%d' % (m, c0[sl+'|'+m], c1[sl+'|'+m]) for m in mem))
print('ZERO now (were >0):', [k for k in c0 if c0[k] and not c1[k]])
# violations check: every surviving class obeys every rule
bad = collections.Counter()
L = {k: {x.lower() for x in v} for k, v in G.items()}
for p, s, t in full:
    p, s, t = p.lower(), s.lower(), t.lower()
    if (p in L['SwP']) != (s in L['SwS']): bad['sword'] += 1
    if (p in L['PiP']) != (s in L['PiS']): bad['pistol'] += 1
    if (s in L['GaS']) != (t in L['GaT']): bad['gauntlet'] += 1
    if t in L['GrT'] and s not in L['GrS']: bad['gremlin'] += 1
    if (p in L['CaP']) != (s in L['CaS']): bad['cannon'] += 1
    if (s in L['ShS']) != (t in L['ShT']): bad['shield'] += 1
    if t == 'commissar': bad['commissar'] += 1
print('rule violations in final deck:', dict(bad) or 'none')
added = collections.Counter(); removed = 0
sb, sf = set(map(tuple, base)), set(map(tuple, full))
print('classes newly created by releases:', len(sf - sb), '| removed:', len(sb - sf))
for p, s, t in sorted(sf - sb)[:400]: added[(p, s)] += 1
print('new P+S pairings (count of tertiaries):', dict(added))
json.dump(full, open('deck_final.json', 'w'))
