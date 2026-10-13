# Challenge: This program is hard-coded. The only way to get a different story is to edit the variables in main().
#
# 1. Replace the hard-coded variables in main() with values from input(),
#    and remove any spaces the user types around their answers.
# 2. Ask the user to type Y or N, and turn their answer into True or False for is_happy.
#    y, Y, and Y with spaces around it should all count as yes.
#
# Then run the program with different words and fix these problems inside madlib():
#
# 3. Print the name with a capital first letter and the rest in lowercase: ben, BEN, and bEN all print as Ben.
# 4. Put "an" before new_item when it starts with a vowel, and "a" otherwise: "an apple" but "a new car".
# 5. When the quantity is 1, leave the s off the item: "his 1 dog", but "his 50 dogs".
# 6. Start the story with a title, such as The Story of Ben, and print a line of = beneath it
#    that is exactly as long as the title.

def madlib(name, verb, quantity, item, new_item, is_happy):
    print(f"There once was a man named {name}.")
    print(f"Every day he would {verb} with his {quantity} {item}s")

    if is_happy:
        print(f"But then, he found a {new_item} and everything changed!")
    else:
        print(f"But then, a {new_item} took over his life and he couldn't {verb} again!")

    print("The end.")

def main():
    name = 'Ben'
    verb = 'run'
    quantity = 50
    item = 'dog'
    new_item = 'new car'
    is_happy = False

    madlib(name, verb, quantity, item, new_item, is_happy)

main()
