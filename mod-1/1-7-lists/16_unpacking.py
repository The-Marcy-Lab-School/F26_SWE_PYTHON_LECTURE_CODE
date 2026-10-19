first_name, last_name = "Ada Lovelace".split(" ")

print(first_name)  # Ada
print(last_name)   # Lovelace

# A variable with a * in front collects "the rest" as a list
items = ['coffee', 'bagel', 'juice', 'muffin']

first_item, *other_items = items

print(first_item)   # coffee
print(other_items)  # ['bagel', 'juice', 'muffin']

# Inside square brackets, * unpacks one list into a new list, which makes a copy
letters = ['a', 'b', 'c']
copy = [*letters]

def extend(items, value):
    new_items = [*items, value]
    return new_items

more_letters = extend(letters, 'd')

print(letters)       # Prints ['a', 'b', 'c']
print(more_letters)  # Prints ['a', 'b', 'c', 'd']

# Predict, then run: What happens when the number of variables does not match the number of elements?
first, second = items
