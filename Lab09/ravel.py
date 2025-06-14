import numpy as np

my_array = np.array([[7, 8, 3, 4], 
                     [9, 23, 2, 1], 
                     [3, 2, 1, 8]])

# Compare the output of the following
np.ravel(my_array)
np.reshape(my_array, np.size(my_array))
np.reshape(my_array, -1)
