"""Every spec in the live deck: slot, own weapons, guaranteed squaddie perks, and the primary weapon categories of the cards it sits on.
For an eye pass on perks that load but do nothing off their weapon."""
import json, os, sys, collections
os.chdir('C:/Users/jep/.claude/jobs/94ad0c55/tmp'); sys.path.insert(0, '.')
exec(open('audit2.py').read().split("if __name__")[0])
st = sim.load()
live = [tuple(x[:3]) for x in sim.deck(st) if not x[3]]
def pw(spec): return [w for w, sl in SPEC[spec.lower()]['weapons'] if sl == 'PrimaryWeapon']
def sw(spec): return [w for w, sl in SPEC[spec.lower()]['weapons'] if sl == 'SecondaryWeapon']
for i, slot in enumerate('PST'):
    for x in st[slot]:
        cards = [c for c in live if c[i] == x]
        if not cards: continue
        r0 = [a for a, r, f in tree(x) if r == 0 and f]
        prim = collections.Counter(w for c in cards for w in pw(c[0])[:1])
        sec = collections.Counter(w for c in cards for w in (sw(c[1])[:1] or ['-']))
        own = ('P:' + '/'.join(pw(x))) if slot == 'P' else ('S:' + '/'.join(sw(x)) + (' P:' + '/'.join(pw(x)) if pw(x) else ''))
        print('%s %-18s %-34s r0 %-44s on primaries %s%s' % (slot, x, own[:34], ','.join(r0)[:44], dict(prim.most_common(4)), '' if slot == 'S' else ' sec ' + str(dict(sec.most_common(3)))))
