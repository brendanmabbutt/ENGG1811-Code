import numpy as np

#%%
# Imagine an instance of throwing a beanbag at a target, where you get 
# automatic data about a player's proximity to the target.
players = ['Anton', 'Bella', 'Charlie', 'David', 'Eva', 'Felix', 'Grace', 
           'Hannah', 'Iris', 'Jack', 'Kenny', 'Lily', 'Mason', 'Nina', 'Oscar', 
           'Paul', 'Quincy', 'Rita', 'Sam', 'Tina']
hits = np.array([20. , 13.6, 21.5, 30.2, 12.7, 12.7, 30.8, 22.7, 10.7, 20.4, 
                 10.4, 10.3, 17.4, -4.1, -2.2,  9.4,  4.9, 18.1,  5.9,  0.9])
target = 10.3

# Try to figure out how this works; it uses "broadcasting"
index_of_min = np.argmin(np.abs(hits - target))
winner = players[index_of_min]

print("The winner is", winner, "who got", hits[index_of_min], 
      "which is the closest to the target", target)


