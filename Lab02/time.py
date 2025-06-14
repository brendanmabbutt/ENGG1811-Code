"""
!GOOD STYLE!

Purpose: To find the number of full years and then leftover days, hours, and 
minutes in a given amount of minutes.

Author:  Brendan Mabbutt

Date:    22/02/25

Method: First, we will find the full number of years using integer division
by converting units. Then, we will determine the leftover days, hours, and 
minutes by calculating the total amount of each respective unit using integer 
division and then taking the modulus of the conversion to the next unit up. 
The results are then printed.

Data dictionary:
    [int] MINUTES_IN_HOUR  The number of minutes in an hour
    [int] HOURS_IN_DAY     The number of hours in a day
    [int] DAYS_IN_YEAR     The number of days in a year
    [int] time             The total number of minutes
    [int] years            The total number of years
    [int] days             The number of leftover days
    [int] hours            The number of leftover hours
    [float] minutes          The number of leftover minutes
"""

MINUTES_IN_HOUR = 60
HOURS_IN_DAY = 24
DAYS_IN_YEAR = 365

time = 2 * 10 ** 6

# Full years
years = time // (MINUTES_IN_HOUR * HOURS_IN_DAY * DAYS_IN_YEAR)
 
# Leftover time
days = time // (MINUTES_IN_HOUR * HOURS_IN_DAY) % DAYS_IN_YEAR
hours = time // MINUTES_IN_HOUR % HOURS_IN_DAY
minutes = time % MINUTES_IN_HOUR

# aligning to open bracket
print(time, "minutes is", years, "years", 
      days, "days", hours, "hours, and", minutes, "minutes")




