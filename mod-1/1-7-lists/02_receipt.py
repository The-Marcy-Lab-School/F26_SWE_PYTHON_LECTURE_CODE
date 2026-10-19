# Run this file and add a few items. Try a price that is not a number, like two.

items = []
prices = []

while True:
    # now we also ask for an item (or done)
    item = input("Item (or done to finish): ").strip()
    if item.lower() == "done":
        break

    # then we ask for the price
    price = input(f"Price of {item}: ").strip()
    digits = price.replace(".", "", 1)
    if not digits.isdigit():
        print(f"Sorry, {price} is not a price, so {item} was not added.")
        continue

    # add the item to the items list and price to the prices list
    items.append(item)
    prices.append(float(price))

# Once the while loop is done collecting inputs, calculate the total and print out the receipt
total = 0
for i in range(len(items)):
    print(f"{items[i]}: ${prices[i]:.2f}")
    total += prices[i]

print(f"Total: ${total:.2f}")
