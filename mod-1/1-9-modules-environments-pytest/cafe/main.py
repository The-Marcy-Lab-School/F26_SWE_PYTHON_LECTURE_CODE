import orders
from interface import ask_for_item, ask_for_quantity, print_receipt

def main():
    while True:
        item = ask_for_item()
        if item == "done":
            break
        quantity = ask_for_quantity(item)
        orders.add_purchase(item, quantity)

    print_receipt(orders.purchases, orders.get_total())

if __name__ == "__main__":
    main()


# These notes sit below the code so that the line numbers above match the traceback in the lesson.

# ---------- The if __name__ == "__main__": Guard ----------
# Why is the guard here? To see what happens without it:
# 1. Replace the two guard lines above with a plain main() call.
# 2. In this folder, start the REPL with python3 and run: import main
# A file that imported main.py only to reuse something from it would suddenly start taking an order.
# Put the guard back when you are done.
