from matplotlib import pyplot as plt
import numpy as np
from collections import Counter
from scipy.optimize import curve_fit

def network_dynamics(m, links, duration, nodes, active_links):
    fig = plt.figure("network")
    plt.plot(nodes, label = 'nodes')
    plt.plot(active_links, label = 'links')
    plt.title('m = {}, total links ={}, actual duration = {:.2f} '.format(m, links, duration))
    plt.legend()
    # plt.style.use(['science', 'ieee'])
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

def fitting(m, nodes):
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
    plt.title('m = {}'.format(m))
    plt.legend()
    return fig

def general_sir(susceptible, infected, recovered):

    fig = plt.figure("sir dynamics")
    ticks = np.arange(len(susceptible))

    plt.plot(ticks, susceptible, label = 'susceptible', color = '#4068b2')
    plt.plot(ticks, infected, label = 'infectious', color = '#ee716d')
    plt.plot(ticks, recovered, label = 'recovered', color = '#428b2c')
    plt.xlabel('time')
    plt.ylabel('population')
    plt.legend()
    plt.title('HPV-16 Transmission Dynamics')
    return fig

def gender_sir(female_susceptible, female_infected, female_recovered, male_susceptible, male_infected, male_recovered):
    fig, ax = plt.subplots(nrows=1, ncols=2, sharey=True, squeeze=False)
    ticks = np.arange(len(female_susceptible))

    ax[0][0].plot(ticks, female_susceptible, label='susceptible', color='#4068b2')
    ax[0][0].plot(ticks, female_infected, label='infectious', color='#ee716d')
    ax[0][0].plot(ticks, female_recovered, label='recovered', color='#428b2c')
    ax[0][0].set_xlabel('time')
    ax[0][0].set_ylabel('population')
    ax[0][0].title.set_text('female')

    ax[0][1].plot(ticks, male_susceptible, label='susceptible', color='#4068b2')
    ax[0][1].plot(ticks, male_infected, label='infectious', color='#ee716d')
    ax[0][1].plot(ticks, male_recovered, label='recovered', color='#428b2c')
    ax[0][1].set_xlabel('time')
    ax[0][1].set_ylabel('population')
    ax[0][1].title.set_text('male')
    plt.legend()
    plt.suptitle('Gender-specific Transmission Dynamics')
    return fig

def cumulative_incidence(cumulative, female_cumulative, male_cumulative):
    fig = plt.figure('incidences')
    ticks = np.arange(len(cumulative))

    plt.stackplot(ticks, [female_cumulative, male_cumulative],
                                          labels=['female', 'male'], colors=['#f8c4c2', '#f4a09d'])
    plt.plot(ticks, cumulative, label='general', color='#ee716d')
    plt.xlabel('time')
    plt.ylabel('incidences')
    plt.legend()
    plt.title('HPV-16 Cumulative Incidences')
    return fig
