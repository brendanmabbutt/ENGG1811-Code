# Example of debugging using placement of print functions
global_variable = 0
SIZE = 30

for i in range(30):
    global_variable = (i + i * global_variable) % SIZE
    print("On iteration", i, "global_variable =", global_variable)

# Make sure you remove your print statements after you have finished
# your function for the assignment!
