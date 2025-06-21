import math 

NUM_ITEMS = 10

# In the variable explorer, look at the difference between x and y
x = [i for i in range(NUM_ITEMS)]
y = range(NUM_ITEMS)

# What does this do?
z = [element ** element for element in x]

def long_calculation(number):
    return math.cos(number) ** 3 - math.pi * number \
           + math.sin(math.cos(2 * number - math.pi / 2))
     
# What does this do?
w = [long_calculation(dummy) for dummy in x]
