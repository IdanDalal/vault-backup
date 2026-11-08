"""Price cut rules on the live deck. Tier order A1/A2/A3 > B > C. Never let a spec reach 0."""
import json, collections
exec(open('tiers.py').read().split("rows = collections")[0])
rank = lambda k: 0 if k.startswith('A') else (1 if k.startswith('B') else 2)
cards = [(p, s, t, tier(p, s, t)) for p, s, t in deck]
byPS = collections.defaultdict(list)
for c in cards: byPS[(c[0], c[1])].append(c)
def spec_counts(keep):
    n = collections.Counter()
    for p, s, t, _ in keep: n[('P', p)] += 1; n[('S', s)] += 1; n[('T', t)] += 1
    return n
base = spec_counts(cards)
def report(name, keep):
    n = spec_counts(keep)
    zero = [k for k in base if n[k] == 0]
    tc = collections.Counter(rank(c[3]) for c in keep)
    print('%-62s keep %4d (A %d, B %d, C %d) | specs at 0: %s' % (name, len(keep), tc[0], tc[1], tc[2], zero))
    return zero
# D1: within a P+S pair keep only the best tier present
d1 = [c for c in cards if rank(c[3]) == min(rank(x[3]) for x in byPS[(c[0], c[1])])]
report('D1 keep only the best tier within each primary+secondary', d1)
# D2: D1, then a C-only P+S keeps one passive and one healer at most (the rarest tertiary of each kind)
tcount = collections.Counter(c[2] for c in cards)
def d2f(keep):
    out = []
    g = collections.defaultdict(list)
    for c in keep: g[(c[0], c[1])].append(c)
    for ps, cs in g.items():
        if rank(cs[0][3]) < 2: out += cs; continue
        for kind in ('C1', 'C2'):
            sub = sorted([c for c in cs if c[3].startswith(kind)], key=lambda c: tcount[c[2]])
            out += sub[:1]
    return out
d2 = d2f(d1)
z = report('D2 = D1, and a passive-only pair keeps 1 passive + 1 healer', d2)
# D3: D1, and a passive-only pair keeps just its rarest tertiary
def d3f(keep):
    out = []; g = collections.defaultdict(list)
    for c in keep: g[(c[0], c[1])].append(c)
    for ps, cs in g.items():
        if rank(cs[0][3]) < 2: out += cs; continue
        out += sorted(cs, key=lambda c: tcount[c[2]])[:1]
    return out
d3 = d3f(d1)
report('D3 = D1, and a passive-only pair keeps 1 card (rarest tertiary)', d3)
json.dump({'D1': [c[:3] for c in d1], 'D2': [c[:3] for c in d2], 'D3': [c[:3] for c in d3]}, open('cuts_out.json', 'w'))
def d4f(keep):
    out = []; g = collections.defaultdict(list)
    for c in keep: g[(c[0], c[1])].append(c)
    for ps, cs in g.items():
        if rank(cs[0][3]) < 2: out += cs; continue
        out += sorted(cs, key=lambda c: (0 if c[3].startswith('C1') else 1, tcount[c[2]]))[:1]
    return out
d4 = d4f(d1)
report('D4 = D1, passive-only pair keeps 1 card (passive before healer)', d4)
n4 = spec_counts(d4)
print('D4 tertiary counts:', {k[1]: n4[k] for k in sorted((k for k in n4 if k[0] == 'T'), key=lambda k: n4[k])})
print('D4 lowest P/S:', sorted(((n4[k], k) for k in n4 if k[0] in 'PS'))[:12])
json.dump([list(c[:3]) for c in d4], open('deck_d4.json', 'w'))
n2 = spec_counts(d2)
print('D2 tertiary counts:', {k[1]: n2[k] for k in sorted((k for k in n2 if k[0] == 'T'), key=lambda k: n2[k])})
