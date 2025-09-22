root_alpha = 5
root_beta = 4.2
root_gamma = 5
root_delta = 40.1
root_epsilon = -2
root_zeta = -2

# aligning to equal sign 
prod_of_roots = root_alpha * root_beta * root_gamma * root_delta \
                * root_epsilon * root_zeta

#%% sum of roots two at a time 
"""
sum_roots_prod = root_alpha * root_beta + root_alpha * root_gamma \
                 + root_alpha * root_delta + root_alpha * root_epsilon \
                 + root_alpha * root_zeta + root_beta * root_gamma \
                 + root_beta * root_epsilon + root_beta * root_zeta \
                 + root_gamma * root_delta + root_gamma * root_epsilon \
                 + root_gamma * root_zeta + root_delta * root_epsilon \
                 + root_delta * root_zeta + root_epsilon * root_zeta
"""

# Brackets don't require a new line character. Compare the following to above:
#%%
"""
sum_roots_prod = (root_alpha * root_beta + root_alpha * root_gamma 
                  + root_alpha * root_delta + root_alpha * root_epsilon 
                  + root_alpha * root_zeta + root_beta * root_gamma 
                  + root_beta * root_epsilon + root_beta * root_zeta 
                  + root_gamma * root_delta + root_gamma * root_epsilon 
                  + root_gamma * root_zeta + root_delta * root_epsilon 
                  + root_delta * root_zeta + root_epsilon * root_zeta)
"""

#%%
"""
sum_roots_prod = root_alpha * (root_beta + root_gamma + root_delta \
                               + root_epsilon + root_zeta) \
                 + root_beta * (root_gamma + root_delta 
                                + root_epsilon + root_zeta) \
                 + root_gamma * (root_delta  + root_epsilon + root_zeta) \
                 + root_delta * (root_epsilon + root_zeta) \
                 + root_epsilon * root_zeta
"""                
               
               
               
               
               