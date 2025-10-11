THRESHOLD = 10

#%%
dummy_list = [23, -1, 22, -13, 58, -9, 87, 14]

# Loop by index
dummy_squared = [0] * len(dummy_list)
for i in range(len(dummy_list)):
    dummy_squared[i] = dummy_list[i] ** 2

# Loop by value
dummy_squared = []
for element in dummy_list:
    dummy_squared.append(element ** 2)

# List comprehension
dummy_squared = [element ** 2 for element in dummy_list]

#%%
# How can we achieve the following using a loop by value?

positive_numbers = [2, 53, 61, 12, 9, 43, 80, 12]
product = 1
for i in range(len(positive_numbers)):
    if positive_numbers[i] % product < THRESHOLD - i:
        product *= positive_numbers[i]