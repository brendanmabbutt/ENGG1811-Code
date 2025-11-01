import numpy as np
import math

"""
Note that this content is not explicitly covered in this week's lab, 
but there is content on it in the slides in the appendix with an exercise you can try. 
I recommend doing so since broadcasting is quite useful and elegant; understanding 
it will really help you grasp the intuition behind NumPy.
"""

#%%
# What does the following do?
cols = np.arange(0, 10)
print(np.size(cols))

rows = np.reshape(np.arange(0, 10), (-1, 1)) * 10
print(np.size(rows))

# What does the following do?
cols + rows

#%%
vector = np.array([3, 4, 5, 2, 4, 5])
scalar = 6

scalar_mult = vector * scalar

#%%
angles = np.array([0, 1, 2, 3, 4, 5])
cosines = np.cos(angles)

# Does the following work?
# cosines = math.cos(angles)

#%%
temperatures = np.array([[5, 6, 7, 900],
                         [7, 180, 2, 3],
                         [1, 2, 400, 5]])

threshold = 10

# Excluding outliers
temps_under_threshold = temperatures * (temperatures < threshold)

#Find the average temperature of each column for those under the threshold
averages_under_threshold = np.sum(temps_under_threshold, axis=0) \
                           / np.sum(temperatures < threshold, axis=0)

# Compare this with the following. Why don't they work?
# np.mean(temps_under_threshold, axis=0)
# np.mean(temps_under_threshold[temperatures < threshold], axis=0)
