import random
import numpy as np

import components
import pairing
import transmission
import updates
import plots
import files

def initial_network(m_0, nodes,all_links, active_links, average_age_difference, number_of_nodes, number_of_links,
                    assortativity, avg, heterogeneity, clustering, avgpath):
    # initial network
    for i in range(m_0):
        options = [node for node in nodes if node.newbie == 0]
        link = pairing.firstpair(options, average_age_difference)
        link.start = 0
        link.id = len(all_links)
        all_links.append(link)
        active_links.append(link)

    number_of_links.append(len(active_links))
    number_of_nodes.append((len([node for node in nodes if node.newbie != 0])))
    avg.append(2 * number_of_links[0] / number_of_nodes[0])

    options = [node for node in nodes if len(node.neighbors) > 0]
    assortativity.append(components.assortativity(options, active_links))
    heterogeneity.append(components.heterogeneity(options, active_links))
    clustering.append(components.cluster(options, active_links))
    avgpath.append(components.average_path(options, active_links))
    print(number_of_nodes[0], number_of_links[0], assortativity[0])
    print(heterogeneity)


def secondary_link(nodes, all_links, active_links, average_age_difference, epsilon, secondary, m_i, day):
    count = 0
    for j in range(m_i):
        # the node initiating the link
        options = [node for node in nodes if node.newbie != 0]
        node0 = pairing.selection(options)
        # new neighbor hunting
        potential_partners = [node for node in nodes if
                              (node.newbie == 1) and (node.sex != node0.sex) and (node not in node0.neighbors)]
        if len(potential_partners) > 0:
            link = pairing.linking(node0, potential_partners, average_age_difference, epsilon)
            link.start = day
            link.id = len(all_links)
            all_links.append(link)
            active_links.append(link)
            count += 1
    secondary.append(count)

def primary_link(nodes, all_links, active_links, average_age_difference, epsilon, external_nodes, m_0, m, primary, day):

    #nodes in the network
    internal_nodes = [node for node in nodes if node.newbie == 1]

    #count primary links
    count = 0

    # introducing new nodes
    options = [node for node in nodes if node.newbie == 0]
    if len(options) <= external_nodes:
        new_nodes = options
    else:
        new_nodes = random.sample(options, external_nodes)

    #for each new node
    for node0 in new_nodes:
        # number of neighbors
        # number of links to form
        x = 0
        while x == 0:
            x = round(np.random.exponential(m))

        potential_partners = [node for node in internal_nodes if (node.sex != node0.sex)]
        x = min([x, len(potential_partners), m_0])

        # pairing
        for j in range(x):
            link = pairing.linking(node0, potential_partners, average_age_difference, epsilon)
            link.start = day
            link.id = len(all_links)
            all_links.append(link)
            active_links.append(link)

        count += x
    primary.append(count)


