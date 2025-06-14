import matplotlib.pyplot as plt

#%%
# x-y data
distance = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
field_strength = [400.2, 100.05, 44.47, 25.0125, 
                  16.008, 11.12, 8.17, 6.25, 4.9, 4.002]

#%%
# Plot data points and line
plt.plot(distance, field_strength, 'x')
plt.plot(distance, field_strength)  

# Labels and title
plt.xlabel("Distance from Earth's center [10^6 m]")  
plt.ylabel("Gravitational field strength [m/s^2]")  
plt.title("Gravitational Field Strength vs Distance")  

# Show graph
plt.grid()
plt.show()


  