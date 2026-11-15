"""Refresh the pick sheet from deck_1115.json, keeping layout and every tick. Reads the live vault copy, writes the worktree copy."""
import json, re, sys, collections
OLD = 'C:/Users/jep/.claude/jobs/94ad0c55/tmp/'
MAIN, WT = sys.argv[1], sys.argv[2]
deck = [tuple(c) for c in json.load(open('C:/Users/jep/.claude/jobs/0815ca4d/tmp/deck_1115.json'))]
N = json.load(open(OLD + 'names.json')); n = lambda x: N.get(x, x)
cards = {'%s - %s - %s' % (n(a), n(b), n(c)) for a, b, c in deck}
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
        flush(); sec = m.group(1); out.append('**%s** (%d)' % (sec, len(cnt[sec]))); continue
    m = re.match(r'^- \[([ x])\] (.+?) \((\d+)\)$', l)
    if m and sec:
        name, old = m.group(2), int(m.group(3))
        assert name in cnt[sec], (sec, name)
        seen[sec].add(name)
        if cnt[sec][name] != old: log.append('%s %s: %d -> %d' % (sec, name, old, cnt[sec][name]))
        blk.append('- [%s] %s (%d)' % (m.group(1), name, cnt[sec][name])); continue
    flush()
    if l.startswith('## 3.'): sec = None
    out.append(l)
flush()
for s in cnt: assert not (set(cnt[s]) - seen[s]), (s, set(cnt[s]) - seen[s])
txt = '\n'.join(out)
m = re.search(r'(\d+) cards left in the game', txt); txt = txt.replace(m.group(0), '%d cards left in the game' % len(deck))
lines = txt.split('\n')
tos = [i for i, l in enumerate(lines) if re.match(r'^- \[[ x]\] \*\*', l)]
gone = [lines[i] for i in tos if re.search(r'\*\*(.+?)\*\*', lines[i]).group(1) not in cards]
print('take-on-sight lines whose card left the deck:', gone)
listed = ' '.join(lines[i] for i in tos)
need = [(s, x) for s in cnt for x, v in sorted(cnt[s].items()) if v <= 2 and ('%s %s (' % (x, s.lower())) not in listed]
print('rare specs not yet listed:', need)
assert need == [('Secondary', 'Stygian Slayer')] and not gone
assert 'Androctonus - Stygian Slayer - Scout' in cards
add = ['- [ ] **Androctonus - Stygian Slayer - Scout**: Stygian Slayer secondary (1 card). Equip sniper rifle + pistol.']
body = sorted([lines[i] for i in tos] + add, key=lambda l: re.search(r'\*\*(.+?)\*\*', l).group(1))
lines[tos[0]:tos[-1] + 1] = body
txt = '\n'.join(lines)
print('\n'.join(log))
print('ticks before/after', '\n'.join(src).count('- [x]'), txt.count('- [x]'), '| cards', len(deck))
open(WT, 'wb').write(txt.encode('utf-8'))
