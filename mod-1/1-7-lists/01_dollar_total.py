# The dollar program from chapter 1.6. It prints a total, but it forgets each amount once it is added.
# Could this program print a receipt of every amount the user typed?

total = 0

while True:
    amount = input("Enter an amount in dollars (like 4.50), or done to finish: ").strip()

    # exit on "done"
    if amount.lower() == "done":
        break

    # skip the amount if anything other than digits is left after removing a single `.`
    digits = amount.replace(".", "", 1)
    if not digits.isdigit():
        print(f"Sorry, {amount} is not a dollar amount")
        continue

    total += float(amount)

print(f"Your total is ${total:.2f}")
