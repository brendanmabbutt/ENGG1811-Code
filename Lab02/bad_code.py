# Example of bad code for time.py
MINUTES_IN_HOUR=60
HOURS_IN_DAY=24
DAYS_IN_YEAR=365
time=1*10**6
years=time//(MINUTES_IN_HOUR*HOURS_IN_DAY*DAYS_IN_YEAR)
days=(time//(MINUTES_IN_HOUR*HOURS_IN_DAY))%DAYS_IN_YEAR
hours=(time//MINUTES_IN_HOUR)%HOURS_IN_DAY
minutes=time%MINUTES_IN_HOUR
print(time,"minutes is",years,"years",days,"days",hours,"hours,and",minutes,"minutes")

