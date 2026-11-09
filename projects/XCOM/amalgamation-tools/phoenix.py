import collections, itertools, sim, json
exec(open('audit2.py').read().split("if __name__")[0])
st = sim.load()
auth, jep = set(), collections.defaultdict(list)
for a, b, mod in st['inc']:
    (jep[frozenset((a, b))].append(mod) if mod == 'jepFixes' else auth.add(frozenset((a, b))))
def pairs(c):
    t = [x.lower() for x in c]
    return [frozenset(p) for p in itertools.combinations(t, 2)] + [frozenset((x,)) for x in t]
Z = 'Phoenix'
rows = []
for p in st['P']:
    for t in st['T']:
        c = (p, Z, t)
        if any(q in auth for q in pairs(c)): continue
        (fx, tot), pc, sc, dead = audit(c)
        if fx or sc is None: continue
        blk = [tuple(sorted(q)) for q in pairs(c) if q in jep]
        rows.append((len(blk), tot, '_'.join(c), pc, sc, blk))
rows.sort()
print('author-approved working Swash combos:', len(rows))
for r in rows[:25]: print('  ', r)
