import numpy as np

my_array = np.array([[5, 6, 7, 4, 7, 8],
                     [3, 4, 7, 5, 7, 7],
                     [0, 4, 5, 3, 2, 1],
                     [3, 8, 10, 10, 6, 5],
                     [5, 6, 7, 7, 4, 3]])

# Get the first and third rows and the fourth and fifth columns as a subarray
mask = np.ix_([0, 2], [3, 4])
my_array[mask]
my_array[1:2:1,2:4:1]