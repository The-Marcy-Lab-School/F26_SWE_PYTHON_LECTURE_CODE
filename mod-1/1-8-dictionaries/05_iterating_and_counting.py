# The menu from 03_menu_order.py, plus a day's purchases.
# Uncomment one section at a time as the lesson goes on.

menu = {
    "coffee": 3.50,
    "bagel": 2.25,
    "juice": 4.00,
    "muffin": 3.00,
}

purchases = [
    {"item": "coffee", "price": 3.50},
    {"item": "bagel", "price": 2.25},
    {"item": "coffee", "price": 3.50},
    {"item": "juice", "price": 4.00},
    {"item": "coffee", "price": 3.50},
]

print(menu)


# # ---------- Iterating Over Keys and Values of a Dictionary ----------
# # So far we have iterated over a list of records, one record at a time.

# for purchase in purchases:
#     print(purchase["item"])  # do something with each purchase record

# # A for loop over a dictionary visits its keys.
# for item in menu:
#     price = menu[item]
#     print(f"{item} costs ${price:.2f}")

# # The .values() method hands you only the values.
# total = 0
# for price in menu.values():
#     total += price
#
# print(f"One of everything costs ${total:.2f}")

# # The .items() method hands you each key and its value together, unpacked in the for line.
# for item, price in menu.items():
#     print(f"{item} costs ${price:.2f}")


# # ---------- Predict, then run: Items Under $3.50 🤔🤔🤔🤔🤔 ----------
# # The café wants a list of everything on the menu that costs less than $3.50. What does this print?

# cheap_items = []
# for item, price in menu.items():
#     if price < 3.50:
#         cheap_items.append(item)
#
# print(cheap_items)


# # ---------- Challenge: Counting Items 🏗️🏗️🏗️🏗️🏗️ ----------
# # The café wants to know which items sell best.
# # Complete count_items so that it returns a lookup table mapping each item to the number of times it appears in purchases.
# # Start with an empty dictionary. The first time an item appears it is not a key yet.

# def count_items(purchases):
#     # return a dictionary that maps each item to how many times it was bought
#     return None
#
# print(count_items(purchases))  # should print {'coffee': 3, 'bagel': 1, 'juice': 1}
