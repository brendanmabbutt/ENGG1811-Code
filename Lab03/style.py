"""
Purpose: Script that provides an interface for converting degrees to radians
         and then shifting the angle by a fixed amount.

Date: 28/02/25

Name: Brendan Mabbutt

Method: Defines a constant for conversion and takes an input angle from  
        the user. It then converts the angle by multiplying it by the  
        conversion factor from degrees to radians. The result is printed  
        after applying a fixed shift.  

Data Dictionary:  
    [int] HALF_REVOLUTION  
    Number of degrees in half of a circular revolution.  

    [float] CONVERSION_FACTOR  
    Multiplication factor for converting degrees to radians, which is the 
    ratio of a circle's circumference to the degrees in a revolution.

    [float] angle_deg  
    The input angle in degrees.  

    [float] angle_rad  
    The input angle converted to radians.  

    [float] angle_shift  
    Fixed value by which the angle is shifted in radians.

    [float] shifted_angle  
    The input angle in radians after applying the shift.  
"""

import math  

# Constants for converting to radians  
HALF_REVOLUTION = 180  
CONVERSION_FACTOR = math.pi / HALF_REVOLUTION  

angle_shift = 1  

angle_deg = float(input("Enter your angle: "))  

# Converting the input angle to radians  
angle_rad = angle_deg * CONVERSION_FACTOR  

# Applying the shift and rounding the result  
shifted_angle = angle_rad + angle_shift  
print("The shifted angle in radians is", round(shifted_angle, 2))  


