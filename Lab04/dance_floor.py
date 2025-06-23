import math as m

x = float(input("Give me a float: "))

floor = m.floor(x)
ceil = m.ceil(x)
decimal_part = x - floor
min_distance = min(abs(x - ceil), abs(x - floor))

print("\nYou gave the number", x,
      "\nThe smallest integer no greater than x is", floor,
      "\nThe largest integer no less than x is", ceil,
      "\nThe decimal part of x is", decimal_part,
      "\nThe distance to the nearest integer is", min_distance)
