s = open('select3.py').read()
s = s.replace("exec(open(TMP + 'audit.py').read()", "exec(open(TMP + 'audit2.py').read()")
s = s.replace('.replace("spec[n.lower()]", "SPEC[n.lower()]"))', '.replace("spec[n.lower()]", "SPEC[n.lower()]").replace("- {\'empty\'}", "- {\'empty\', \'canister\'}"))')
s = s.replace("work = [c for c in built if aud[c][0][0] == 0]", "work = [c for c in built if aud[c][0][0] == 0 and aud[c][2] is not None]   # 11-10b: a real secondary weapon is required")
s = s.replace('"; jepFixes 2026-11-10, cut (replaces the 11-09 list): working cards only (perk audit); no two specs sharing a guaranteed",',
              '"; jepFixes 2026-11-10, cut (replaces the 11-09 list): working cards only (perk audit) with a REAL secondary weapon (a canister beside a",\n       "; chemthrower sits in its own aux slot, so it does not count); no two specs sharing a guaranteed",')
s = s.replace("json.load(open(TMP + 'deck_1109.json'))", "json.load(open(TMP + 'deck_1110.json'))")
s = s.replace("open(TMP + 'deck_1110.json', 'w')", "open(TMP + 'deck_1110b.json', 'w')").replace("open(TMP + 'audit_1110.json', 'w')", "open(TMP + 'audit_1110b.json', 'w')")
s = s.replace("XComAmalgamation.ini.bak-1110a", "XComAmalgamation.ini.bak-1110b")
for k in ("audit2.py", "'canister'}", "is not None", "deck_1110b", "REAL secondary"):
    assert k in s, k
open('select4.py', 'w').write(s)
print('ok')
