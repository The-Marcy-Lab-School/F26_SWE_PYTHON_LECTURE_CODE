phone = '555-123-4567'

# Replacing a character with an empty string removes it
print(phone.replace('-', ''))
# Output: 5551234567

# replace() replaces every match...
print('apples'.replace('p', 'g'))
# Output: aggles

# ...unless a third argument says how many to replace
print('apples'.replace('p', 'g', 1))
# Output: agples
