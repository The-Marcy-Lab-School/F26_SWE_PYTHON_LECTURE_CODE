letters = ['a', 'b', 'c']

# Two ways to copy:
copy1 = list(letters)   # the list() function builds a new list from any sequence
copy2 = letters[:]      # a slice with no start or end creates a copy of the whole thing


# With a copy, apply_discount changes only its own list and returns it
def apply_discount(prices):
    sale_prices = list(prices)
    for i in range(len(sale_prices)):
        sale_prices[i] = sale_prices[i] - 1
    return sale_prices

prices = [3.50, 2.25, 4.00]
sale_prices = apply_discount(prices)

print(prices)       # [3.5, 2.25, 4.0]
print(sale_prices)  # [2.5, 1.25, 3.0]
