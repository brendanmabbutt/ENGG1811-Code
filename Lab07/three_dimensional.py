import numpy as np

# Temperatures in degrees Celsius
# Heights (each rectangle), rows, columns being (z, y, x) respectively
temperatures = np.array([[[57.93, 94.61, 70.99, 45.99],
                          [41.61, 18.84, 43.39, 30.59],
                          [ 9.06, 41.59, 73.45, 34.96],
                          [33.43, 89.66, 13.23, 49.91],
                          [94.47, 16.04, 29.79, 47.99]],
                         [[64.54, 50.19, 64.67,  1.62],
                          [66.46, 20.61, 63.5 ,  2.07],
                          [23.93, 56.46, 82.25, 31.05],
                          [56.64, 15.47, 19.18, 96.14],
                          [94.04, 96.36, 71.98, 34.42]],
                         [[62.6 , 60.2 , 23.81, 42.48],
                          [42.87, 38.15, 26.85, 82.08],
                          [46.44, 17.3 , 80.2 , 70.6 ],
                          [74.87,  7.71, 92.36, 95.4 ],
                          [94.91, 33.28, 17.87, 51.33]]])

#%%
# Example of finding the temperature at (z, y, x)
x = 2
y = 2
z = 1
temperatures[z][y][x]

#%%
# Try clicking on the value box for 'temperatures' in the variable explorer.
# Have a play around with the index.

#%%
# Average temperature at each height
averages = np.mean(np.mean(temperatures, axis=2), axis=1)

# Which of the following does the same thing?
# a) averages = np.mean(np.mean(temperatures, axis=1), axis=2)
# b) averages = np.mean(np.mean(temperatures, axis=1), axis=1)
# c) averages = np.mean(np.mean(temperatures, axis=0), axis=1)
# d) averages = np.mean(np.mean(temperatures, axis=1), axis=0)