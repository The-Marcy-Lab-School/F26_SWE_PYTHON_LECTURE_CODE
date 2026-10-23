from orders import is_on_menu

def ask_for_item():
    while True:
        item = input("Item (or done to finish): ").strip().lower()
        # A Traceback Across Two Files: change this check to if len(item) > 0: and then order a pizza
        if item == "done" or is_on_menu(item):
            return item
        print(f"Sorry, {item} is not on the menu")

def ask_for_quantity(item):
    while True:
        answer = input(f"How many {item}s? ").strip()
        try:
            return int(answer)
        except ValueError:
            print(f"Sorry, {answer} is not a whole number")

def print_receipt(purchases, total):
    print("Receipt")
    print("-" * 20)
    for purchase in purchases:
        cost = purchase["quantity"] * purchase["price"]
        print(f"{purchase['quantity']} {purchase['item']}: ${cost:.2f}")
    print("-" * 20)
    print(f"Total: ${total:.2f}")
