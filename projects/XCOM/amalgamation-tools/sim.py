"""Amalgamation deck simulator. Mirrors X2SoldierClass_Amalgamation.uc:100-113 + 548-561 (pair A,B both among P,S,T kills
the class) and X2DownloadableContentInfo:130-165 (DisableClass -> NumInDeck 0). Reads only the sections the engine reads,
from every active AML mod's Config/**/XComAmalgamation.ini. Optional argv[1] = extra ini text appended last (a candidate)."""
import json, glob, re, sys, collections
SEC_CLS = 'amalgamationclasseswotc.x2soldierclass_amalgamation'
SEC_DLC = 'amalgamationclasseswotc.x2downloadablecontentinfo_amalgamationclasseswotc'
ST = r'C:/XCOM2 AML 1.6.0-beta/settings.json'

def rd(p):
    b = open(p, 'rb').read()
    return b.decode('utf-16') if b[:2] in (b'\xff\xfe', b'\xfe\xff') else b.decode('utf-8', 'replace')

def files():
    d = json.load(open(ST, encoding='utf-8-sig'))
    act = [x for c in d['Mods']['Entries'].values() for x in c['Entries'] if x.get('isActive')]
    for x in act:
        for p in sorted(glob.glob(x['Path'] + '/Config/**/XComAmalgamation.ini', recursive=True)):
            yield x['Name'], p, rd(p)

def logical_lines(t):
    """join backslash-continued lines (Amalgamation files use '\\\\' at line end)"""
    buf = ''
    for l in t.splitlines():
        s = l.rstrip()
        if s.endswith('\\'):
            buf += s.rstrip('\\') + ' '
            continue
        yield buf + l
        buf = ''
    if buf:
        yield buf

def load(extra=None):
    st = dict(P=[], S=[], T=[], inc=[], dis=[])
    keymap = {'primaryspecs': 'P', 'secondaryspecs': 'S', 'tertiaryspecs': 'T', 'incompatiblespecs': 'inc'}
    srcs = list(files())
    if extra:
        srcs.append(('CANDIDATE', 'candidate', extra))
    for mod, p, t in srcs:
        sec = ''
        for l in logical_lines(t):
            s = l.strip()
            m = re.match(r'^\[([^\]]+)\]', s)
            if m:
                sec = m.group(1).strip().lower(); continue
            m = re.match(r'^([+\-!]?)(\w+)\s*=\s*(.*)$', s)
            if not m:
                continue
            op, key, val = m.group(1), m.group(2).lower(), m.group(3)
            if sec == SEC_CLS and key in keymap:
                lst = st[keymap[key]]
                if key == 'incompatiblespecs':
                    mm = re.search(r'A\s*=\s*"?([\w]+)"?\s*,\s*B\s*=\s*"?([\w]+)"?', val)
                    item = (mm.group(1).lower(), mm.group(2).lower(), mod) if mm else None
                else:
                    mm = re.search(r'Spec\s*=\s*"([^"]+)"', val)
                    item = (mm.group(1), mod) if mm else None
                if op == '!':
                    lst.clear()
                elif op == '-' and item:
                    for i, x in enumerate(lst):
                        if x[:-1] == item[:-1]:
                            del lst[i]; break
                elif item:
                    lst.append(item)
            elif sec == SEC_DLC and key == 'disableclass':
                v = val.strip().strip('"').lower()
                if op == '+':
                    st['dis'].append(v)
                elif op == '-' and v in st['dis']:
                    st['dis'].remove(v)
    # unique specs, first definition wins (engine keeps duplicates, but class names would collide)
    for k in 'PST':
        seen = set(); u = []
        for n, mod in st[k]:
            if n.lower() not in seen:
                seen.add(n.lower()); u.append(n)
        st[k] = u
    return st

def deck(st):
    pairs = collections.defaultdict(set)
    for a, b, _ in st['inc']:
        pairs[a].add(b); pairs[b].add(a)
    dis = set(st['dis'])
    out = []
    for p in st['P']:
        for s in st['S']:
            for t in st['T']:
                tri = (p.lower(), s.lower(), t.lower())
                if any(y in pairs[x] for x in tri for y in tri):
                    continue
                name = '%s_%s_%s' % (p, s, t)
                out.append((p, s, t, name.lower() in dis))
    return out

if __name__ == '__main__':
    extra = open(sys.argv[1]).read() if len(sys.argv) > 1 else None
    st = load(extra)
    dk = deck(st)
    live = [x for x in dk if not x[3]]
    print('specs P/S/T', len(st['P']), len(st['S']), len(st['T']), '| pairs', len(st['inc']), '| DisableClass', len(st['dis']))
    print('classes built', len(dk), '| in deck (not disabled)', len(live))
    json.dump([x[:3] for x in live], open(sys.argv[2] if len(sys.argv) > 2 else 'deck_now.json', 'w'))
