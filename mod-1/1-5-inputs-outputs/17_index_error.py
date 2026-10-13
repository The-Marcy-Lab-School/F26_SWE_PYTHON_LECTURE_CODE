# Predict, then run: Run this file and press Enter without typing a name. What happens?
# Challenge: Add a len() check that prints "You didn't type a name." instead of crashing.

name = input("What's your name? ").strip()
print(f"Your name starts with {name[0].upper()}")
