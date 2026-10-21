# Dictionaries are held by reference, exactly like lists.
# Uncomment one section at a time as the lesson goes on.

purchase = {"item": "coffee", "price": 3.50}
print(purchase)


# # ---------- Dictionaries are Mutable and Held by Reference ----------
# # Predict, then run: What will purchase and receipt_line hold after this runs?

# purchase = {"item": "coffee", "price": 3.50}
# receipt_line = purchase       # both variables reference the same dictionary
# receipt_line["price"] = 3.00  # mutating the referenced dictionary
#
# print(purchase)
# print(receipt_line)
# print(purchase is receipt_line)


# # ---------- Changing a Dictionary Inside a Function ----------
# # Predict, then run: apply_discount returns nothing. Does coffee change?

# def apply_discount(purchase, amount):
#     purchase["price"] = purchase["price"] - amount
#
# coffee = {"item": "coffee", "price": 3.50}
# apply_discount(coffee, 0.50)
# print(coffee)


# # ---------- Copying a Dictionary Before Changing It ----------
# # Predict, then run: Which dictionaries have the sale price?

# def discounted_copy(purchase, amount):
#     new_purchase = dict(purchase)  # copy the key-value pairs of purchase into a new dictionary
#     new_purchase["price"] = new_purchase["price"] - amount
#     return new_purchase
#
# coffee = {"item": "coffee", "price": 3.50}
# sale_coffee = discounted_copy(coffee, 0.50)
#
# print(coffee)
# print(sale_coffee)
# print(coffee is sale_coffee)
#
# # purchase.copy() and {**purchase} do the same thing as dict(purchase)
# print(coffee.copy())
# print({**coffee})


# # ---------- Advanced Topics: Which Values Can Be Keys ----------
# # Keys can be numbers, or tuples, which cannot change. Then uncomment the last line to see what happens.

# roman_numerals = {
#     1: "I",
#     5: "V",
#     10: "X",
# }
# print(roman_numerals[5])
#
# sized_menu = {
#     ("coffee", "small"): 3.00,
#     ("coffee", "large"): 3.50,
#     ("juice", "small"): 3.25,
#     ("juice", "large"): 4.00,
# }
# print(sized_menu[("coffee", "large")])
#
# # A list can change, so a list cannot be a key.
# # bad_menu = {["coffee", "large"]: 3.50}  # crashes on purpose


# # ---------- Advanced Topics: A Copy Shares Its Nested Values ----------
# # Predict, then run: A customer orders a second coffee like the first, but with an extra shot. What happens to the first coffee?

# first_coffee = {"item": "coffee", "price": 3.50, "add_ons": ["oat milk"]}
# second_coffee = dict(first_coffee)
# second_coffee["add_ons"].append("extra shot")
#
# print(first_coffee["add_ons"])
# print(first_coffee["add_ons"] is second_coffee["add_ons"])


# # ---------- Challenge: Keeping the First Coffee's Add-Ons 🏗️🏗️🏗️🏗️🏗️ ----------
# # Copy the code from the section above and fix it so that first_coffee keeps only "oat milk",
# # while second_coffee gets both "oat milk" and "extra shot".
