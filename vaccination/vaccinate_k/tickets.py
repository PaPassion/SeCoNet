#phi numerator: fitness of node j
#phi denominator: age difference, lsp difference

def initial_pairs(node0, nodes, average_age_difference):
    pool = 0
    for node in nodes:
        # node.ticket = node.fitness / (max([average_age_difference, node0.age - node.age]) * max([1, abs(node0.lsp - node.lsp)]))
        node.ticket = 1 / (
                    max([average_age_difference, abs(node0.age - node.age)]) * max([1, abs(node0.lsp - node.lsp)]))
        pool += node.ticket

    return pool

def probability(node0, nodes, average_age_difference, epsilon):
    pool = 0
    for node in nodes:
        # phi = node.fitness / (max([average_age_difference, node0.age - node.age]) *
        #                       max([1, abs(node0.lsp - node.lsp)]))
        phi = 1 / (max([average_age_difference, abs(node0.age - node.age)]) * max([1, abs(node0.lsp - node.lsp)]))
        node.ticket = (len(node.neighbors) + epsilon) * phi
        pool += node.ticket

    return pool
def update_ticket(nodes):
    for node in nodes:
        node.ticket = 0