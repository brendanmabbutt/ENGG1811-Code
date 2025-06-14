number = int(input("Give me an integer: "))

# Where possible, print the favorability of the number
if type(number) != int:
    print("The number you provided was not an integer.")
elif number % 2 == 1:
    # number is odd
    print("Your number is of the favorable type.")
else:
    print("Your choice was not favorable.")