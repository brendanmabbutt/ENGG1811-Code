import numpy as np

my_list = [1, 2, 3, 4, 5, 6, 7, 8]
my_array = np.array(my_list)

#%%
# This does not work 
my_list[2:5] = -1

#%%
# This works.
my_array[2:5] = -1




