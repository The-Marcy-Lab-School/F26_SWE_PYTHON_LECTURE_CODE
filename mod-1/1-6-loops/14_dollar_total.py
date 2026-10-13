# Predict, then run: Type 4.50, then ten, then 10, then done. What is printed after each answer?
# Which line stops float() from crashing on ten?

total = 0

while True:
    amount = input("Enter an amount in dollars (like 4.50), or done to finish: ").strip().lower()
    if amount == "done":
        break

    digits = amount.replace(".", "", 1)
    if not digits.isdigit():
        print(f"Sorry, {amount} is not a dollar amount")
        continue

    total += float(amount)

print(f"Your total is ${total:.2f}")
