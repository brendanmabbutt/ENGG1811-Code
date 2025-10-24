import numpy as np

my_list = [[ 0,  1,  2,  3,  4],
           [ 5,  6,  7,  8,  9],
           [10, 11, 12, 13, 14],
           [15, 16, 17, 18, 19]]

# same lst as a numpy array
my_array = np.array(my_list)

#%%
# Try comparing the output of the following:
my_array[1:][1:3]
my_array[1:, 1:3]

# To understand why, consider what the following returns:
x = my_array[1:]

# Then, what should the following return?
x[1:3]

# This is the same as doing:
my_array[1:][1:3]


