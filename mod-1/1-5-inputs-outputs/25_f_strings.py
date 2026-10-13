print(f"The sum of 10 and 2 is {10 + 2}")
# Output: The sum of 10 and 2 is 12

# Without the f, the curly braces are just characters
print("The sum of 10 and 2 is {10 + 2}")
# Output: The sum of 10 and 2 is {10 + 2}

first = "ada"
last = "lovelace"

print(f"Welcome, {first[0].upper()}{first[1:]}!")
# Output: Welcome, Ada!

print(f"Your initials are {first[0].upper()}.{last[0].upper()}.")
# Output: Your initials are A.L.

print(f"Your last name has {len(last)} letters.")
# Output: Your last name has 8 letters.

card = "4111222233334444"

print(f"Paid with the card ending in {card[-4:]}")
# Output: Paid with the card ending in 4444
