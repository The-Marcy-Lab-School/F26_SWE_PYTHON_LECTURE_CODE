# The receipt program from chapter 1.7 (../1-7-lists/01_receipt.py) kept two parallel lists.
# This version keeps one list of purchase records, so each item and its price stay together.
# Run it and add a few items.

purchases = []

while True:
    item = input("Item (or done to finish): ").strip()
    if item.lower() == "done":
        break

    # for now, assume the user enters a valid number
    price = float(input(f"Price of {item}: "))

    # one record holds both pieces of information about the purchase
    # the key "item" is a string, and the variable item holds the value stored under it
    purchases.append({"item": item, "price": price})

# The for loop hands us one record at a time, so we no longer need range(len(items))
total = 0
for purchase in purchases:
    print(f"{purchase['item']}: ${purchase['price']:.2f}")
    total += purchase["price"]

print(f"Total: ${total:.2f}")
