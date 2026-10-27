# Job 1: Do something with every value without producing a result.
# A plain for loop already handles this job well, so there is no new tool here.

purchases = [
    {"customer": "Ada", "item": "coffee", "price": 3.50, "payment": "card"},
    {"customer": "Zo", "item": "bagel", "price": 2.25, "payment": "cash"},
    {"customer": "Malik", "item": "coffee", "price": 3.50, "payment": "card"},
    {"customer": "Priya", "item": "juice", "price": 4.00, "payment": "cash"},
    {"customer": "Ada", "item": "muffin", "price": 3.00, "payment": "card"},
]

# For every element in the list, do something
for purchase in purchases:
    print(f"{purchase['item']}: ${purchase['price']:.2f}")

# coffee: $3.50
# bagel: $2.25
# coffee: $3.50
# juice: $4.00
# muffin: $3.00
