# In days
soon_threshold = 2
# Assignment due date (in April)
DUE_DATE = 25
current_date = 24

assignment_due_soon = abs(current_date - DUE_DATE) <= soon_threshold

# Assumes the user enters an integer
hours_slept = int(input("How many hours did you sleep last night? "))

if hours_slept >= 10:
    print("Welcome back from hibernation")
elif hours_slept >= 7:
    print("That's a good amount of hours")
elif hours_slept >= 4:
    print("You should probably get more sleep")
elif hours_slept >= 1:
    if assignment_due_soon:
        print("You should have started the assignment earlier!")
    else:
        print("Make sure to get some good sleep tonight")
elif hours_slept == 0:
    print("How many cups of coffee have you been drinking???")
else:
    # Negative sleep
    print("I wish you the best!")