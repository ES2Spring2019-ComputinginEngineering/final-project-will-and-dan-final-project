
# Simulating the Spread of an Epidemic

This project simulates an epidemic by taking data inputted by the user and calculating the ratios over time of three population groups: Susceptible, Infected, and Recovered. A graph and table displays the data.

## Instructions

When main.py is open, run the program. It will prompt you for the following data:

- Total population
- Initial infected population
- Type of community
- Type of disease
- Number of days simulated

Enter in the desired simulation data, and after the days are inputted a graph and table will appear. The graph displays the ratios of groups as time advances, and the table shows the exact percentages. 
We recomend that you use at least a 100 person population and run the simulation for around 200 days to give a complete view of the disease over its course throughout the epidemic.

## File List

- main.py: The main function that calls other functions
- user_input.py: The function where the user inputs initial data
- simulation_functions.py: Function that calculates infection and recovery rates, and the ratios along time
- graph_functions.py: Function that graphs the data and displays table

## Features
- Libraries
  - numpy arrays
  - panda DataFrames
- Methods
  - Solving systems of linear equations
  - Using descriptive statistics
  - Extrapolation
