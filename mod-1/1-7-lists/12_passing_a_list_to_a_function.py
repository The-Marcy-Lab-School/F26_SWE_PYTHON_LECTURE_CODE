def empty_the_list(items):
    # 3. Upon receiving the reference, this function modifies the list
    items.clear()

# 1. The list below is created in the heap and the "reference" to its location is stored in letters
letters = ['a', 'b', 'c']

# 2. When we invoke empty_the_list, we assign the "reference" to the function parameter "items"
empty_the_list(letters)

# 4. The list referenced by letters has been modified by the function!
print(letters)  # Prints []


# A function can never change a caller's number this way. Reassignment only changes the variable on the left of the =
x = 10
y = x
y += 1  # shorthand for y = y + 1

print(x)  # 10
print(y)  # 11
