import numpy as np

array = np.array([[1, 2, 3, 4],
                  [5, 6, 7, 8],
                  [9, 10, 11, 12]])

#%% What does the following do?
array[1, 2] = -1

#%% What does the following do?
array[1:3, 1:4] = -1

#%% What does the following do?
array[:2, :2] = np.array([[-1, -2], [-3, -4]])
