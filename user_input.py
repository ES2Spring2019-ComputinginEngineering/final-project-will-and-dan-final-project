# -*- coding: utf-8 -*-
"""
Created on Mon Apr 22 15:00:22 2019

@author: danie
"""
import numpy as np

import tkinter as tk

def userInput():
    pop = int(input("Total population: "))
    infect = int(input("Initial infected: "))
    vaccine = float(input("Percentage of population vaccinated (Enter as decimal): "))
    disease = input("Type of disease: ")
    
    return pop, infect, vaccine, disease

def severityCoeff(infect, vaccine, disease):
    diseaseCoeff = a[disease, 1]
    infectCoeff = 0.05 * infect
    sev = diseaseCoeff + infectCoeff - vaccine
    return sev
    
pop, infect, vaccine, disease = userInput()
a = np.array([["Measles", 0.90], ["Flu",0.40], ["Tuberculosis",0.80], ["Cholera",0.70], ["Ebola", 0.80]])
sev = severityCoeff(infect, vaccine, disease)