import random
import numpy as np

import demography

#HPV-16 0.3 11 & 15.4 months; HPV-18 0.13 9.7 & 11.3 months
transmissibility = 0.13

#infection clearance
viral_clearance = 291

'''
prevalence
        female male
HPV16   8.3     3
HPV18   2.5     1.2
'''
female_prevalence = 0.025
male_prevalence = 0.012

#vaccination_coverage = 0.4


def initialization(nodes):
    for node in nodes:
        if node.sex == 1:
            r =random.random()
            if r <= female_prevalence:
                node.status = 1
                x = max(1, round(np.random.exponential(viral_clearance)))
                node.clearance = max(1, random.randrange(x))
                node.infections += 1
        else:
            r =random.random()
            if r <= male_prevalence:
                node.status = 1
                x = max(1, round(np.random.exponential(viral_clearance)))
                node.clearance = max(1, random.randrange(x))
                node.infections += 1

def initial_prevalence(nodes):
    prevalence_initial = 0
    prevalence_initial_female = 0
    prevalence_initial_male = 0

    for node in nodes:
        if node.status== 1:
            prevalence_initial += 1
            if node.sex == 1:
                prevalence_initial_female += 1
            else:
                prevalence_initial_male += 1
    print("Initial prevalence: {}, female: {}, male: {}".format(prevalence_initial, prevalence_initial_female, prevalence_initial_male))
    return prevalence_initial, prevalence_initial_female, prevalence_initial_male

def sexual_contact(links):
    infection = 0
    female_infection = 0
    male_infection = 0

    for link in links:
        r = random.random()
        if r <= link.frequency:
            female = link.female
            male = link.male
            infection_x, female_infection_x, male_infection_x = transmission(female, male)
            infection += infection_x
            female_infection += female_infection_x
            male_infection += male_infection_x
    return infection, female_infection, male_infection

def transmission(female, male):
    infection = 0
    female_infection = 0
    male_infection = 0

    #male to female
    if female.status == 0 and male.status > 0:
        r = random.random()
        if r <= transmissibility:
            female.status = 1
            female.clearance = max(1, round(np.random.exponential(viral_clearance)))
            female.infections += 1
            female_infection += 1
            infection += 1
    #female to male
    elif male.status == 0 and female.status > 0:
        r = random.random()
        if r <= transmissibility:
            male.status = 1
            male.clearance= max(1, round(np.random.exponential(viral_clearance)))
            male.infections += 1
            male_infection += 1
            infection += 1

    return infection, female_infection, male_infection

def general_sir(nodes):
    # overall
    s = 0  # susceptible
    i = 0  # infection
    r = 0  # immunity
    v = 0  # vaccinated

    for node in nodes:
        if node.status == 0:
            s += 1
        elif node.status == 1:
            i += 1
        elif node.status == -1:
            r += 1
        else:
            v += 1

    return s, i, r, v

def gender_sir(nodes):
    # overall
    female_s = 0  # susceptible
    female_i = 0  # infection
    female_r = 0  # immunity
    female_v = 0

    male_s = 0  # susceptible
    male_i = 0  # infection
    male_r = 0  # immunity
    male_v = 0

    for node in nodes:
        if node.sex == 1:
            if node.status == 0:
                female_s += 1
            elif node.status == 1:
                female_i += 1
            elif node.status == -1:
                female_r += 1
            else:
                female_v += 1
        else:
            if node.status == 0:
                male_s += 1
            elif node.status == 1:
                male_i += 1
            elif node.status == -1:
                male_r += 1
            else:
                male_v += 1

    return female_s, female_i, female_r, female_v, male_s, male_i, male_r, male_v

def vaccinate_session(nodes, total_vaccination, actual_vaccinated):
    nodes.sort(key = lambda x: len(x.neighbors), reverse=True)
    count = 0

    for node in nodes:
        if node.status == 0 and node.newbie == 1 and node.age < 26:
            node.status = -2
            count += 1
            if count == total_vaccination // 4:
                break

    actual_vaccinated += count