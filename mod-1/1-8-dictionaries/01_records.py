# Chapter 1.7 ended with a receipt stored as rows. Which index holds the price? You have to remember.
# Uncomment one section at a time as the lesson goes on.

receipt = [['coffee', 3.50], ['bagel', 2.25], ['juice', 4.00], ['muffin', 3.00]]
print(receipt[1][1])  # 2.25

# A dictionary stores each value under a key instead of at a position. Now the code says what it wants.
purchase_1 = {"item": "coffee", "price": 3.50}
print(purchase_1["price"])  # 3.5


# # ---------- What is a Dictionary? ----------
# # Dictionaries can be written in one line or across multiple.

# purchase_2 = {
#     "item": "bagel",
#     "price": 2.25,
# }
# print(purchase_2["price"])
#
# # Keys need quotes. Without them, Python looks for a variable named price.
# # bad_purchase = {"item": "juice", price: 4.00}  # crashes on purpose

# # Dictionaries do two jobs. purchase_1 is a record. This menu is a lookup table, which you will use in 03_menu_order.py.
# menu = {
#     "coffee": 3.50,
#     "bagel": 2.25,
#     "juice": 4.00,
#     "muffin": 3.00,
# }
# print(menu)


# # ---------- Records: One Thing's Information Together ----------
# # The programmer decides a record's keys in advance, so every purchase record has the same shape.

# purchase_1 = {"item": "coffee", "price": 3.50}
# purchase_2 = {"item": "bagel", "price": 2.25}
# purchase_3 = {"item": "juice", "price": 4.00}
# purchase_4 = {"item": "muffin", "price": 3.00}
# print(purchase_1, purchase_2, purchase_3, purchase_4)


# # ---------- Reading Values with Bracket Notation and .get() ----------
# # Predict, then run: There is no "discount" in purchase_1. Uncomment the last line to see what happens.

# purchase_1 = {"item": "coffee", "price": 3.50}
# print(f"One {purchase_1['item']}, please")
#
# print(purchase_1.get("discount"))     # .get() returns None for a missing key
# print(purchase_1.get("discount", 0))  # or the default you choose
# print(purchase_1.get("item"))
#
# if "discount" in purchase_1:  # you can also ask first
#     print(purchase_1["discount"])
#
# # print(purchase_1["discount"])  # crashes on purpose


# # ---------- Predict, then run: Does in Check Values? 🤔🤔🤔🤔🤔 ----------
# # The value "coffee" is in purchase_1. Does this print anything?

# purchase_1 = {"item": "coffee", "price": 3.50}
#
# if "coffee" in purchase_1:
#     print(purchase_1["item"])
#
# print("item" in purchase_1)
# print("coffee" in purchase_1)


# # ---------- Challenge: Phone Records 🏗️🏗️🏗️🏗️🏗️ ----------
# # Create a dictionary record for a phone with at least 3 keys: at least one string, one boolean, and one number.
# # Then make a second phone record with the exact same shape but different values.
# # Print one value from each phone, using bracket notation or .get().

# phone_1 = None
# phone_2 = None


# # ---------- Changing a Record ----------
# # Predict, then run: What does each print statement show?

# purchase_1 = {"item": "coffee", "price": 3.50}
#
# # Create and Update use the same line: assigning to a key adds it if it is new, or replaces its value
# purchase_1["price"] = 3.00
# purchase_1["discount"] = 0.50
# print(purchase_1)
#
# # Delete with del ...
# del purchase_1["discount"]
# print(purchase_1)
#
# # ... or with .pop(), which also returns the value it removed
# price = purchase_1.pop("price")
# print(price)
# print(purchase_1)


# # ---------- Lists of Dictionaries ----------
# # The receipt from 02_receipt.py, typed in so you don't have to enter it on every run.
# # Predict, then run: What does each print statement show?

# purchases = [
#     {"item": "coffee", "price": 3.50},
#     {"item": "bagel", "price": 2.25},
#     {"item": "juice", "price": 4.00},
#     {"item": "muffin", "price": 3.00},
# ]
#
# # Reach one by position, then by key. Compare this with receipt[1][1] above.
# print(purchases[1]["price"])
#
# # Remove one the same way you remove from any list. The bagel and its price leave together.
# purchases.pop(1)
# print(len(purchases))
#
# for purchase in purchases:
#     print(f"{purchase['item']}: ${purchase['price']:.2f}")


# # ---------- A Dictionary with a List ----------
# # A dictionary can hold a list of records too.
# # Predict, then run: Read the last line from left to right, one step at a time.
# receipt = {
#     "customer": "Ada",
#     "purchases": [
#         {"item": "coffee", "price": 3.50},
#         {"item": "bagel", "price": 2.25},
#     ],
# }
#
# print(receipt["purchases"])
# print(receipt["purchases"][0])
# print(receipt["purchases"][0]["item"])


# # ---------- Predict, then run: Changing Ada's Receipt 🤔🤔🤔🤔🤔 ----------
# # The cashier makes Ada's coffee free by deleting its price. What happens when the loop adds up the prices?
# # Predict first, then uncomment the loop to find out.

# receipt = {
#     "customer": "Ada",
#     "purchases": [
#         {"item": "coffee", "price": 3.50},
#         {"item": "bagel", "price": 2.25},
#     ],
# }
#
# del receipt["purchases"][0]["price"]
#
# # total = 0                                  # crashes on purpose
# # for purchase in receipt["purchases"]:
# #     total += purchase["price"]
# # print(total)


# # ---------- Challenge: Updating a Receipt 🏗️🏗️🏗️🏗️🏗️ ----------
# # Without retyping any existing record, write code that:
# # 1. Adds a muffin that costs 3.00 to Ada's purchases.
# # 2. Changes the bagel's price to 2.00, because it is on sale.
# # 3. Adds a "paid" key to the receipt, set to False.
# # 4. Prints each purchase as item: $price, followed by the total.
# # Your program should print:
# # coffee: $3.50
# # bagel: $2.00
# # muffin: $3.00
# # Total: $8.50

# receipt = {
#     "customer": "Ada",
#     "purchases": [
#         {"item": "coffee", "price": 3.50},
#         {"item": "bagel", "price": 2.25},
#     ],
# }
