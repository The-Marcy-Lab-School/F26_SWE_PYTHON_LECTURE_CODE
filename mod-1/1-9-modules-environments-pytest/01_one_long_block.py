# A café ordering program that also asks how many of each item the customer wants.
# Run it and order a few items. Try something the café does not sell, and a quantity that is not a number.
#
# Then think: the café wants the total to include sales tax.
# Which line would you have to change, and how would you check that the new total is right?

menu = {
    "coffee": 3.50,
    "bagel": 2.25,
    "juice": 4.00,
    "muffin": 3.00,
}
purchases = []

while True:
    item = input("Item (or done to finish): ").strip().lower()
    if item == "done":
        break
    if item not in menu:
        print(f"Sorry, {item} is not on the menu")
        continue

    while True:
        answer = input(f"How many {item}s? ").strip()
        try:
            quantity = int(answer)
            break
        except ValueError:
            print(f"Sorry, {answer} is not a whole number")

    purchases.append({"item": item, "quantity": quantity, "price": menu[item]})

total = 0
print("Receipt")
print("-" * 20)
for purchase in purchases:
    cost = purchase["quantity"] * purchase["price"]
    print(f"{purchase['quantity']} {purchase['item']}: ${cost:.2f}")
    total += cost
print("-" * 20)
print(f"Total: ${total:.2f}")
