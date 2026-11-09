exec(open('audit.py').read().split("# M1 tables")[0])
import re
want_sets = {'rifles', 'melee', 'precisionrifles', 'sparkrifles', 'pistols'}
want_ab = {'nimblehands', 'rapidfire', 'inthezone', 'mzbuckleyourswash', 'mzangerstrike'}
seen = set()
for mod, sec, s in lines_of('XComAbilityToSlotReassignment.ini'):
    m = re.match(r'^\+WeaponCategorySets\s*=\s*\(\s*WeaponCategorySetName\s*=\s*"?(\w+)"?', s, re.I)
    if m and m.group(1).lower() in want_sets:
        k = ('set', m.group(1).lower()); print(('WIN ' if k not in seen else '    ') + mod[:40], '|', s[:120]); seen.add(k)
    m = re.match(r'^\+AbilityWeaponCategories\s*=\s*\(\s*AbilityName\s*=\s*"?(\w+)"?', s, re.I)
    if m and m.group(1).lower() in want_ab:
        k = ('ab', m.group(1).lower()); print(('WIN ' if k not in seen else '    ') + mod[:40], '|', s[:120]); seen.add(k)
print('load order head:', [x['Name'][:30] for x in act if glob.glob(x['Path'] + '/Config/**/XComAbilityToSlotReassignment.ini', recursive=True)])
