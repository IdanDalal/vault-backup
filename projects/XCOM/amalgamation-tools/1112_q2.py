import json, os, sys
os.chdir('C:/Users/jep/.claude/jobs/94ad0c55/tmp')
sys.path.insert(0, '.')
exec(open('audit2.py').read().split("if __name__")[0])
d = [tuple(c) for c in json.load(open('deck_1110b.json'))]
def show(c):
    print('=' * 100); print('_'.join(c), '| in deck:', c in d)
    for x in c:
        s = SPEC.get(x.lower())
        if not s: print('  NO SPEC', x); continue
        print('  %-16s weapons %s extra %s' % (x, s['weapons'], EXTRA.get(x.lower(), [])))
        for a, r, f in tree(x):
            if r <= 1 or a in M1 or a in M2:
                print('      r%d %-5s %-34s M1=%s M2=%s' % (r, 'fixed' if f else 'deck', a, sorted(M1[a]) if a in M1 else '-', M2.get(a, '-')))
    (fx, tot), pc, sc, dead = audit(c)
    print('  AUDIT best loadout %s + %s | dead fixed %d total %d' % (pc, sc, fx, tot), [(x[0], x[1], x[2]) for x in dead])
cards = [a.split('_') for a in sys.argv[1:]]
for c in cards: show(tuple(c))
