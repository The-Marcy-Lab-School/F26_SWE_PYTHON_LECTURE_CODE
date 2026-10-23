# The same café program, with each job moved into a helper function of its own.
# Run it and check that it behaves exactly like 01_one_long_block.py.
#
# Check for understanding: Which of these functions talk to the user, and which ones only work with the data?
# What does main() do? Decide, then compare with the answer in the lesson.

menu = {
    "coffee": 3.50,
    "bagel": 2.25,
    "juice": 4.00,
    "muffin": 3.00,
}
purchases = []

def add_purchase(item, quantity):
    purchases.append({"item": item, "quantity": quantity, "price": menu[item]})

def get_total():
    total = 0
    for purchase in purchases:
        total += purchase["quantity"] * purchase["price"]
    return total

def ask_for_item():
    while True:
        item = input("Item (or done to finish): ").strip().lower()
        if item == "done" or item in menu:
            return item
        print(f"Sorry, {item} is not on the menu")

def ask_for_quantity(item):
    while True:
        answer = input(f"How many {item}s? ").strip()
        try:
            return int(answer)
        except ValueError:
            print(f"Sorry, {answer} is not a whole number")

def print_receipt():
    print("Receipt")
    print("-" * 20)
    for purchase in purchases:
        cost = purchase["quantity"] * purchase["price"]
        print(f"{purchase['quantity']} {purchase['item']}: ${cost:.2f}")
    print("-" * 20)
    print(f"Total: ${get_total():.2f}")

# The main function just runs all of the other functions
def main():
    while True:
        item = ask_for_item()
        if item == "done":
            break
        quantity = ask_for_quantity(item)
        add_purchase(item, quantity)

    print_receipt()

main()
