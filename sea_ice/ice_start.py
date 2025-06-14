# Import packages
import numpy as np
import matplotlib.pyplot as plt

#%%
data_sea_ice = np.loadtxt("sea_ice.txt")
print("The shape of the numpy array is: ", data_sea_ice.shape)

#%%
print("The first row of data is \n", data_sea_ice[0,:])

#%%
years = data_sea_ice[:,0]
data_sea_ice = np.delete(data_sea_ice, 0, axis=1)  
print("The shape of the numpy array is: ", data_sea_ice.shape) 

#%%
months = np.linspace(0.5,12,24)

#%%
plt.figure(1)
plt.plot(months, np.transpose(data_sea_ice))
plt.xticks([2, 4, 6, 8, 10, 12], ["Feb", "Apr", "Jun", "Aug", "Oct", "Dec"]) 
plt.show()