def whole_process(m, repeat):
    #setting
    population = 3000
    total_ticks = 1000

    m_0 = 10
    external_nodes = 100
    # m = 3.0

    epsilon = 0.5
    average_duration = 100
    average_age_difference = 3.5

    path = files.create_folder(population, m, epsilon, repeat)
    # 4 vaccination sessions
    vaccination_date = {6, 13, 20, 27}
    # assume vaccination coverage in people under 26 is 10%
    vaccination_coverage = 0.1
    # stage 2 flag
    flag = False

    #topology
    #network growth model functions
    # primary links brought by newly introduced nodes
    primary = [0]
    #secondary links within the network
    secondary = [0]
    #link removals
    removed = [0]

    #create nodes
    nodes, actual_duration = components.create_nodes(population, average_duration, total_ticks)

    rate = 1 / actual_duration
    active_links = []
    all_links = []
    # number of links in the end of phase 1
    total_links = 0
    number_of_links = []
    number_of_nodes = []
    assortativity = []
    heterogeneity = []
    clustering = []
    avgpath = []
    avg = []

    #epidemic dynamics
    #initial prevalence
    transmission.initialization(nodes)

    #compartment
    susceptible = [population for day in range(total_ticks)]
    infected = [0 for day in range(total_ticks)]
    recovered = [0 for day in range(total_ticks)]
    vaccinated = [0 for day in range(total_ticks)]

    female_susceptible = [population for day in range(total_ticks)]
    female_infected = [0 for day in range(total_ticks)]
    female_recovered = [0 for day in range(total_ticks)]
    female_vaccinated = [0 for day in range(total_ticks)]

    male_susceptible = [population for day in range(total_ticks)]
    male_infected = [0 for day in range(total_ticks)]
    male_recovered = [0 for day in range(total_ticks)]
    male_vaccinated = [0 for day in range(total_ticks)]

    #incidences
    incidences = [0 for i in range(total_ticks)]
    cumulative = [0 for i in range(total_ticks)]

    # sex specific
    female_incidences = [0 for i in range(total_ticks)]
    female_cumulative = [0 for i in range(total_ticks)]

    male_incidences = [0 for i in range(total_ticks)]
    male_cumulative = [0 for i in range(total_ticks)]

    #sex specific incidences

    incidences[0], female_incidences[0], male_incidences[0] = transmission.initial_prevalence(nodes)
    cumulative[0] = incidences[0]
    female_cumulative[0] = female_incidences[0]
    male_cumulative[0] = male_incidences[0]

    females = len([node for node in nodes if node.sex == 1])
    males = len([node for node in nodes if node.sex == -1])

    print('HPV-16 Prevalence: {:.2f}, female: {:.2f}, male:{:.2f}'.format(cumulative[0] / population,
                                                                          female_cumulative[0] / females,
                                                                          male_cumulative[0] / males))

    # sir dynamics
    #s, i, r
    susceptible[0], infected[0], recovered[0], vaccinated[0] = transmission.general_sir(nodes)
    (female_susceptible[0], female_infected[0], female_recovered[0], female_vaccinated[0],
     male_susceptible[0], male_infected[0], male_recovered[0], male_vaccinated[0]) = transmission.gender_sir(nodes)


    # vaccination amount
    total_vaccination = int(len([node for node in nodes if node.age < 26]) * vaccination_coverage)
    actual_vaccinated = 0
    print('Expected to vaccinated {} females'.format(total_vaccination))

    #initial network
    initial_network(m_0, nodes, all_links, active_links, average_age_difference, number_of_nodes, number_of_links,
                        assortativity, avg, heterogeneity, clustering, avgpath)

    # iterations
    for day in range(1, total_ticks):
        active_links, x = updates.update_links(active_links, day)
        removed.append(x)
        updates.update_nodes(nodes, day)

        cumulative[day] = cumulative[day - 1]
        female_cumulative[day] = female_cumulative[day - 1]
        male_cumulative[day] = male_cumulative[day - 1]

        # node.newbie 0: not introduced 1:introduced
        # number of secondary links
        # phase 2
        if len([node for node in nodes if node.newbie == 0]) == 0:
            m_i = round(total_links * rate)
            # capture the end of phase 1
            if flag == False:
                flag = True
                files.record_stage(path, nodes)
                total_links = len(active_links)
                m_i = round(total_links * rate)
        # phase 1
        else:
            m_i = round((day * m * external_nodes + m_0) * rate)

        # forming secondary links
        secondary_link(nodes, all_links, active_links, average_age_difference, epsilon, secondary, m_i, day)

        # forming primary links
        options = [node for node in nodes if node.newbie == 0]
        if len(options) == 0:
            primary.append(0)
        else:
            primary_link(nodes, all_links, active_links, average_age_difference, epsilon, external_nodes, m_0, m,
                         primary, day)

        # updates
        number_of_links.append(len(active_links))
        number_of_nodes.append(len([node for node in nodes if node.newbie != 0]))
        avg.append(2 * number_of_links[-1] / number_of_nodes[-1])

        options = [node for node in nodes if len(node.neighbors) > 0]
        assortativity.append(components.assortativity(options, active_links))
        heterogeneity.append(components.heterogeneity(options, active_links))
        clustering.append(components.cluster(options, active_links))
        avgpath.append(components.average_path(options, active_links))

        # transmission simulation
        incidences[day], female_incidences[day], male_incidences[day] = transmission.sexual_contact(active_links)


        cumulative[day] += incidences[day]
        female_cumulative[day] += female_incidences[day]
        male_cumulative[day] += male_incidences[day]

        susceptible[day], infected[day], recovered[day], vaccinated[day] = transmission.general_sir(nodes)
        (female_susceptible[day], female_infected[day], female_recovered[day], female_vaccinated[day],
         male_susceptible[day], male_infected[day], male_recovered[day], male_vaccinated[day]) = (
            transmission.gender_sir(nodes))

        # vaccination session
        if day in vaccination_date:
            transmission.vaccinate_session(nodes, active_links, total_vaccination, actual_vaccinated)
            files.record_vaccination(path, nodes, day)

        print(day, susceptible[day], infected[day], recovered[day], vaccinated[day])
        #print(day, primary[-1], secondary[-1], removed[-1])

    #visualisations
    fig1 = plots.network_dynamics(m, total_links, actual_duration, number_of_nodes, number_of_links)
    fig1.show()

    fig2 = plots.fitting(m, nodes)
    fig2.show()

    fig_sir = plots.general_sir(susceptible, infected, recovered, vaccinated)
    fig_sir.show()

    fig_gender = plots.gender_sir(female_susceptible, female_infected, female_recovered, female_vaccinated,
                                  male_susceptible, male_infected, male_recovered, male_vaccinated)
    fig_gender.show()

    fig_incidence = plots.cumulative_incidence(cumulative, female_cumulative, male_cumulative)
    fig_incidence.show()

    #path = files.create_folder(population, m, epsilon, repeat)
    files.record_network(path, number_of_nodes, number_of_links, assortativity, primary, secondary,
                         removed, avg, heterogeneity, clustering, avgpath)
    files.record_nodes(path, nodes)
    files.record_sir(path, susceptible, infected, recovered, vaccinated,
                     female_susceptible, female_infected, female_recovered, female_vaccinated,
                     male_susceptible, male_infected, male_recovered, male_vaccinated)
    files.record_incidence(path, incidences, cumulative, female_incidences, female_cumulative,
                           male_incidences, male_cumulative)
    files.record_links(path, all_links)



if __name__ == '__main__':
    # for j in range(10):
    #     for i in range(10):
    #         m = 0.5 * j + 0.5
    #         whole_process(m, i)
    #whole_process(0)
    import sys

    whole_process(float(sys.argv[1]), int(sys.argv[2]))
