# Represents the quadratic x^2 + 5x + 6
constant_term = 6
linear_term = 5
quadratic_term = 1

# b^2 - 4ac
discriminant = linear_term ** 2 \
               - 4 * quadratic_term * constant_term
               
root_one = 1/(2 * quadratic_term) \
           * (- linear_term + discriminant ** (1/2))
root_two = 1/(2 * quadratic_term) \
           * (- linear_term - discriminant ** (1/2))
    
print("My roots are " + str(root_one) + " and " + str(root_two))