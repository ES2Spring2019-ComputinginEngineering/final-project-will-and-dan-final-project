"""
Created on Wed Apr 17 15:33:44 2019

@author: william

The purpose of this program is to create the 2D array system over the course of the desired number of days.
"""
#Import Statements
import numpy as np

#Initial disease and community arrays
a = np.array([["Measles", 4], 
              ["Flu", 10], 
              ["Tuberculosis", 14], 
              ["Cholera", 3], 
              ["Ebola", 21]])

b = np.array([[0, 2],[1, 5],[2, 10]])

#Functions
def environmentInfo(tc, disease):
    recovery = int(a[disease, 1])
    contact = int(b[tc, 1])
    return contact, recovery   

def initialize_inf(pop, inf):
    sus = pop - inf
    return [[sus/pop, inf/pop, 0]]

def system_var(tc, tr):
    beta = 1 / tc
    gamma = 1 / tr
    return beta, gamma

def update_system(pop, beta, gamma, i,):
    current_pop = pop[i]
    s = current_pop[0]
    i = current_pop[1]
    r = current_pop[2]
    
    infected = beta * i * s
    recovered = gamma * i
    
    R = r + recovered
    I = i + infected - recovered
    S = s - infected
    
    new_pop = np.array([[S, I, R]])
    
    pop = np.concatenate((pop, new_pop))
    return pop


def run_sim(pop, days, b, g):
    
    for i in range(days):
        if i == 0:
            new_pop = update_system(pop, b, g, i)
        else:
            new_pop = update_system(new_pop, b, g, i)
            
    return new_pop
        