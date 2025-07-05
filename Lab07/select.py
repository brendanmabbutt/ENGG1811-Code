import numpy as np

#%%
# Selecting multiple indices at once
animals = np.array(['cat', 'dog', 'mouse', 'hyena', 
                    'elephant', 'giraffe', 'bear', 'rhinoceros'])

# Select elements at indices 1, 3, and 4
selected_animals = animals[[1, 3, 4]]

# Alternatively, do:
important_animals = np.array([1, 3, 4])
selected_animals = animals[important_animals]

#%%
# Creating a NumPy array with sample data
data = np.array([
    [5, 6, 7, 4, 700000, 8],
    [3, 100000, 7, 5, 7, 7],
    [0, 4, 5, 3, 200000, 1],
    [3, 8, 10000, 10, 6, 5],
    [500000, 6, 7, 7, 4, 3]
])

# Selecting specific elements using row and column indices
rows = np.array([0, 1, 2, 3, 4])
columns = np.array([4, 1, 4, 2, 0])
selected_values = data[rows, columns]

