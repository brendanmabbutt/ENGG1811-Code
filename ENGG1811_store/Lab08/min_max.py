import numpy as np
import math as m
import matplotlib.pyplot as plt

def mapping(x):
    return -m.pi * x + m.exp(-x) + m.sin(x) * x ** 2

#%%
x_vals = np.arange(0, 10, 0.2)
y_vals = [mapping(x) for x in x_vals]

#%%
plt.plot(x_vals, y_vals)
plt.xlabel("x")
plt.ylabel("y")
plt.title("Plot of y = mapping(x)")
plt.grid(True)
plt.show()

#%%
print("Min is the point", (x_vals[np.argmin(y_vals)], np.min(y_vals)))

print("Max is the point", (x_vals[np.argmax(y_vals)], np.max(y_vals)))