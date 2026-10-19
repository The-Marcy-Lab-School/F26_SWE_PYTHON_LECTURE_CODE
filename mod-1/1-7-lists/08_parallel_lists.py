# Predict, then run: The customer changes their mind about the bagel. What does the receipt print?
# Challenge: Fix the program so that every item prints beside its own price.

items = ['coffee', 'bagel', 'juice', 'muffin']
prices = [3.50, 2.25, 4.00, 3.00]

items.remove('bagel')

for i in range(len(items)):
    print(f"{items[i]}: ${prices[i]:.2f}")
