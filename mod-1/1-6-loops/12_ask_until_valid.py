# Run this file and type twenty, then 20.

age = input("How old are you? ").strip()

while not age.isdigit():
    print(f"Sorry, {age} is not a number")
    age = input("How old are you? ").strip()

age = int(age)
print(f"Next year you will be {age + 1}")
