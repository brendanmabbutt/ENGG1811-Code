# 1: What data type is x?
x = range(5)

# For the following, try playing around with these
start = 2
stop = 17
step = 3

#%%
# 2: What will this print?
for i in range(start, stop, step):
    print(i)

#%%
# 3: What will the following print?
for i in range(stop):
    print(i)

#%%
# 4: What will the following print?
for i in range(start, stop):
    print(i)

#%%
# Why will the following not work as intended?
for i in range(stop, step):
    print(i)
   
#%%
# Why does the following give an error?
for i in range(start, stop, 0.5):
    print(i)