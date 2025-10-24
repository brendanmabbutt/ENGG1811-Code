#%%
# 'a' and 'b' are positional arguments; they must always be placed first.
# 'c' and 'd' are keyword arguments with default values of 4 and 5, 
# respectively.
def example_func(a, b, c=4, d=5):
    return a + b + c + d

# Define arguments
arg_a = 8
arg_b = 6
arg_c = 9
arg_d = 1

# print(example_func(arg_a, arg_b, arg_c, arg_d))
# print(example_func(arg_a, arg_b, arg_c))         
# print(example_func(arg_a, arg_b, d=arg_c))       
# print(example_func(arg_a, arg_b, d=arg_c, argc=arg_d))  
# print(example_func(arg_a, arg_b, argc=arg_c, d=arg_d))  
# print(example_func(arg_a, arg_b))
# print(example_func(arg_b, arg_c))
# print(example_func(arg_a))         
