# The café's end-of-day report.
# Each café report challenge in the lesson completes one helper function below, and generate_report()
# at the bottom of the file calls every helper. Run the file after each challenge to watch the report fill in:
#     python3 01_cafe.py

purchases = [
    {"customer": "Ada", "item": "coffee", "price": 3.50, "payment": "card"},
    {"customer": "Zo", "item": "bagel", "price": 2.25, "payment": "cash"},
    {"customer": "Malik", "item": "coffee", "price": 3.50, "payment": "card"},
    {"customer": "Priya", "item": "juice", "price": 4.00, "payment": "cash"},
    {"customer": "Ada", "item": "muffin", "price": 3.00, "payment": "card"},
]


# ---------- Challenge: Café Report, Part 1 🏗️🏗️🏗️🏗️🏗️ ----------
# Print one line per purchase with the customer's name and how the customer paid.
# Should print:
#     Ada paid by card
#     Zo paid by cash
#     Malik paid by card
#     Priya paid by cash
#     Ada paid by card

def print_payment_lines(purchases):
    pass  # replace with a for loop


# ---------- Challenge: Café Report, Part 2 🏗️🏗️🏗️🏗️🏗️ ----------
# Return a list of how each purchase was paid.
# Should return ['card', 'cash', 'card', 'cash', 'card']

def get_payment_methods(purchases):
    return []  # replace with a comprehension


# ---------- Challenge: Café Report, Part 3 🏗️🏗️🏗️🏗️🏗️ ----------
# Return the items that customers paid for in cash, using one comprehension.
# Should return ['bagel', 'juice']

def get_cash_items(purchases):
    return []  # replace with a comprehension


# ---------- Challenge: Café Report, Part 4 🏗️🏗️🏗️🏗️🏗️ ----------
# Return a lookup table that maps each payment method to the number of purchases paid that way.
# Should return {'card': 3, 'cash': 2}

def count_payments(purchases):
    payment_counts = {}
    # your loop here
    return payment_counts


# ---------- Challenge: Café Report, Part 5 🏗️🏗️🏗️🏗️🏗️ ----------
# Return the item of the first purchase paid with payment, or None when no purchase was paid that way.
# first_item_paid_by(purchases, "cash") should return 'bagel'
# first_item_paid_by(purchases, "card") should return 'coffee'
# first_item_paid_by(purchases, "check") should return None

def first_item_paid_by(purchases, payment):
    return None  # replace with a for loop that returns early


# ---------- Challenge: Café Report, Part 6 🏗️🏗️🏗️🏗️🏗️ ----------
# Return every price paid in cash, from highest to lowest, without changing purchases.
# Should return [4.0, 2.25]

def get_cash_prices(purchases):
    return []  # replace with sorted() and a comprehension


# ---------- Challenge: Coffee Revenue 🏗️🏗️🏗️🏗️🏗️ ----------
# Return how much the café made from coffee. Name each job your code does before you write it.
# Should return 7.0

def get_coffee_total(purchases):
    return 0  # replace with your code


# ---------- The Report ----------
# generate_report() calls every helper above. Until a helper is finished, its line of the report
# shows the placeholder value the helper returns.

def generate_report():
    print("===== End-of-Day Report =====")
    print()
    print("How each customer paid:")
    print_payment_lines(purchases)
    print()

    payment_methods = get_payment_methods(purchases)
    print(f"Payment methods: {payment_methods}")
    print("At least one customer paid in cash" if "cash" in payment_methods else "No one paid in cash")
    print(f"Items paid for in cash: {get_cash_items(purchases)}")
    print(f"Purchases per payment method: {count_payments(purchases)}")
    print(f"First item paid by cash: {first_item_paid_by(purchases, 'cash')}")
    print(f"First item paid by card: {first_item_paid_by(purchases, 'card')}")
    print(f"First item paid by check: {first_item_paid_by(purchases, 'check')}")
    print(f"Cash prices, highest first: {get_cash_prices(purchases)}")
    print(f"Coffee revenue: ${get_coffee_total(purchases):.2f}")


if __name__ == "__main__":
    generate_report()
