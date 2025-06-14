# A program to find the number of consecutive even numbers in a list

# A flag initialized to indicate whether the previous element is even, 
# set to False as there is no previous element initially
even_flag = False

integer_list = [2, 3049, 4, 45212, 278, 27, 3, 2, 231, 25, 94, 30, 75]

number_even = 0
for number in integer_list:
    # If the number is even
    if number % 2 == 0:
        if even_flag:
            number_even += 1
        even_flag = True
    else:
        even_flag = False
