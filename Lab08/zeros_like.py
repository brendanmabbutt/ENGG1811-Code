import numpy as np

x_values = np.array([1, 2, 5, 3, 5, 6])

print(np.zeros_like(x_values, dtype=int))
print(np.zeros_like(x_values, dtype=float))
