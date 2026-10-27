# Job 4: Reduce a list of values into one value.
# Uncomment one section at a time as the lesson goes on.

purchases = [
    {"customer": "Ada", "item": "coffee", "price": 3.50, "payment": "card"},
    {"customer": "Zo", "item": "bagel", "price": 2.25, "payment": "cash"},
    {"customer": "Malik", "item": "coffee", "price": 3.50, "payment": "card"},
    {"customer": "Priya", "item": "juice", "price": 4.00, "payment": "cash"},
    {"customer": "Ada", "item": "muffin", "price": 3.00, "payment": "card"},
]

prices = [3.50, 2.25, 3.50, 4.00, 3.00]

print(sum(prices))   # 16.25
print(min(prices))   # 2.25
print(max(prices))   # 4.0
print(len(prices))   # 5
print(sum(prices) / len(prices))  # 3.25, the average


# # ---------- The Limitation: sum(), min(), and max() Need Numbers ----------
# # len() only counts the elements, so it works on a list of dictionaries.
# # Uncomment the last line to see the error, then comment it out again so the rest of the file still runs.

# print(len(purchases))  # 5
# # print(sum(purchases))  # crashes on purpose: TypeError: unsupported operand type(s) for +: 'int' and 'dict'


# # ---------- The Fix: Transform the Records into Numbers First ----------

# prices = [purchase["price"] for purchase in purchases]
# print(prices)       # [3.5, 2.25, 3.5, 4.0, 3.0]
# print(sum(prices))  # 16.25
# print(max(prices))  # 4.0


# # ---------- The Accumulator Pattern ----------
# # Create a variable holding a starting value, update it once per element, and return it when the loop ends.

# def total(purchases):
#     running_total = 0                       # the starting value
#     for purchase in purchases:
#         running_total += purchase["price"]  # combine the current value into the total so far
#     return running_total                    # the final accumulated value
#
# print(total(purchases))  # 16.25
#
# # A loop that builds a list with .append() is an accumulator too.
# def get_customer_names(purchases):
#     customer_names = []                              # the starting value
#     for purchase in purchases:
#         customer_names.append(purchase["customer"])  # combine the current value into the list so far
#     return customer_names                            # the final accumulated value
#
# print(get_customer_names(purchases))  # ['Ada', 'Zo', 'Malik', 'Priya', 'Ada']


# # ---------- Generating a Frequency Counter ----------
# # An accumulator whose starting value is an empty dictionary builds a lookup table of counts.

# def get_item_counts(purchases):
#     # The starting value here is an empty {}
#     counts = {}
#     for purchase in purchases:
#         item = purchase["item"]
#         # if this is the first time we are looking at an item, .get returns 0 and we store its count as 1
#         # if we've already counted the item before, .get returns its count and we store that count + 1
#         counts[item] = counts.get(item, 0) + 1
#     return counts
#
# print(get_item_counts(purchases))
# # {'coffee': 2, 'bagel': 1, 'juice': 1, 'muffin': 1}
#
# # The standard library has this built in.
# from collections import Counter
# print(Counter([purchase["item"] for purchase in purchases]))


# # ---------- Predict, then run: Counting Sizes 🤔🤔🤔🤔🤔 ----------

# sizes = ["small", "large", "small", "small"]
#
# counts = {}
# for size in sizes:
#     counts[size] = counts.get(size, 0) + 1
#
# print(counts)
