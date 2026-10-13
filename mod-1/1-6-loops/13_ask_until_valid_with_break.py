# The same program as 12_ask_until_valid.py, with the question asked in one place.
# while True never ends the loop by itself. What does?

while True:
    age = input("How old are you? ").strip()
    if age.isdigit():
        break
    print(f"Sorry, {age} is not a number")

age = int(age)
print(f"Next year you will be {age + 1}")
