# Challenge: This function changes the list it is given. Rewrite it so that the caller's list stays the same!

def shorten(items):
    items.pop()
    return items

letters = ['a', 'b', 'c']
shorter_letters = shorten(letters)

print(letters)          # should print ['a', 'b', 'c']
print(shorter_letters)  # should print ['a', 'b']
