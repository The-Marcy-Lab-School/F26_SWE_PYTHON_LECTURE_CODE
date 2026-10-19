# enumerate() produces an (index, item) pair on each pass, and the loop unpacks it into two variables.
# This is the receipt loop again.

items = ['coffee', 'bagel', 'juice', 'muffin']
prices = [3.50, 2.25, 4.00, 3.00]

for index, item in enumerate(items):
    print(f"{item}: ${prices[index]:.2f}")
