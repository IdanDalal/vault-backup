"""Carry Idi's ticked tracker boxes from the vault copy into the regenerated sheet (match by slot section + spec name)."""
import re
OLD = 'D:/work/vault/projects/XCOM/pick-sheet.md'
NEW = 'D:/work/vault/.claude/worktrees/xcom-slot-rules-1029/projects/XCOM/pick-sheet.md'
def ticks(path):
    sec, out = None, set()
    for l in open(path, encoding='utf-8').read().splitlines():
        m = re.match(r'^\*\*(Primary|Secondary|Tertiary)\*\*', l)
        if m: sec = m.group(1); continue
        m = re.match(r'^- \[x\] (.+?) \(\d+\)$', l, re.I)
        if m and sec: out.add((sec, m.group(1)))
    return out
got = ticks(OLD)
lines, sec, done = open(NEW, encoding='utf-8').read().splitlines(), None, set()
for i, l in enumerate(lines):
    m = re.match(r'^\*\*(Primary|Secondary|Tertiary)\*\*', l)
    if m: sec = m.group(1); continue
    m = re.match(r'^- \[ \] (.+?) \(\d+\)$', l)
    if m and (sec, m.group(1)) in got:
        lines[i] = l.replace('- [ ]', '- [x]', 1); done.add((sec, m.group(1)))
open(NEW, 'w', encoding='utf-8', newline='\n').write('\n'.join(lines))
print('ticks found', len(got), '| carried', len(done), '| not placed:', sorted(got - done))
print(sorted(got))
