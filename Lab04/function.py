#%%
def square_plus_cube(num): 
    square = num ** 2 
    cube = num ** 3 
    answer = square + cube 
    return answer

#%%
# What will the following do?
a = square_plus_cube(-1)
b = square_plus_cube(2)
c = square_plus_cube(7)

#%%
# What will the following do?
num = 2
d = square_plus_cube(num)

#%%
# Can I pass in a differently named variable?
dummy = 4
e = square_plus_cube(dummy)

#%%
# What is the error here?
print(cube)

#%%
# Is there any problem with doing something like this?
square = 4 * 4