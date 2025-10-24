import numpy as np

#%%
my_array = np.array([[3, 5, -6, -7],
                     [3, -5, 2, -3],
                     [9, -1, 2, -7]])

# Try the following:
mask = np.where(my_array > 2)
my_array[mask]

step_func = np.where(my_array > 2, 1, 0)

#%%
forces = np.array([5.4, 2.0, 0.07, 9.09, 3.2, 10.4, 0.5])
less_than_one = np.where(forces < 1)

# Which of the following work? Why is that?
first_less_than_one = less_than_one[0]  
first_less_than_one = less_than_one[0][0]  
first_less_than_one = forces[less_than_one[0][0]]  

# Finds where the force is between 2 and 4 (inclusive)
np.where((forces >= 2) & (forces <= 4))
np.where(np.abs(forces - 3) <= 1)
np.where(np.logical_and(forces >= 2, forces <= 4))
