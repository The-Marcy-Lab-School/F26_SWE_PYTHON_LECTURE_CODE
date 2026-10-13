# Run this file and type a few messages. Then type Exit.
# What happens if you type exit with a lowercase e?

user_input = None # user hasn't typed in anything yet
while (user_input != "Exit"):
    user_input = input("type something and hit enter: ")
    print(f"you typed: {user_input}")

print("Good bye!")
