import os
import pandas as pd

def create_folder(population, m, epsilon, repeat):
    path = 'N{}m{:.1f}epsilon{:.1f}no{}/'.format(population, m, epsilon, repeat)
    if not os.path.exists(path):
        os.mkdir(path)
    return path

def record_network(path, nodes, links, assortativity, primary, secondary, removed, avg, heterogeneity,
                   clustering, avgpath):
    dict = {'nodes': nodes, 'links': links, 'assortativity': assortativity, 'primary': primary,
            'secondary': secondary, 'removed': removed, '<k>': avg, 'heterogeneity': heterogeneity,
            'clustering': clustering, 'average_path': avgpath}
    df = pd.DataFrame(dict)
    name = "{}network.csv".format(path)
    df.to_csv(name)

def record_nodes(path, nodes):
    dict = {'id': [], 'age': [], 'sex': [], 'estimated_lsp': [], 'original_sp': [], 'final_sp': [], 'relationship': [],
            'degree': [], 'fitness': []}

    for node in nodes:
        dict['id'].append(node.id)
        dict['age'].append(node.age)
        dict['sex'].append(node.sex)
        dict['estimated_lsp'].append(node.lsp)
        dict['original_sp'].append(node.original_sp)
        dict['final_sp'].append(node.sp)
        dict['relationship'].append(node.relationship)
        dict['degree'].append(len(node.neighbors))
        dict['fitness'].append(node.fitness)
    df = pd.DataFrame(dict)

    name = "{}nodes.csv".format(path)
    df.to_csv(name)

def record_links(path, links):
    dict = {'id':[], 'female':[], 'male':[], 'start':[], 'end':[], 'duration':[]}

    for link in links:
        dict['id'].append(link.id)
        dict['female'].append(link.female.id)
        dict['male'].append(link.male.id)
        dict['start'].append(link.start)
        dict['end'].append(link.end)
        dict['duration'].append(link.duration)
    df = pd.DataFrame(dict)

    name = "{}links.csv".format(path)
    df.to_csv(name)

def record_vaccination(path, nodes, day):
    dict = {'id':[], 'age':[], 'sex':[], 'estimated_lsp':[], 'original_sp':[], 'final_sp':[], 'relationship':[],
            'degree':[], 'newbie':[]}

    for node in nodes:
        dict['id'].append(node.id)
        dict['age'].append(node.age)
        dict['sex'].append(node.sex)
        dict['estimated_lsp'].append(node.lsp)
        dict['original_sp'].append(node.original_sp)
        dict['final_sp'].append(node.sp)
        dict['relationship'].append(node.relationship)
        dict['degree'].append(len(node.neighbors))
        dict['newbie'].append(node.newbie)
    df = pd.DataFrame(dict)

    name = "{}vaccination{}.csv".format(path, day // 7)
    df.to_csv(name)

def record_stage(path, nodes):
    dict = {'id':[], 'age':[], 'sex':[], 'estimated_lsp':[], 'original_sp':[], 'final_sp':[], 'relationship':[], 'degree':[],}

    for node in nodes:
        dict['id'].append(node.id)
        dict['age'].append(node.age)
        dict['sex'].append(node.sex)
        dict['estimated_lsp'].append(node.lsp)
        dict['original_sp'].append(node.original_sp)
        dict['final_sp'].append(node.sp)
        dict['relationship'].append(node.relationship)
        dict['degree'].append(len(node.neighbors))
    df = pd.DataFrame(dict)

    name = "{}stage.csv".format(path)
    df.to_csv(name)


def record_nodes0(path, nodes):
    dict = {'id': [], 'age': [], 'sex': [], 'estimated_lsp': [], 'original_sp': [], 'final_sp': [], 'relationship': [],
            'degree': [], 'fitness': [], 'newbie':[]}

    for node in nodes:
        dict['id'].append(node.id)
        dict['age'].append(node.age)
        dict['sex'].append(node.sex)
        dict['estimated_lsp'].append(node.lsp)
        dict['original_sp'].append(node.original_sp)
        dict['final_sp'].append(node.sp)
        dict['relationship'].append(node.relationship)
        dict['degree'].append(len(node.neighbors))
        dict['fitness'].append(node.fitness)
        dict['newbie'].append(node.newbie)
    df = pd.DataFrame(dict)

    name = "{}nodes0.csv".format(path)
    df.to_csv(name)

def record_nodes1(path, nodes):
    dict = {'id': [], 'age': [], 'sex': [], 'estimated_lsp': [], 'original_sp': [], 'final_sp': [], 'relationship': [],
            'degree': [], 'fitness': [], 'newbie':[]}

    for node in nodes:
        dict['id'].append(node.id)
        dict['age'].append(node.age)
        dict['sex'].append(node.sex)
        dict['estimated_lsp'].append(node.lsp)
        dict['original_sp'].append(node.original_sp)
        dict['final_sp'].append(node.sp)
        dict['relationship'].append(node.relationship)
        dict['degree'].append(len(node.neighbors))
        dict['fitness'].append(node.fitness)
        dict['newbie'].append(node.newbie)
    df = pd.DataFrame(dict)

    name = "{}nodes1.csv".format(path)
    df.to_csv(name)