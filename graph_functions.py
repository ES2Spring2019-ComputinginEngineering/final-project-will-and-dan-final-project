# -*- coding: utf-8 -*-
"""
Created on Sun Apr 21 18:13:04 2019

@author: william
"""

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from simulation_functions import initialize_inf, run_sim

def graph_data(pop, inf, days):
    initial_SIR = np.array(initialize_inf(pop, inf))
    final_pop = run_sim(initial_SIR, days)
    
    S = final_pop[:,0]
    I = final_pop[:,1]
    R = final_pop[:,2]
    
    plt.figure()
    plt.title("Infection Spread Summary")
    plt.plot(S, '--', label= 'Susceptible')
    plt.plot(I, ':', label= 'Infected')
    plt.plot(R, '-', label= 'Recovered')
    plt.legend(loc = 'upper right')
    plt.xlabel('Days')
    plt.ylabel('Population Percent')
    plt.show()

graph_data(100, 1, 200)

initial_SIR = np.array(initialize_inf(100, 1))
final_pop = run_sim(initial_SIR, 150)

def table_data(data):
    pd.DataFrame(data=data[0:,0:])
    
print(table_data(final_pop))