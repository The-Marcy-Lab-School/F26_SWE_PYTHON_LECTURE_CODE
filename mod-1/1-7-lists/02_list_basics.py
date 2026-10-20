# The receipt from 01_receipt.py, with its lists typed in so you don't have to enter them on every run.
# Uncomment one section at a time as the lesson goes on.

items = ['coffee', 'bagel', 'juice', 'muffin']
prices = [3.50, 2.25, 4.00, 3.00]

for i in range(len(items)):
    print(f"{items[i]}: ${prices[i]:.2f}")


# ---------- List Basics ----------
# Lists share these tools with strings: indexes, len(), slicing, in, and for loops.

# print(f"type() on a list returns {type(items)}")
# print(f"I bought {len(items)} items")
# print(f"My first item was {items[0]}")
# print(f"My last item was {items[-1]}")
# print(f"My first two items were {items[0:2]}")
# print(f"Did I buy a bagel? {'bagel' in items}")
# print('Here is everything I bought:')
#
# for item in items:
#     # item holds the "current" item that we're looking at in this iteration of the loop
#     print(item)


# ---------- Challenge: has_value ----------
# For each numbered comment below, add a comment explaining the logic of the function!

# def has_value(items, value):
#     for item in items:  # 1.
#         if item == value:  # 2.
#             return True  # 3.
#     return False  # 4.
#
# print(has_value(items, 'bagel'))   # Prints True
# print(has_value(items, 'cookie'))  # Prints False


# ---------- Lists Are Mutable ----------
# Predict, then run: Does upper() change item? Then uncomment the last line to see what happens.

# item = 'bagel'
# item.upper()   # doesn't mutate the string, it makes a copy
# print(item)
# # item[0] = 'B'  # crashes on purpose

# The bagel is on sale. Unlike a string, a list can be changed in place.
# prices = [3.50, 2.25, 4.00, 3.00]
# prices[1] = 1.75
# print(prices)
#
# # We can even empty a list in one go
# prices.clear()
# print(prices)


# ---------- Adding and Removing Values ----------
# Predict, then run: What does each print statement show?

# items = ['coffee', 'bagel', 'juice', 'muffin']
#
# items.append('cookie')      # adds 'cookie' to the end
# items.insert(0, 'tea')      # adds 'tea' to the beginning
# print(items)
#
# items.pop()                 # removes the last item ('cookie')
# items.pop(0)                # removes the first item ('tea')
# print(items)
#
# items.insert(2, 'scone')    # At index 2, inserts 'scone'
# print(items)
#
# items[2] = 'croissant'      # At index 2, replaces 'scone' with 'croissant'
# print(items)
#
# items.remove('croissant')   # Removes the first 'croissant' it finds
# print(items)


# ---------- Predict, then run: Parallel Lists ----------
# The customer changes their mind about the bagel. What does the receipt print?
# Challenge: Fix the program so that every item prints beside its own price.

# items = ['coffee', 'bagel', 'juice', 'muffin']
# prices = [3.50, 2.25, 4.00, 3.00]
#
# items.remove('bagel')
#
# for i in range(len(items)):
#     print(f"{items[i]}: ${prices[i]:.2f}")
