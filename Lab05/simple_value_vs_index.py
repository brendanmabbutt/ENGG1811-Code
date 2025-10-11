THRESHOLD = 10

#%%
dummy_list = [23, -1, 22, -13, 58, -9, 87, 14]

    
# Loop by index
dummy_squared = [0] * len(dummy_list)
for i in range(len(dummy_list)):
    print("i is",i, "dummy_list[i] is", dummy_list[i])
    dummy_squared[i] = dummy_list[i] ** 2

# Loop by value
dummy_squared = []
for element in dummy_list:
    print("element is", element)
    dummy_squared.append(element ** 2)