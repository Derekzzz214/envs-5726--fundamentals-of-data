def is_min_ratio_toilets_to_people_met(ratio):
    toilets_str, people_str = ratio.split('/')
    toilets = int(toilets_str.replace('t', ''))
    people = int(people_str.replace('p', ''))
    return toilets / people >= 1/20
print(is_min_ratio_toilets_to_people_met('1t/37p'))
print(is_min_ratio_toilets_to_people_met('1t/12p'))

def is_population_disabled(disabled, total_population):
    return disabled / total_population >= 0.1
print(is_population_disabled(0, 32))
print(is_population_disabled(52, 392))

def is_gp_religious_or_academic(gp):
    religious = {"Mosque", "Church"}
    academic = {"School", "Institute", "Education", "Faculty"}
    gp_words = set(gp.split())
    return (len(gp_words.intersection(religious)) > 0) or (len(gp_words.intersection(academic)) > 0)
print(is_gp_religious_or_academic('Faculty Of Earth Sciences and Mining'))
print(is_gp_religious_or_academic('Almorada Church'))
print(is_gp_religious_or_academic('Health Insulation Building'))

def get_sanitation_priority(ratio, disabled, pop, gp):
    ratio_met = is_min_ratio_toilets_to_people_met(ratio)
    disabled_met = is_population_disabled(disabled, pop)
    gp_met = is_gp_religious_or_academic(gp)

    if (not ratio_met) and disabled_met and gp_met:
        return 'High Priority'
    elif ratio_met and (not disabled_met) and (not gp_met):
        return 'Lower Priority'
    else:
        return 'Medium Priority'

print(get_sanitation_priority(ratio='1t/49p', disabled=52, pop=392, gp='Faculty - Students Dwelling'))
print(get_sanitation_priority(ratio='1t/29p', disabled=0, pop=178, gp='Mohamed Ali Abbas Secondary School For Girls'))
print(get_sanitation_priority(ratio='1t/17p', disabled=0, pop=52, gp='Alsalam Old Mosque'))
print(get_sanitation_priority(ratio='1t/6p', disabled=0, pop=12, gp='Nile Club'))