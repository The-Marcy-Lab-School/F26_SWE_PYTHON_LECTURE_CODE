# Job 5: Find the first value that passes a test.
# A comprehension cannot stop early, so this job uses a for loop that returns as soon as it finds a match.
# Uncomment one section at a time as the lesson goes on.

purchases = [
    {"customer": "Ada", "item": "coffee", "price": 3.50, "payment": "card"},
    {"customer": "Zo", "item": "bagel", "price": 2.25, "payment": "cash"},
    {"customer": "Malik", "item": "coffee", "price": 3.50, "payment": "card"},
    {"customer": "Priya", "item": "juice", "price": 4.00, "payment": "cash"},
    {"customer": "Ada", "item": "muffin", "price": 3.00, "payment": "card"},
]

def find_purchase(purchases, item):
    for purchase in purchases:
        if purchase["item"] == item:
            return purchase
    return None  # nothing passed the test

def find_purchase_index(purchases, item):
    for index, purchase in enumerate(purchases):
        if purchase["item"] == item:
            return index
    return -1

print(find_purchase(purchases, "juice"))        # {'customer': 'Priya', 'item': 'juice', 'price': 4.0, 'payment': 'cash'}
print(find_purchase_index(purchases, "juice"))  # 3
print(find_purchase(purchases, "tea"))          # None


# # ---------- Predict, then run: Which Coffee? 🤔🤔🤔🤔🤔 ----------
# # "coffee" appears in purchases twice, at index 0 and at index 2.

# print(find_purchase_index(purchases, "coffee"))
