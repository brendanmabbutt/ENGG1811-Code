import numpy as np

my_array = np.array([[5, 6, 7, 4, 7, 8],
                     [3, 4, 7, 5, 7, 7],
                     [0, 4, 5, 3, 2, 1],
                     [3, 8, 10, 10, 6, 5],
                     [5, 6, 7, 7, 4, 3]])

# Try the following 
bool_array_1 = my_array > 5
bool_array_2 = my_array < 3

a = ~bool_array_2
a_log = np.logical_not(bool_array_2)

b = bool_array_2 & bool_array_1
b_log = np.logical_and(bool_array_1, bool_array_2)

c = bool_array_2 | bool_array_1
c_log = np.logical_or(bool_array_1, bool_array_2)  


