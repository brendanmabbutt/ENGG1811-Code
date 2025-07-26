import numpy as np

# Determines whether a sequence is arithmetic 
# (progresses by a common difference)
# Think about how this works
def test_arithmetic(sequence):
    if np.size(sequence) <= 2:
        return True
    
    first_diff  = np.diff(sequence)
    second_diff = np.diff(first_diff)
    
    return np.all(second_diff == 0)

# Examples
print(test_arithmetic([2, 4, 6, 8, 10]))  
print(test_arithmetic([15, 11, 7, 3]))    
print(test_arithmetic([1, 2, 4, 8, 16]))  
print(test_arithmetic([3, 2]))    
print(test_arithmetic([5]))              
print(test_arithmetic([]))                
