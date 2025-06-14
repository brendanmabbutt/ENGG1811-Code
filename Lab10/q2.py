# Import NumPy
import numpy as np 

#%%
def q2_func(x, y):
    #==========================================================================
    # Method 1
    # In the exam, there may be questions involving NumPy where you can't  
    # get the maximum marks possible by using loops. Methods 2 and 3 are  
    # clearer regardless. This method is only advised if other approaches  
    # cannot be thought of.  
    #
    # z = np.zeros_like(x)
    # for i in range(len(x)):
    #     if abs(x[i]) > abs(y[i]):
    #         z[i] = x[i] - y[i] / 2
    #     else:
    #         z[i] = y[i] - x[i] / 2
    #==========================================================================

    #==========================================================================
    # Method 2 (Recommended)
    mask = abs(x) > abs(y)
    z = np.zeros_like(x)
    z[mask] = x[mask] - y[mask] / 2
    z[~mask] = y[~mask] - x[~mask] / 2
    #==========================================================================

    #==========================================================================
    # Method 3
    # This method has worse readability than Method 2 and is really just  
    # showing off. Method 2 is preferred. However, since they work  
    # differently, we include this one for reference.  
    #
    # z = (abs(x) > abs(y)) * (x - y / 2) + (abs(x) <= abs(y)) * (y - x / 2)  
    #==========================================================================

    #==========================================================================
    # Method 4
    # This method is essentially the same as Method 2 but uses the additional  
    # feature of the where function.
    #
    # z = np.where(np.abs(x) > np.abs(y), x - y / 2, y - x / 2)
    #==========================================================================

    return z
