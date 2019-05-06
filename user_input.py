# -*- coding: utf-8 -*-
"""
Created on Mon Apr 22 15:00:22 2019

@author: danie
"""
#This purpose of this program is to allow for user interaction with the simulation
def userInput():
    print("Welcome to the Epidemic Simulator.\nInput your values for the following variables.")
    pop = int(input("Total population: "))
    infect = int(input("Initial infected: "))
    contactTime = int(input("Type of community:\n[0] Urban\n[1] Suburban\n[2] Rural\nEnter a number:"))
    disease = int(input("Type of disease:\n[0] Measles\n[1] Flu\n[2] Tuberculosis\n[3] Cholera\n[4] Ebola\nEnter a number: "))
    days = int(input("How many days do you want to model: "))
    
    return pop, infect, contactTime, disease, days
