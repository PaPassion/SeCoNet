import random

female_immunity = 0.427
male_immunity = 0.188

def update_links(links, day):
    left_links = []
    for link in links:
        link.length += 1
        if link.length < link.duration:
            left_links.append(link)
            if link.length == 14:
                link.frequency = 1/7
        else:
            female = link.female
            male = link.male
            female.neighbors.remove(male)
            male.neighbors.remove(female)
            link.end = day

    return left_links, len(links) - len(left_links)

def update_neighbors(node0,node1):
    node0.newbie = 1
    node0.neighbors.append(node1)
    node0.sp += 1

    node1.newbie = 1
    node1.neighbors.append(node0)
    node1.sp += 1

def update_nodes(nodes, day):
    group = [node for node in nodes if node.newbie == 1]

    for node in group:
        if node.status > 0:
            node.duration += 1
        if node.duration == node.clearance and node.status > 0:
            r = random.random()
            if node.sex == 1:
                if r <= female_immunity:
                    node.status = 0 - node.status
                    node.duration = -1
                else:
                    node.status = 0
                    node.duration = 0
            else:
                if r <= male_immunity:
                    node.status = 0 - node.status
                    node.duration = -1
                else:
                    node.status = 0
                    node.duration = 0
    if day % 365 == 0:
        node.age += 1
