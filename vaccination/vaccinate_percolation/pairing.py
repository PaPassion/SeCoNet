from components import *
import updates
import tickets

def firstpair(nodes, average_age_difference):
    node0 = random.choice(nodes)
    options = [node for node in nodes if (node not in node0.neighbors) and (node.sex != node0.sex)]

    #selection
    pool = tickets.initial_pairs(node0, options, average_age_difference)

    pick = random.uniform(0, pool)

    random.shuffle(options)

    for node in options:
        if pick <= node.ticket:
            node1 = node
            break
        else:
            pick -= node.ticket

    if node0.sex == 1:
        link = Link(node0, node1)
    else:
        link = Link(node1, node0)

    while link.duration == 0:
        link.duration = np.random.exponential(min([node0.relationship, node1.relationship]))

    if link.duration == 1:
        link.frequency = 1
    else:
        link.frequency = 0.5

    link.state = 1

    updates.update_neighbors(node0, node1)
    tickets.update_ticket(options)

    return link

def linking(node0, nodes, average_age_difference, epsilon):
    #selection
    options = [node for node in nodes if node not in node0.neighbors]
    pool = tickets.probability(node0, options, average_age_difference, epsilon)

    pick = random.uniform(0, pool)

    random.shuffle(options)

    for node in options:
        if pick <= node.ticket:
            node1 = node
            break
        else:
            pick -= node.ticket

    if node0.sex == 1:
        link = Link(node0, node1)
    else:
        link = Link(node1, node0)

    while link.duration == 0:
        link.duration = np.random.exponential(min([node0.relationship, node1.relationship]))

    if link.duration == 1:
        link.frequency = 1
    else:
        link.frequency = 0.5

    link.state = 1

    updates.update_neighbors(node0, node1)
    tickets.update_ticket(options)

    return link

def selection(nodes):
    options = nodes
    pool = 0
    for node in options:
        node.ticket = max([0, node.lsp - node.sp])
        pool += node.ticket

    pick = random.uniform(0, pool)

    random.shuffle(options)

    for node in options:
        if pick <= node.ticket:
            node0 = node
            break
        else:
            pick -= node.ticket

    tickets.update_ticket(options)
    return node0