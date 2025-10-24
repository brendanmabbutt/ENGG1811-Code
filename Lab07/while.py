i = 100
dec = 3
  
# Think about what the following does.
while (i >= 0):
    print(i)
    
    if dec == 0: 
        dec = 3
    i -= dec
    dec -= 1