fruits = 'apples, bananas, cherries'

# A slice goes from start up to but not including end
print(fruits[0:6])
# Output: apples

# Leaving out start begins at the first character
print(fruits[:6])
# Output: apples

# Leaving out end continues to the last character
print(fruits[8:])
# Output: bananas, cherries

# A negative number counts from the end
print(fruits[-8:])
# Output: cherries
