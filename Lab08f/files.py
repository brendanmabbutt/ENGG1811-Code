import numpy as np

FILE_LINES = 3

#%%
# Method A
with open("text_file.txt", "r") as f:
    lines = f.readlines()

data = []
for line in lines:
    data.append(line.split())

print("Data by Method A:", data)

#%%
# Method B
data = []

with open("text_file.txt", "r") as f:
    for i in range(FILE_LINES):
        data.append(f.readline().split())

print("Data by Method B:", data)

#%%
# Method C
# This simple method does not work if the data is not well-structured
data = np.loadtxt("text_file.txt", dtype=str)
print("Data by Method C:", data)

# The following does not work because of poorly structured data
# np.loadtxt("not_nice_data.txt", dtype=str)
