"""
Purpose: Demonstration of Boolean variables

Date: 02/03/25

Author: Brendan Mabbutt

Method: Assign Boolean expressions to variables and use Boolean conjunctives  
        to demonstrate their uses.

Data Dictionary:
    [boolean] dummy  
    Arbitrary Boolean variable used for demonstration.  

    [boolean] other  
    Another arbitrary Boolean variable.
"""

# Using names like "dummy" is considered bad practice,  
# but it is used here to indicate that the name is arbitrary.
dummy = True

# 1: What will the following statement do?
dummy = False

# 2: What will the following statement do?
dummy = not(dummy)

# 3: What will the following statement do?
other = dummy or not(dummy)

# 4: What will the following statement do?
other = dummy and not(dummy)

# What will happen when this runs? What if "dummy" is changed?
if dummy:
    print("Hello")