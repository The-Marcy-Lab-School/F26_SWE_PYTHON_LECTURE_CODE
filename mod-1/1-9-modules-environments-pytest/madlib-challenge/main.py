# Challenge: Split the Madlib 🏗️🏗️🏗️🏗️🏗️
# The madlib function and the main function that asks the user for input share this one file.
# 1. Move the madlib function into its own file called madlib.py, in this folder, and import it in main.py.
# 2. Replace the main() call at the bottom of main.py with the if __name__ == "__main__": guard.
# Run python3 main.py before and after, and check that the story comes out the same.

def madlib(name, verb, quantity, item, new_item, is_happy):
    name = name[0].upper() + name[1:].lower()

    if new_item[0].lower() in "aeiou":
        article = "an"
    else:
        article = "a"

    if quantity == "1":
        items = item
    else:
        items = item + "s"

    title = f"The Story of {name}"
    print(title)
    print("=" * len(title))

    print(f"There once was a man named {name}.")
    print(f"Every day he would {verb} with his {quantity} {items}")

    if is_happy:
        print(f"But then, he found {article} {new_item} and everything changed!")
    else:
        print(f"But then, {article} {new_item} took over his life and he couldn't {verb} again!")

    print("The end.")

def main():
    name = input('Choose a name: ').strip()
    verb = input('Choose a verb: ').strip()
    quantity = input('Choose a quantity: ').strip()
    item = input('Choose an item: ').strip()
    new_item = input('Choose a new item: ').strip()
    is_happy_response = input('Choose whether the story is happy. Y or N: ')
    is_happy = is_happy_response.strip().upper() == "Y"

    madlib(name, verb, quantity, item, new_item, is_happy)

main()
