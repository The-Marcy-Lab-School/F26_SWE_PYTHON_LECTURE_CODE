# Challenge: Dynamic Keys. Complete the program so that it lets the café owner add items to the menu!

menu = {
    "coffee": 3.50,
    "bagel": 2.25,
    "juice": 4.00,
    "muffin": 3.00,
}

while True:
    print("Here is your menu: ", menu)
    new_item = input("Add an item to your menu, or press q to exit. ")

    if new_item == 'q':  # a guard clause
        break

    # for now, assume the owner enters a valid number
    price = float(input(f"Okay, what is the price of {new_item}? "))

    # add the new item and its price to the menu!
