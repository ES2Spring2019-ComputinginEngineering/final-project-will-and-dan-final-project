"""
Created on Sun Apr 21 18:13:04 2019

@author: william

The purpose of this program is to take the 2D array system from simulation_functions and graph that data
with respect to the number of days the simulation has ran. This program will also create a table that allows
for the user to see specific data points at certain times.
"""

#Import Statements
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from simulation_functions import initialize_inf, run_sim, system_var

#Functions
def graph_data(pop, inf, days, tc, tr):
    b, g = system_var(tc, tr)
    initial_SIR = np.array(initialize_inf(pop, inf))
    final_pop = run_sim(initial_SIR, days, b, g)
    
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

def table_data(data):
    
    d = {'Susceptible': data[:,0], 'Infected': data[:,1], 'Recovered': data[:,2]}
    return pd.DataFrame(data = d)
     