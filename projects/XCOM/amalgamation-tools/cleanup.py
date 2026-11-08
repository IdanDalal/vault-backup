"""1108: (a) Choose My Class 50 -> 100; (b) drop jepFixes IncompatibleSpecs pairs that name a spec no active mod defines
(any section, MEC included). Verify the simulated deck is unchanged after (b)."""
import json, re, shutil, sim
C = "C:/Program Files (x86)/Steam/steamapps/common/XCOM 2/XCom2-WarOfTheChosen/XComGame/Mods/jepFixes/Config/"
TMP = "C:/Users/jep/.claude/jobs/94ad0c55/tmp/"
# (a)
f = C + 'XComChooseMyClass.ini'
shutil.copyfile(f, TMP + 'XComChooseMyClass.ini.bak-1108')
b = open(f, 'rb').read()
assert b.count(b'NumClassChoices = 50') == 1
b = b.replace(b'raised to 50 on 2026-09-19 at rookie promotion', b'raised to 50 on 2026-09-19, to 100 on 2026-11-08 at rookie promotion')
b = b.replace(b'NumClassChoices = 50', b'NumClassChoices = 100')
open(f, 'wb').write(b)
print(b.decode('ascii'))
# (b)
active = {v['name'].lower() for v in json.load(open(TMP + 'specs_now.json')).values()}
f = C + 'XComAmalgamation.ini'
shutil.copyfile(f, TMP + 'XComAmalgamation.ini.bak-1108')
before = sim.deck(sim.load())
lines = open(f, 'rb').read().decode('ascii').split('\r\n')
keep, dead = [], []
for l in lines:
    m = re.match(r'^\+IncompatibleSpecs=\(A="(\w+)", B="(\w+)"\)', l)
    if m and not (m.group(1).lower() in active and m.group(2).lower() in active):
        dead.append(l); continue
    keep.append(l)
names = sorted({n for l in dead for n in re.findall(r'"(\w+)"', l) if n.lower() not in active})
i = keep.index("; jepFixes 2026-10-29, Idi's weapon slot optimization. A spec 'carries' a weapon in its own slot (primary spec: primary")
note = ['; jepFixes 2026-11-08 (Idi: remove redundant/out-of-date): %d pairs dropped that named a spec no active mod defines:' % len(dead),
        '; ' + ', '.join(names) + '. Re-enabling one of those mods needs a regenerate against the current rules.', '']
keep = keep[:i] + note + keep[i:]
open(f, 'wb').write('\r\n'.join(keep).encode('ascii'))
after = sim.deck(sim.load())
print('dead pairs removed', len(dead), '| specs', names)
print('deck unchanged:', sorted(before) == sorted(after), len(before), len(after))
