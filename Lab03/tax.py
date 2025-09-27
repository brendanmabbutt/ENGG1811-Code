"""
Income thresholds    Rate    Tax payable on this income
$0 – $18,200         0%      Nil
$18,201 – $45,000    19%     16c for each $1 over $18,200
$45,001 – $135,000   30%     $4,288 plus 30% of amounts over $45,000
$135,001 – $190,000  37%     $31,288 plus 37% of amounts over $135,000
$190,001 and over    45%     $51,638 plus 45% of amounts over $190,000
"""

import matplotlib.pyplot as plt

NUMBER_BRACKETS = 5

#%%
thresholds = [0, 18200, 45000, 135000, 190000]
tax = [0, 0, 4288, 31288, 51638]
tax_rates = [0, 0.16, 0.30, 0.37, 0.45] 

income_range = 200000

# You don't need to understand what this does yet
thresholds.append(income_range)
tax.append(tax[-1] + (income_range - thresholds[-2]) * tax_rates[-1])

#%%
# Plot data points and line
plt.plot(thresholds, tax)
plt.plot(thresholds, tax, 'x')

# Labels and title
plt.xlabel("Income (Dollars)")  
plt.ylabel("Tax (Dollars)")  
plt.title("Tax vs Income")  

# Show graph
plt.grid()
plt.show()


#%%
# You don't need to understand how this works yet
income = float(input("Please enter your income (in dollars): "))

i = 0
while i < NUMBER_BRACKETS and income > thresholds[i]:
    i += 1

income_tax = (income - thresholds[i - 1]) * tax_rates[i - 1] + tax[i - 1]
print("Your tax is", income_tax, "dollars")


