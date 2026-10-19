# Challenge: This function can verify whether or not a given list items contains a given value value.
# For each numbered comment below, add a comment explaining the logic of the function!

def has_value(items, value):
    for item in items:  # 1.
        if item == value:  # 2.
            return True  # 3.
    return False  # 4.

letters = ['a', 'b', 'c', 'd']
print(has_value(letters, 'c'))  # Prints True
print(has_value(letters, 'e'))  # Prints False
