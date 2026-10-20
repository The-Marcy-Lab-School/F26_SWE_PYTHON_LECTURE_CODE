# Uncomment one section at a time as the lesson goes on.

items = ['coffee', 'bagel', 'juice', 'muffin']
prices = [3.50, 2.25, 4.00, 3.00]


# ---------- Unpacking ----------
# One line of a receipt, split into its two parts and unpacked into two variables

# line = "coffee: 3.50"
# item, price = line.split(": ")
# print(item)   # coffee
# print(price)  # 3.50

# A variable with a * in front collects "the rest" as a list
# first_item, *other_items = items
# print(first_item)   # coffee
# print(other_items)  # ['bagel', 'juice', 'muffin']

# Inside square brackets, * unpacks one list into a new list, which makes a copy
# def add_item(items, item):
#     new_items = [*items, item]
#     return new_items
#
# more_items = add_item(items, 'cookie')
# print(items)       # ['coffee', 'bagel', 'juice', 'muffin']
# print(more_items)  # ['coffee', 'bagel', 'juice', 'muffin', 'cookie']

# Predict, then run: What happens when the number of variables does not match the number of elements?
# # first, second = items  # crashes on purpose


# ---------- Looping with enumerate() ----------
# The receipt loop again. enumerate() hands each pass an (index, item) pair, and the loop unpacks it.

# for index, item in enumerate(items):
#     print(f"{item}: ${prices[index]:.2f}")


# ---------- 2D Lists ----------
# The receipt as one list of rows. Each row is a list holding one item and its price.
# The first index picks the row, and the second index picks the column.

# receipt = [
#     ['coffee', 3.50],
#     ['bagel', 2.25],
#     ['juice', 4.00],
#     ['muffin', 3.00],
# ]
#
# print(receipt[1])      # ['bagel', 2.25]
# print(receipt[1][0])   # bagel
# print(receipt[1][1])   # 2.25
# print(len(receipt))    # 4, the number of rows
# print(len(receipt[0])) # 2, the number of columns in the first row


# ---------- Tuples: Lists That Cannot Change ----------
# Predict, then run: Everything that reads a list works on a tuple. What happens on the last line?

# line = ('coffee', 3.50)
#
# print(line[0])          # coffee
# print(len(line))        # 2
# print(3.50 in line)     # True
#
# # line[1] = 3.00  # crashes on purpose
