# This function does not return a value. Is it still a useful function?
def print_doc(number, item):
    print("Item", number, "is a", item)

items = ["guitar", "piano", "trumpet", "drum", "trombone"]

for i in range(len(items)):
    print_doc(i + 1, items[i])

#%%
# The following does not take an input
def give_number():
    return 45 * 678 + 23 - 7234

x = give_number()

#%%
# The following does not take an input or return a value
def hello_printer():
    print("This is an extremely long message to demonstrate "
          "that it would be much easier to call this function "
          "than to repeat this code every time.")
    
    
hello_printer()



