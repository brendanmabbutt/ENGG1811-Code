# Live examples

import math as m

def distance(x, y):
    z = m.sqrt(x ** 2 + y ** 2)
    return z

#print("distance gives", distance(12, 5))

def example(a, b, c):
    print("a is", a)
    print("b is", b)
    print("c is", c)
    
    z = a + b + c
    return z

#%%
def multiply(x, y):
    product = x * y
    return product

# returns (a1, b1) dot (a2, b2)
def dot_product(a1, b1, a2, b2):
    term1 = multiply(a1, a2)
    term2 = multiply(b1, b2)
    dot_product = term1 + term2
    return dot_product