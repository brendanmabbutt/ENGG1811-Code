my_string = "My name is Liam and I like frogs"

#%% 
# Observe the following output
for letter in my_string:
    print(letter)

# We have seen this before; a string is basically a list!

#%%
# This does the same as above
for i in range(len(my_string)):
    print(my_string[i])

#%%
# Consider the following
file_prefix = "selection_file_"

# Try using "B" instead of "A"
file_id = "A"
file_type = ".txt"
file_name = file_prefix + file_id + file_type
with open(file_name, "r") as f:
    print(f.readline())

