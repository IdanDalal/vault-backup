exec(open('audit.py').read().split("# M1 tables")[0])
import re
for mod, sec, s in lines_of('XComAmalgamation.ini'):
    if sec == sim.SEC_DLC and re.search(r'AbilityRestrictions.*(slamfire|fearsome)', s, re.I):
        print('M2', mod[:45], '|', s[:140])
for mod, sec, s in lines_of('XComAbilityToSlotReassignment.ini'):
    if re.search(r'AbilityName\s*=\s*"?(NimbleHands|ShadowOps_SlamFire|ShadowOps_Fearsome)\b', s, re.I):
        print('M1', mod[:45], '|', s[:140])
# which specs carry these perks as fixed skills
exec(open('audit.py').read().split("if __name__")[0].split("# M1 tables")[1].split("SPEC = {")[0].split("def tree")[0][:0])
