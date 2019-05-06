"""This is the python file that your instructors will run to test your code
make sure it runs correctly when someone downloads your repository. You 
might want to test this on a classmates computer to be sure it works!"""

# This files should not contain any function defitions


# IMPORT STATEMENTS
import numpy as np
from simulation_functions import initialize_inf, run_sim, environmentInfo, system_var
from graph_functions import graph_data, table_data
from user_input import userInput

# DEMONSTRATION CODE
pop, infect, tc, disease, days = userInput()

tc, tr = environmentInfo(tc, disease)
b, g = system_var(tc, tr)

graph_data(pop, infect, days, tc, tr)

initial_SIR = np.array(initialize_inf(pop, infect))
final_pop = run_sim(initial_SIR, days, b, g)
print(table_data(final_pop))