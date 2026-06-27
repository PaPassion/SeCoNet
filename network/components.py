import random
import numpy as np
import networkx as nx
from networkx.algorithms import bipartite

import demography

class Node:
    def __init__(self):
        self.id = 0
        self.age = 0 #ranges from 15 to 49
        self.sex = 0 #1:female; -1:male
        self.ticket = 0 #prospensity to be chosen
        self.lsp = 0  #estimated lifetime sexual partners
        self.sp = 0 #number of sexual partners
        self.original_sp = 0 #number of sexual partners at the beginning of the simulation
        self.relationship = 0 #mean duration of relationships

        self.fitness = 0

        self.newbie = 0  # 0: not introduced 1:introduced
        self.neighbors = []

        self.status = 0 #0:susceptible; 1: infected; -1: recovered; -2:vaccinated
        self.clearance = 0 #clearance period
        self.duration = 0  # clearance period


    def initial(self, average_duration, total_ticks):
        self.age_distribution()
        self.sex_distribution()
        self.lsp_distribution(average_duration, total_ticks)
        #self.fitness_distribution()

    def age_distribution(self):
        r = random.random()
        x = 0
        for i in range(len(demography.age_cumulative_proportions)):
            x += demography.age_cumulative_proportions[i]
            if r <= x:
                self.age = 15 + 5 * i + random.randrange(5)
                break

    def sex_distribution(self):
        r = random.random()
        if r <= demography.gender_proportions[0]:
            self.sex = 1
        else:
            self.sex = -1

    def lsp_distribution(self, average_duration, total_ticks):
        r = 0
        while r == 0:
            r = np.random.gamma(average_duration, size = None)

        self.relationship = r
        self.lsp = total_ticks / self.relationship

        if self.age < 18:
            self.sp = 0
            self.original_sp = 0
        else:
            self.sp = random.randrange(round(self.lsp))
            self.original_sp = self.sp

    def fitness_distribution(self):
        while self.fitness <= 0:
            self.fitness = np.random.poisson(1000)
            #self.fitness = np.random.gamma(100, 10)

def create_nodes(population, average_duration, total_ticks):
    nodes = []
    total = 0
    for i in range(population):
        item = Node()
        item.id = i
        item.initial(average_duration, total_ticks)
        total += item.relationship
        nodes.append(item)
    # nodes.sort(key=lambda x: x.fitness, reverse=True)
    # for i in range(5):
    #     nodes[i].fitness *= 100
    # print([node.fitness for node in nodes])
    return nodes, total / len(nodes)


class Link:
    def __init__(self, female, male):
        self.id = id
        self.male = male
        self.female = female
        self.duration  = 0 #estimated relationship duration
        self.length = 0 #length of the relationship
        self.frequency = 0 #sex frequency
        self.start = -1
        self.end = -1

def assortativity(nodes, links):
    #average degree
    degree = []
    avg = 0
    for node in nodes:
        degree.append(len(node.neighbors))
    mu = np.mean(degree)

    #degree distribution
    dict = {}
    for x in degree:
        if x in dict.keys():
            dict[x] += 1
        else:
            dict[x] = 1
    for key in dict.keys():
        dict[key] /= len(nodes)

    ex = 0
    for x in dict.keys():
        ex += x * dict[x]

    #excess degree distribution
    excess_dict = {}
    for x in dict.keys():
        excess_dict[x-1] = x * dict[x] / ex
    part1 = 0
    part2 = 0
    for x in excess_dict.keys():
        part1 += x ** 2 * excess_dict[x]
        part2 += x * excess_dict[x]
    var_excess = part1 - part2 ** 2

    #joint excess degree distribution
    joint_dict = {}
    joint = []
    for link in links:
        x1 = (len(link.female.neighbors) - 1, len(link.male.neighbors) -1)
        x2 = (len(link.male.neighbors) - 1, len(link.female.neighbors) - 1)
        if x1 not in joint_dict.keys():
            joint_dict[x1] = 1
        else:
            joint_dict[x1] += 1
        if x2 not in joint_dict.keys():
            joint_dict[x2] = 1
        else:
            joint_dict[x2] += 1
        joint.append(x1)
        joint.append(x2)
    for x in joint_dict.keys():
        joint_dict[x] = joint_dict[x] / len(links) / 2


    #assortativity
    value = 0
    for key in joint_dict.keys():
        value += key[0] * key[1] * (joint_dict[key] - excess_dict[key[0]] * excess_dict[key[1]])
    if var_excess != 0:
        value /= var_excess
    else:
        value = 0

    return value


def heterogeneity(nodes, links):
    value = 0
    for link in links:
        x = len(link.female.neighbors) * len(link.male.neighbors)
        x = x ** (-1/2)
        value += x
    n = len(nodes)
    result = (n - 2 * value) / (n - (n - 1) ** 0.5 * 2)
    return result

def average_path(nodes, links):
    graph = nx.Graph()
    graph.add_nodes_from(nodes)
    graph.add_edges_from([(link.female, link.male) for link in links])

    if nx.is_connected(graph):
        result = nx.average_shortest_path_length(graph)
    else:
        c = max(nx.connected_components(graph))
        component = graph.subgraph(c).copy()
        result = nx.average_shortest_path_length(component)

    return result

def cluster(nodes, links):
    females = [node for node in nodes if node.sex == 1]
    males = [node for node in nodes if node.sex == -1]

    graph = nx.Graph()
    graph.add_nodes_from(females, bipartite = 1)
    graph.add_nodes_from(males, bipartite=0)
    graph.add_edges_from([(link.female, link.male) for link in links])

    result = bipartite.average_clustering(graph, nodes,'dot')

    return result






