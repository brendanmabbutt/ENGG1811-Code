short_alph = ["a", "b", "c", "d", "e"]

# # %% While loop
# print("While loop:")

i = 0
while i < len(short_alph) and short_alph[i] != "d":
    print(short_alph[i])
    i += 1

# # %% The same loop using a for loop by index
# print("For loop (by index):")

# for i in range(len(short_alph)):
#     print(short_alph[i])

# # %% The same loop using a for loop by value
# print("For loop (by value):")

# for value in short_alph:
#     print(value)
