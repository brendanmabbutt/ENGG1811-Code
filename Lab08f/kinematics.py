import numpy as np
import math as m
import matplotlib.pyplot as plt

def position(time):
    return m.sin(time) * time ** 2 - m.exp(-time) * time \
           + 20 * time * m.cos(time)

#%%
times = np.arange(0, 15, 0.2)

# Computation of the particle's position at each time instance
positions = [position(x) for x in times]

#%%
plt.plot(times, positions)
plt.xlabel("Time (s)")
plt.ylabel("Position (m)")
plt.title("Plot of position of particle with respect to time")
plt.grid(True)
plt.show()

#%%
velocities = np.diff(positions)
max_speed = np.max(np.abs(velocities))
# Ignoring the last time since there is no next value
# Increasing in the sense of the value compared to the next
increasing_times = times[0:-1][velocities > 0]


