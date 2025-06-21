#%%
def squarepluscube(num): 
    square = num ** 2 
    cube = num ** 3 
    answer = square + cube 
    return answer

#%%
# What will the following do?
a = squarepluscube(-1)
b = squarepluscube(2)
c = squarepluscube(7)

#%%
# What will the following do?
num = 2
d = squarepluscube(num)

#%%
# Can I pass in a differently named variable?
dummy = 4
e = squarepluscube(dummy)

#%%
# What is the error here?
print(cube)

#%%
# Is there any problem with doing something like this?
square = 4 * 4