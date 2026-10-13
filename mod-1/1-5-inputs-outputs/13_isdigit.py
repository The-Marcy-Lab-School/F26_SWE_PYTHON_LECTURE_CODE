print('42'.isdigit())
# Output: True

print('4.2'.isdigit())
# Output: False

# Run this file and type twenty when asked. Compare what happens with 08_cast_input.py.
age = input("How old are you? ").strip()

if not age.isdigit():
    print(f"Sorry, {age} is not a number")
else:
    age = int(age)
    print(f"Next year you will be {age + 1}")
