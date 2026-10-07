def add(x, y):
    return x + y

# The value of 5 + 3 is returned, resolving to `result = 8`
result = add(5, 3)

# We can now use the computed value outside of the function
print(result)

# Predict, then run: What does this print? In what order are the calls resolved?
print(add(12, add(5, 3)))


# Predict, then run: What does this print? There are two lines of output.

def say_hello(name):
    print(f"Hello, {name}!")

result = say_hello("Ada")
print(result)
