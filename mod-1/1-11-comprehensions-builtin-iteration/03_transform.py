# Job 2: Transform every value and collect the results in a new list.
# Uncomment one section at a time as the lesson goes on.

purchases = [
    {"customer": "Ada", "item": "coffee", "price": 3.50, "payment": "card"},
    {"customer": "Zo", "item": "bagel", "price": 2.25, "payment": "cash"},
    {"customer": "Malik", "item": "coffee", "price": 3.50, "payment": "card"},
    {"customer": "Priya", "item": "juice", "price": 4.00, "payment": "cash"},
    {"customer": "Ada", "item": "muffin", "price": 3.00, "payment": "card"},
]

# Transform purchases into a list of customer names
customer_names = []
for purchase in purchases:
    customer_names.append(purchase["customer"])

print(customer_names)  # ['Ada', 'Zo', 'Malik', 'Priya', 'Ada']


# # ---------- List Comprehensions ----------
# # [expression for item in source_list]
# # Read it from the for outward: "for each purchase in purchases, compute purchase["customer"] and collect it."

# customer_names = [purchase["customer"] for purchase in purchases]
#
# print(customer_names)  # ['Ada', 'Zo', 'Malik', 'Priya', 'Ada']
# print(len(purchases), len(customer_names))  # the new list always has exactly as many elements as the source


# # ---------- The Expression Can Call a Function ----------
# # Keeping the work in a small function is what lets the comprehension stay one readable line.

# def format_line(purchase):
#     return f"{purchase['item']}: ${purchase['price']:.2f}"
#
# receipt_lines = [format_line(purchase) for purchase in purchases]
# print(receipt_lines)
# # ['coffee: $3.50', 'bagel: $2.25', 'coffee: $3.50', 'juice: $4.00', 'muffin: $3.00']


# # ---------- Imperative vs. Declarative Code ----------
# # Both build the same list. Only the loop lets you add a step, like this print.

# # Imperative: High Control & High Effort:
# customer_names = []
# for purchase in purchases:
#     customer_names.append(purchase["customer"])
#     # A custom print statement that is only possible when written imperatively
#     print(f"Added {purchase['customer']}")
#
# # Declarative: Low Control & Low Effort:
# customer_names = [purchase["customer"] for purchase in purchases]
