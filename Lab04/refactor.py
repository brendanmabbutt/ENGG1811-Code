#%%
# don't do this 
age_one = 12
if age_one < 18:
    print("child")
elif age_one < 60:
    print("adult")
else:
    print("senior")
    
age_two = 30
if age_two < 18:
    print("child")
elif age_two < 60:
    print("adult")
else:
    print("senior")
    
age_three = 90
if age_three < 18:
    print("child")
elif age_three < 60:
    print("adult")
else:
    print("senior")

#%%
#do this instead

def categorize_age(age):
    if age < 18:
        print("child")
    elif age < 60:
        print("adult")
    else:
        print("senior")
        
age_one = 12
age_two = 30
age_three = 90

categorize_age(age_one)
categorize_age(age_two)
categorize_age(age_three)
