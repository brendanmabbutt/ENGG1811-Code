import numpy as np

my_array = np.array([[5, 6, 7, 4, 7, 8],
                     [3, 4, 7, 5, 7, 7],
                     [0, 4, 5, 3, 2, 1],
                     [3, 8, 10, 10, 6, 5],
                     [5, 6, 7, 7, 4, 3]])

#%%
# what does the following do?
c = my_array[::-1,::]
d = my_array[2:5:2, 1:5:3]

#%%
rows = np.arange(np.shape(my_array)[0])
cols = np.arange(np.shape(my_array)[1])


# why does the ollowing not work?
# a = my_array[cols < 2]
# b = my_array[rows < 3, cols < 2]

# why does the following work for the respective coutnerparts above?
a = my_array[:,cols < 2]
b = my_array[:3, cols < 2] 

# how would we do the last one using ix_ to get b?



