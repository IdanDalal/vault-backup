"""Refresh the pick sheet from the live deck, keeping its layout and every tick. Reads the live vault copy (Idi's ticks), writes the worktree copy."""
import json, re, sys, collections
OLD = 'C:/Users/jep/.claude/jobs/94ad0c55/tmp/'
MAIN, WT = sys.argv[1], sys.argv[2]
deck = [tuple(c) for c in json.load(open('C:/Users/jep/.claude/jobs/0815ca4d/tmp/deck_1112.json'))]
N = json.load(open(OLD + 'names.json')); n = lambda x: N.get(x, x)
cnt = {'Primary': collections.Counter(), 'Secondary': collections.Counter(), 'Tertiary': collections.Counter()}
for p, s, t in deck: cnt['Primary'][n(p)] += 1; cnt['Secondary'][n(s)] += 1; cnt['Tertiary'][n(t)] += 1
src = open(MAIN, 'rb').read().decode('utf-8').replace('\r\n', '\n').split('\n')
out, sec, blk, log = [], None, [], []
def flush():
    blk.sort(key=lambda l: int(re.search(r'\((\d+)\)$', l).group(1)))
    out.extend(blk); blk.clear()
seen = {k: set() for k in cnt}
for l in src:
    m = re.match(r'^\*\*(Primary|Secondary|Tertiary)\*\* \((\d+)\)$', l)
    if m:
        flush(); sec = m.group(1)
        out.append('**%s** (%d)' % (sec, len(cnt[sec]))); continue
    m = re.match(r'^- \[([ x])\] (.+?) \((\d+)\)$', l)
    if m and sec:
        name, old = m.group(2), int(m.group(3))
        if name not in cnt[sec]:
            log.append('DROPPED from tracker (0 cards): %s %s' % (sec, name)); continue
        seen[sec].add(name)
        if cnt[sec][name] != old: log.append('%s %s: %d -> %d' % (sec, name, old, cnt[sec][name]))
        blk.append('- [%s] %s (%d)' % (m.group(1), name, cnt[sec][name])); continue
    flush()
    if l.startswith('## 3.'): sec = None
    out.append(l)
flush()
for s in cnt:
    miss = set(cnt[s]) - seen[s]
    assert not miss, (s, miss)
txt = '\n'.join(out)
m = re.search(r'(\d+) cards left in the game', txt); assert m
txt = txt.replace(m.group(0), '%d cards left in the game' % len(deck))
# take-on-sight: add the two Buckler cards (the only spec that moved into the 1-2 card range)
rare_now = {(s, x) for s in cnt for x, v in cnt[s].items() if v <= 2}
lines = txt.split('\n')
tos = [i for i, l in enumerate(lines) if re.match(r'^- \[[ x]\] \*\*', l)]
listed = ' '.join(lines[i] for i in tos)
need = [(s, x) for s, x in sorted(rare_now) if ('%s %s (' % (x, s.lower())) not in listed]
print('rare specs not yet on the take-on-sight list:', need)
assert need == [('Secondary', 'Buckler')], need
add = ['- [ ] **Captain - Buckler - Scout**: Buckler secondary (2 cards). Equip sword + pistol.',
       '- [ ] **Captain - Buckler - Smoker**: Buckler secondary (2 cards). Equip sword + pistol.']
body = sorted([lines[i] for i in tos] + add, key=lambda l: re.search(r'\*\*(.+?)\*\*', l).group(1))
lines[tos[0]:tos[-1] + 1] = body
txt = '\n'.join(lines)
tip = '; Heavy beside Rocketeer (the squaddie starts with the rocket launcher; swap it for the gauntlet, which keeps every perk of both)'
key = 'SwordMaster (label says sword; it carries shield or sword in the secondary slot)'
assert txt.count(key) == 1 and tip not in txt
txt = txt.replace(key, key + tip)
print('\n'.join(log))
print('ticks before/after', '\n'.join(src).count('- [x]'), txt.count('- [x]'), '| cards', len(deck))
open(WT, 'wb').write(txt.encode('utf-8'))
