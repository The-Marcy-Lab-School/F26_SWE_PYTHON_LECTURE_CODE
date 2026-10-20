# The dollar program in chapter 1.6 (../1-6-loops/14_dollar_total.py) kept only a running total.
# This program keeps every item and every price, so it can print a receipt.
# Run it and add a few items.

items = []
prices = []

while True:
    # now we also ask for an item (or done)
    item = input("Item (or done to finish): ").strip()
    if item.lower() == "done":
        break

    # then we ask for the price (for now, assume the user enters a valid number)
    price = float(input(f"Price of {item}: "))

    # add the item to the items list and price to the prices list
    items.append(item)
    prices.append(price)

# Once the while loop is done collecting inputs, calculate the total and print out the receipt
total = 0
for i in range(len(items)):
    print(f"{items[i]}: ${prices[i]:.2f}")
    total += prices[i]

print(f"Total: ${total:.2f}")
