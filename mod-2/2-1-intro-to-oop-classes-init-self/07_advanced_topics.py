# Advanced Topics
# Uncomment one section at a time as the lesson goes on.

# ---------- Calling a Method Through the Wrong Class ----------
# Written through the class, the first argument has to be an instance of that class.
print(str.upper('sold out'))  # SOLD OUT

# print(str.upper(5))  # crashes on purpose: TypeError: descriptor 'upper' for 'str' objects doesn't apply to a 'int' object
