"""Audit every class the pair rules build (before the D4 DisableClass cut). Writes audit_all.json."""
import json, collections, sim
exec(open('audit.py').read().split("if __name__")[0])
st = sim.load()
built = [tuple(x[:3]) for x in sim.deck(st)]   # x[3] = disabled flag, ignored here
res = {}
for c in built:
    (fx, tot), pc, sc, dead = audit(c)
    res['_'.join(c)] = dict(c=c, fixed=fx, total=tot, load=[pc, sc], dead=[[d[0], d[1], d[2], d[3]] for d in dead])
json.dump(res, open('audit_all.json', 'w'))
ok = [v for v in res.values() if v['fixed'] == 0]
print('built', len(built), '| no dead guaranteed perk', len(ok), '| broken', len(built) - len(ok))
n_all, n_ok = collections.Counter(), collections.Counter()
for v in res.values():
    for i, x in enumerate(v['c']):
        n_all[('PST'[i], x)] += 1
        if v['fixed'] == 0: n_ok[('PST'[i], x)] += 1
zero = sorted(k for k in n_all if n_ok[k] == 0)
print('specs with no working card:', len(zero))
for k in zero:
    why = collections.Counter(d[1] for v in res.values() if k[1] in v['c'] for d in v['dead'] if d[3])
    print('  ', k, n_all[k], 'cards; dead guaranteed perks:', dict(why.most_common(4)))
