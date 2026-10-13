print('apples, bananas, cherries'.split(', '))
# Output: ['apples', 'bananas', 'cherries']

# Predict, then run: split() returns a list, not a string. What happens when we chain .lower() after it?
print('a, b'.split(', ').lower())
