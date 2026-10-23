menu = {
    "coffee": 3.50,
    "bagel": 2.25,
    "juice": 4.00,
    "muffin": 3.00,
}
purchases = []

def is_on_menu(item):
    return item in menu

def add_purchase(item, quantity):
    purchases.append({"item": item, "quantity": quantity, "price": menu[item]})

def get_total():
    total = 0
    for purchase in purchases:
        total += purchase["quantity"] * purchase["price"]
    return total


# These sections sit below the code so that the line numbers above match the traceback in the lesson.

# # ---------- What Happens When You Import a File? ----------
# # Predict, then run: Uncomment the print below, then run python3 main.py (not orders.py) and type done.
# # Write down everything you expect to see printed, in order.

# print("orders was loaded")


# # ---------- __name__ ----------
# # Comment out the print above and uncomment this one instead.
# # Then add the same line to main.py, just below its import lines, and run python3 main.py.

# print(f"my __name__ is {__name__}")
