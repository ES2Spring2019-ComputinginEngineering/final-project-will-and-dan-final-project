"""This is the python file that your instructors will run to test your code
make sure it runs correctly when someone downloads your repository. You 
might want to test this on a classmates computer to be sure it works!"""

# This files should not contain any function defitions


# IMPORT STATEMENTS

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from simulation_functions import initialize_inf, run_sim
from graph_functions import graph_data, table_data
from user_input import userInput, severityCoeff

# DEMONSTRATION CODE
pop, infect, vaccine, disease, days = userInput()
graph_data(pop, infect, days)
initial_SIR = np.array(initialize_inf(pop, infect))
final_pop = run_sim(initial_SIR, days)
print(table_data(final_pop))