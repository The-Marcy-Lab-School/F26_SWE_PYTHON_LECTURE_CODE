# Question: A sign-up form accepts a phone number when it has exactly 10 digits
# once the dashes are removed. How would you complete this is_valid_phone function?
# Replace None with your code.

def is_valid_phone(phone):
    return None

print(is_valid_phone('555-123-4567'))   # True
print(is_valid_phone('5551234567'))     # True
print(is_valid_phone('555-1234'))       # False
print(is_valid_phone('555-CALL-NOW'))   # False
