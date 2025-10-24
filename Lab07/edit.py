import numpy as np
my_array = np.array([3, 4, 3, 7, 8, 9, 1, 2], dtype=float)

# Does the following also work for a list?
my_array[1:4:2] = 20

#%%
# What does the following do?
mask = my_array < 5
my_array[mask] = 0.5 / my_array[mask]
