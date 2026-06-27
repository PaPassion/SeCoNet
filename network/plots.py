from matplotlib import pyplot as plt
import numpy as np
from collections import Counter
from scipy.optimize import curve_fit

def network_dynamics(m, total_links, duration, nodes, links):
    fig = plt.figure("network")
    plt.plot(nodes, label = 'nodes')
    plt.plot(links, label = 'links')
    plt.title('m = {}, total links ={}, actual duration = {:.2f} '.format(m, total_links, duration))
    plt.legend()
    return fig

def line_function(x, a, b):
    return -a * x + b

def r_squared(original, expectation):
    residuals = [(original[i] - expectation[i]) ** 2 for i in range(len(original))]
    numerator = sum(residuals)
    average = sum(original) / len(original)
    variance = [(x - average) ** 2 for x in original]
    denominator = sum(variance)
    return 1 - numerator / denominator

def fitting(m, epsilon, nodes):
    #degree distribution
    distribution = [len(node.neighbors) for node in nodes]
    result = Counter(distribution)
    keys = sorted(result.keys())[1:]
    values = [result[key] for key in keys]
    sum_values = sum(values)
    values = [value / sum_values for value in values]

    #log log distribution
    log_degree = np.log(keys[1:])
    log_proportion = np.log(values[1:])


    #power law fitting
    xdata = np.array(log_degree)
    ydata = np.array(log_proportion)
    popt, pcov = curve_fit(line_function, xdata, ydata)
    fitted_results = line_function(xdata, *popt)

    #plot
    fig = plt.figure("power law")
    plt.plot(xdata, ydata, 'x', label='data')
    plt.plot(xdata, fitted_results, label = "fit: -{:.2f} * x + {:.2f}, $r^2$ = {:.2f}%".format(*popt, r_squared(ydata, fitted_results) * 100))
    plt.title('m = {} epsilong = {}'.format(m, epsilon))
    plt.legend()
    return fig

