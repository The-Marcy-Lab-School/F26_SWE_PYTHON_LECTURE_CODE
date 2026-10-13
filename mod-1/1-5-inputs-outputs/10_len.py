message = 'Hello there!'

print(len(message))
# Output: 12

print(len(''))
# Output: 0

# Run this file and press Enter without typing a name. Then try typing only spaces.
name = input("What's your name? ").strip()

if len(name) == 0:
    print("You didn't type a name.")
else:
    print(f"Hello, {name}!")
