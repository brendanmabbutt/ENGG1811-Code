# Good coding style, such as using constants, isn't strictly necessary in 
# exams, but it helps make things clearer so that partial marks may be more 
# easily awarded.  
EASY_TIME = 4
HARD_TIME = 8
EASY_HEIGHT = 200
HARD_HEIGHT = 600

def q1_func(d, h, s):
    # Ensure s and d are strictly positive, and h is non-negative  
    if s <= 0 or d <= 0 or h < 0:
        return "invalid"
   
    time = d / s + h / 400

    if time < EASY_TIME and h < EASY_HEIGHT:
        return "Easy"
    elif time > HARD_TIME or h > HARD_HEIGHT:
        return "Hard"
    
    return "Medium"

    