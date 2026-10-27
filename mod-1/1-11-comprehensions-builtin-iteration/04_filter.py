# Job 3: Keep some values and discard the others (filter).
# [expression for item in source_list if test]
# Uncomment one section at a time as the lesson goes on.

purchases = [
    {"customer": "Ada", "item": "coffee", "price": 3.50, "payment": "card"},
    {"customer": "Zo", "item": "bagel", "price": 2.25, "payment": "cash"},
    {"customer": "Malik", "item": "coffee", "price": 3.50, "payment": "card"},
    {"customer": "Priya", "item": "juice", "price": 4.00, "payment": "cash"},
    {"customer": "Ada", "item": "muffin", "price": 3.00, "payment": "card"},
]

adas_purchases = [purchase for purchase in purchases if purchase["customer"] == "Ada"]
print(adas_purchases)
# [
#   {'customer': 'Ada', 'item': 'coffee', 'price': 3.5, 'payment': 'card'},
#   {'customer': 'Ada', 'item': 'muffin', 'price': 3.0, 'payment': 'card'}
# ]


# # ---------- Transform and Filter at Once ----------
# # Read it from the for outward: "for each purchase in purchases, keep it if its price is over 3, and collect its item."

# big_items = [purchase["item"] for purchase in purchases if purchase["price"] > 3]
# print(big_items)  # ['coffee', 'coffee', 'juice']
