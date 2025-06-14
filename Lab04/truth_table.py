print("For De Morgan's Law:\n"
      "not(X and Y) = not(X) or not(Y),\n"
      "we test all possible cases:\n")

holds = True
for x in [True, False]:
    for y in [True, False]:
        if (not(x) or not(y)) != (not(x and y)):
            print("De Morgan's Law fails when X is", x, "and Y is", y)
            holds = False
        else:
            print("De Morgan's Law holds when X is", x, "and Y is", y)

if not(holds):
    print("\nDe Morgan's Law does not hold")
else:
    print("\nDe Morgan's Law does hold")
