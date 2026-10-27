# Advanced Topics
# Uncomment one section at a time as the lesson goes on.

purchases = [
    {"customer": "Ada", "item": "coffee", "price": 3.50, "payment": "card"},
    {"customer": "Zo", "item": "bagel", "price": 2.25, "payment": "cash"},
    {"customer": "Malik", "item": "coffee", "price": 3.50, "payment": "card"},
    {"customer": "Priya", "item": "juice", "price": 4.00, "payment": "cash"},
    {"customer": "Ada", "item": "muffin", "price": 3.00, "payment": "card"},
]

# ---------- Finding the First Match with next() ----------
# The parentheses build a generator expression, which produces one value at a time, only when asked.
# next() asks for the first value. None is what next() returns when no purchase passes the test.

first_juice = next((purchase for purchase in purchases if purchase["item"] == "juice"), None)
print(first_juice)  # {'customer': 'Priya', 'item': 'juice', 'price': 4.0, 'payment': 'cash'}

first_tea = next((purchase for purchase in purchases if purchase["item"] == "tea"), None)
print(first_tea)  # None


# # ---------- A New List Shares Its Dictionaries ----------
# # The filtered list is new, but the dictionaries inside it are the same dictionaries the source list holds.

# purchases = [
#     {"customer": "Ada", "item": "coffee", "price": 3.50},
#     {"customer": "Zo", "item": "bagel", "price": 2.25},
# ]
#
# big_purchases = [purchase for purchase in purchases if purchase["price"] > 3]
# big_purchases[0]["price"] = 0
#
# print(purchases[0])                      # {'customer': 'Ada', 'item': 'coffee', 'price': 0}
# print(big_purchases[0] is purchases[0])  # True
#
# # To change the records without touching the originals, copy each one inside the comprehension.
# copied_purchases = [dict(purchase) for purchase in purchases if purchase["price"] > 3]
