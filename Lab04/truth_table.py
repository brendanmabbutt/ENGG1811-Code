print("For De Morgan's Law:\n"
      "not(X and Y) = not(X) or not(Y),\n"
      "we test all possible cases:\n")

# Flag to track if all required conditions are satisfied
holds = True
booleans = [True, False]

for x in booleans:
    for y in booleans:
        if (not(x) or not(y)) != (not(x and y)):
            print("De Morgan's Law fails when X is", x, "and Y is", y)
            holds = False
        else:
            print("De Morgan's Law holds when X is", x, "and Y is", y)

if not(holds):
    print("\nDe Morgan's Law does not hold")
else:
    print("\nDe Morgan's Law does hold")
