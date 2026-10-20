# Predict, then run: Type 4.50, then press Enter without typing anything, then 10, then done. What is printed after each answer?
# Which line stops float() from crashing on the blank answer?
# For now, this program assumes that every answer is either a number, done, or blank.

total = 0

while True:
    amount = input("Enter an amount in dollars (like 4.50), or done to finish: ").strip().lower()
    if amount == "done":
        break

    if amount == "":
        continue

    total += float(amount)

print(f"Your total is ${total:.2f}")
