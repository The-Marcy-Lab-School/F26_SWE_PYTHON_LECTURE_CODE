# The bagel on the receipt is on sale. A list can be changed in place.

prices = [3.50, 2.25, 4.00, 3.00]
prices[1] = 1.75
print(prices)  # [3.5, 1.75, 4.0, 3.0]

# We can even empty a list in one go
prices.clear()  # prices now has no values
print(prices)  # []
