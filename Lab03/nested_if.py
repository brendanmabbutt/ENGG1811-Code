number = int(input("Give me an integer: "))

if number % 2 == 0:
    if number % 3 == 0:
        print("Your number is divisible by both 2 and 3.")
    else:
        print("Your number is divisible by 2 but not by 3.")
elif number % 3 == 0:
    print("Your number is divisible by 3 but not by 2.")
else:
    print("Your number is divisible by neither 2 nor 3.")
