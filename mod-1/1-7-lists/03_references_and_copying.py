# Uncomment one section at a time as the lesson goes on.
#
# items ──► [ slot 0 | slot 1 | slot 2 | slot 3 ]
#               │        │        │        │
#               ▼        ▼        ▼        ▼
#           'coffee'  'bagel'  'juice'  'muffin'

items = ['coffee', 'bagel', 'juice', 'muffin']
prices = [3.50, 2.25, 4.00, 3.00]


# ---------- A List Is a Row of References ----------
# The id() function returns a number that identifies where a value lives.

# receipt = items
#
# print(id(items))        # some large number, like 4395782592
# print(id(receipt))      # the exact same number
# print(items is receipt) # True: `is` asks whether two variables reference the same object


# ---------- Two Names, One List ----------
# Predict, then run: What will items and receipt hold after this runs?

# items = ['coffee', 'bagel', 'juice', 'muffin']
# receipt = items
# receipt[1] = 'scone'
#
# print(items)
# print(receipt)


# ---------- Passing a List to a Function ----------
# Predict, then run: The function never mentions the variable items. Does items change?

# def clear_receipt(receipt_items):
#     receipt_items.clear()
#
# items = ['coffee', 'bagel', 'juice', 'muffin']
# clear_receipt(items)
# print(items)

# A function can never change a caller's number this way. You can reassign a variable, but you cannot mutate the number itself.
# def add_one_and_print(x):
#     x += 1  # shorthand for x = x + 1
#     print(x)
#
# my_num = 10
# add_one_and_print(my_num)  # 11
# print(my_num)  # 10


# ---------- Copying a List Before Changing It ----------
# Predict, then run: The receipt should show each item's regular price next to its sale price.
# What happened to the regular prices?

# def apply_discount(prices):
#     for i in range(len(prices)):
#         prices[i] = prices[i] - 1
#     return prices
#
# prices = [3.50, 2.25, 4.00, 3.00]
# sale_prices = apply_discount(prices)
#
# print(prices)
# print(sale_prices)

# Two ways to copy, and apply_discount rewritten to change only its copy
# prices = [3.50, 2.25, 4.00, 3.00]
# copy1 = list(prices)   # the list() function builds a new list from any sequence
# copy2 = prices[:]      # a slice with no start or end creates a copy of the whole thing
#
# def apply_discount(prices):
#     sale_prices = list(prices)
#     for i in range(len(sale_prices)):
#         sale_prices[i] = sale_prices[i] - 1
#     return sale_prices
#
# sale_prices = apply_discount(prices)
# print(prices)       # [3.5, 2.25, 4.0, 3.0]
# print(sale_prices)  # [2.5, 1.25, 3.0, 2.0]


# ---------- Copying List Challenge ----------
# This function changes the list it is given. Rewrite it so that the caller's list stays the same!

# def shorten(items):
#     items.pop()
#     return items
#
# items = ['coffee', 'bagel', 'juice', 'muffin']
# shorter_items = shorten(items)
#
# print(items)          # should print ['coffee', 'bagel', 'juice', 'muffin']
# print(shorter_items)  # should print ['coffee', 'bagel', 'juice']
