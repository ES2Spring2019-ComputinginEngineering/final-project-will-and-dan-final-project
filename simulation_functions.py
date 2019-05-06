# -*- coding: utf-8 -*-
"""
Created on Wed Apr 17 15:33:44 2019

@author: william
"""

import numpy as np

a = np.array([["Measles", 0.90], 
              ["Flu",0.40], 
              ["Tuberculosis",0.80], 
              ["Cholera",0.70], 
              ["Ebola", 0.80]])

def severityCoeff(infect, vaccine, disease):
    diseaseCoeff = float(a[disease, 1])
    sev = diseaseCoeff - vaccine
    return sev   

def initialize_inf(pop, inf):
    sus = pop - inf
    return [[sus/pop, inf/pop, 0]]

initial_SIR = np.array(initialize_inf(100, 1))

def system_var(tc, tr):
    beta = 1 / tc
    gamma = 1 / tr
    return beta, gamma

b, g = system_var(3, 14)

def update_system(pop, beta, gamma, i, sev):
    current_pop = pop[i]
    s = current_pop[0]
    i = current_pop[1]
    r = current_pop[2]
    
    infected = beta * i * s
    recovered = gamma * i
    
    R = r + recovered
    I = (i + infected - recovered) * sev
    S = s - infected
    
    new_pop = np.array([[S, I, R]])
    
    pop = np.concatenate((pop, new_pop))
    return pop

new_pop = update_system(initial_SIR, b, g, 0)

def run_sim(pop, days):
    
    for i in range(days):
        if i == 0:
            new_pop = update_system(pop, b, g, i)
        else:
            new_pop = update_system(new_pop, b, g, i)
            
    return new_pop
        
final_pop = run_sim(initial_SIR, 7*14)

        