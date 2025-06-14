"""
Application of Euler's forward method on the displacement x of a spring 
with respect to time t, modeled by the ODE:
    ma = -kx
where a is the acceleration, x is the displacement, k is the spring constant, 
and m is the mass of the spring. We have:
    v = v - (k/m) * x * dt
    x = x + v * dt
This updates the spring's position x and velocity v over time.
"""

import numpy as np
import matplotlib.pyplot as plt
import math as m

spring_constant = 10.2
spring_mass = 1.2

initial_velocity = 4
initial_position = 4.5

time_start = 0
time_stop = 20
time_step = 0.001
time_array = np.arange(time_start, time_stop, time_step)

time_array = np.array(time_array)
velocities = np.zeros_like(time_array)
positions = np.zeros_like(time_array)

velocities[0] = initial_velocity
positions[0] = initial_position

for i in range(len(time_array) - 1):
    dt = time_array[i + 1] - time_array[i]
    acceleration = - positions[i] * spring_constant / spring_mass
    velocities[i + 1] = velocities[i] + acceleration * dt
    positions[i + 1] = positions[i] + velocities[i] * dt

# Plotting position vs. time
plt.plot(time_array, positions)
plt.xlabel("Time (s)")
plt.ylabel("Position (m)")
plt.title("Position with Respect to Time")
plt.grid(True)
plt.show()

# Plotting velocity vs. time
plt.plot(time_array, velocities)
plt.xlabel("Time (s)")
plt.ylabel("Velocity (m/s)")
plt.title("Velocity with Respect to Time")
plt.grid(True)
plt.show()
