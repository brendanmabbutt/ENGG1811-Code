#%%
# Is x permanently modified at any point?
# Does printing x at the end work?
for x in range(10):
    x += 3
    print(x)

x += 1
print(x)

#%%
my_list = ['a', 'b', 'c']

# Infinite for loop
for element in my_list:
    my_list.append('f')
    print(element)
