# A lookup table: the menu's keys are the items the café sells, so they are part of the data.
# The user types item names and the menu supplies the prices.
# Run it and order a few items. Try something the café does not sell, like pizza.

menu = {
    "coffee": 3.50,
    "bagel": 2.25,
    "juice": 4.00,
    "muffin": 3.00,
}

# Check for understanding: record or lookup table? Decide for each scenario, then compare with the answers in the lesson.
# 1. The number of loyalty_points each customer has (e.g. Ada has 50 while Zo has 25)
# 2. One customer's account data such as their name, email, and membership status
# 3. The remaining inventory for each item on the menu (e.g. 41 bagels left over, 20 muffins, etc...)
# 4. The café's details, such as its address, its phone number, and whether it has Wi-Fi

# The key can be held in a variable. Python uses the value the variable holds.
item = "bagel"
print(f"A {item} costs ${menu[item]:.2f}")

# Watch the quotes. Nothing on the menu is called "item".
# print(menu["item"])  # crashes on purpose

purchases = []

while True:
    item = input("Item (or done to finish): ").strip().lower()
    if item == "done":
        break

    # Instead of asking for the price, we first check that the item is on the menu...
    if item not in menu:
        # ...print a message if it isn't there...
        print(f"Sorry, {item} is not on the menu")
        continue

    # ...and then use the price from the menu
    # menu is a lookup table, and each dictionary appended here is a record
    purchases.append({"item": item, "price": menu[item]})

total = 0
for purchase in purchases:
    print(f"{purchase['item']}: ${purchase['price']:.2f}")
    total += purchase["price"]

print(f"Total: ${total:.2f}")
