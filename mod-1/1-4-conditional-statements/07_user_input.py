# This program asks the same question twice, once for each check.
# Run it and type No both times. Does each check behave the way you expect?

answer = input("Yes or No?")
if answer:
    print("they said yes!")
else:
    print(":(")

answer = input("Yes or No?")
if answer == "Yes":
    print("they said yes!")
else:
    print(":(")
