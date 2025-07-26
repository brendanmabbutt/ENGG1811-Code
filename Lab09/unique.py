import numpy as np

#%%
x_vals = np.array([42, 5, 2, 23 - 3, 4, 5, 3, 2, 2, 
                   23, 5, 24, 3, 6, 32, 32, 2])
y_vals = [x ** 3 - x ** 2 for x in x_vals]

#%%
# Finding unique values and their probabilities
set_values, counts = np.unique(y_vals, return_counts=True)
probabilities = counts / np.size(y_vals)

#%%
# Calculating the mean value (the long way)
mean_val_a = np.sum(probabilities * set_values)

# Compare this with the direct mean calculation
mean_val_b = np.mean(y_vals)

#%%
# Finding the mode
mode_index = np.argmax(counts)
mode = set_values[mode_index]

# Try unpacking this calculation step by step
mode_x_orig = x_vals[np.where(y_vals == mode)[0]][0]
