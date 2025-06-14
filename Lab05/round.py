# In binary, 0.7 has a repeating sequence of digits, and in Python, this 
# has to be rounded when stored, as computers have finite memory, 
# which is represented as a sequence of 1s and 0s (binary numbers).
x = 0.7 * 39

# 0.4 also has a repeating sequence of digits in binary.
# Why do you think the following results are different?
y_floor = 20 // 0.4  
y_normal = 20 / 0.4 
