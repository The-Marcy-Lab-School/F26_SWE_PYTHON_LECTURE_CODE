# Combining Steps: the output of one tool can feed straight into the next.
# Uncomment one section at a time as the lesson goes on.

purchases = [
    {"customer": "Ada", "item": "coffee", "price": 3.50, "payment": "card"},
    {"customer": "Zo", "item": "bagel", "price": 2.25, "payment": "cash"},
    {"customer": "Malik", "item": "coffee", "price": 3.50, "payment": "card"},
    {"customer": "Priya", "item": "juice", "price": 4.00, "payment": "cash"},
    {"customer": "Ada", "item": "muffin", "price": 3.00, "payment": "card"},
]

# Name the intermediate steps when it helps the reader. This finds the two highest prices.
prices = [purchase["price"] for purchase in purchases]  # transform each purchase into its price
ordered = sorted(prices, reverse=True)                  # put the prices in order, highest first
top_two = ordered[:2]                                   # keep the first two

print(top_two)
# [4.0, 3.5]


# # ---------- The Same Steps in One Line ----------
# # Folding the steps into one line is fine while it stays readable.

# print(sorted([purchase["price"] for purchase in purchases], reverse=True)[:2])
# # [4.0, 3.5]
