# Predict, then run: The receipt should show each item's regular price next to its sale price.
# What do the two print statements show? What happened to the regular prices?

def apply_discount(prices):
    for i in range(len(prices)):
        prices[i] = prices[i] - 1
    return prices

prices = [3.50, 2.25, 4.00]
sale_prices = apply_discount(prices)

print(prices)
print(sale_prices)
