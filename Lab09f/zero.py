import numpy as np

# What is the difference between the following?
np.zeros(8, dtype=int)
np.zeros(8, dtype=float)

# What does the following produce? (Feel free to skip this if you 
# are not familiar with broadcasting yet.)
np.zeros((4, 5), dtype=int) + 2
