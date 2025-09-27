grade = float(input("What is your grade? "))

if grade < 0 or grade > 100:
    print("haha nice one")
elif grade < 50:
    print("fail")
elif grade < 85:
    print("distinction")
else:
    print("high distinction")

