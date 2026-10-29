"""Release author IncompatibleSpecs bans on the pairings Idi's weapon-slot rules require (W1 sword P x sword S, W2 pistol,
W3 gauntlet, W4 gremlin T x gremlin S, W5 cannon x SiegeGunner, W6 shield). jep's own pairs stay.
Each '-' line is a byte copy of the '+' line (leading + -> -), only from the section the engine reads."""
import json, re, collections, sim
o = json.load(open('slotrule_out.json')); G = o['G']
TARGET = [('SwP', 'SwS'), ('PiP', 'PiS'), ('GaS', 'GaT'), ('GrT', 'GrS'), ('CaP', 'CaS'), ('ShS', 'ShT')]
want = {frozenset((a.lower(), b.lower())) for x, y in TARGET for a in G[x] for b in G[y]}
raw = collections.defaultdict(list)  # pair -> [(mod, raw line without '+')]
for mod, p, t in sim.files():
    if 'jepfixes' in p.lower():
        continue
    sec = ''
    for l in t.splitlines():
        s = l.strip()
        m = re.match(r'^\[([^\]]+)\]', s)
        if m:
            sec = m.group(1).strip().lower(); continue
        if sec != sim.SEC_CLS or not l.lstrip().startswith('+IncompatibleSpecs'):
            continue
        mm = re.search(r'A\s*=\s*"?(\w+)"?\s*,\s*B\s*=\s*"?(\w+)"?', l)
        if mm and frozenset((mm.group(1).lower(), mm.group(2).lower())) in want:
            lead = l[:len(l) - len(l.lstrip())]
            raw[frozenset((mm.group(1).lower(), mm.group(2).lower()))].append((mod, '-' + l.lstrip()[1:]))
jep = {frozenset((a, b)) for a, b, m in sim.load()['inc'] if m == 'jepFixes'}
lines = []
for pr in sorted(raw, key=sorted):
    if pr in jep:
        continue  # still blocked by jep's own rule; releasing the author line alone changes nothing
    for mod, l in raw[pr]:
        lines.append((mod, l))
print('author pairs released', len({frozenset(re.findall(r'"(w+)"', l)) for _, l in lines}), 'lines', len(lines))
for mod, l in lines:
    print('  %-40s %s' % (mod[:40], l.strip()))
json.dump(lines, open('release_out.json', 'w'), indent=0)
