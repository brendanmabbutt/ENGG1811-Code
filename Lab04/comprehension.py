import math 

#%%
num_items = 10

# In the variable explorer, look at the difference between x and y
x = [i for i in range(num_items)]
y = range(num_items)

#%%
# What does this do?
z = []
for element in x:
    power = element ** element
    z.append(power)

# Does this do the same as above?
z = [element ** element for element in x]

#%%
def long_calculation(number):
    return math.cos(number) ** 3 - math.pi * number \
           + math.sin(math.cos(2 * number - math.pi / 2))
     
# What does this do?
w = [long_calculation(dummy) for dummy in x]
