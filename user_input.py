# -*- coding: utf-8 -*-
"""
Created on Mon Apr 22 15:00:22 2019

@author: danie
"""

def userInput():
    print("Welcome to the Epidemic Simulator.\nInput your values for the following variables.")
    pop = int(input("Total population: "))
    infect = int(input("Initial infected: "))
    vaccine = float(input("Percentage of population vaccinated (Enter as decimal): "))
    disease = int(input("Type of disease:\n[0] Measles\n[1] Flu\n[2] Tuberculosis\n[3] Cholera\n[4] Ebola\nEnter a number for the disease you want: "))
    days = input("How many days do you want to model: ")
    
    return pop, infect, vaccine, disease, days

pop, infect, vaccine, disease, days = userInput()

