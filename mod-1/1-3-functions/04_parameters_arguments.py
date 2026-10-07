# x and y are parameters that reference the values provided when the function is called.
def print_sum(x, y):
    print(x + y)

# 5 and 3 are the arguments. 8 is printed
print_sum(5, 3)

# This time, 10 and 2 are the arguments. 12 is printed
print_sum(10, 2)

# Predict, then run: What does each of these two calls do?
# Uncomment one line at a time.
# print_sum('hello', 5)
# print_sum()


# Challenge: Refactor say_hello so that it can print any name and hobby.
# Test your code by invoking the function with various inputs. What happens when no input is provided?

def say_hello():
    print("Hi, my name is Ben. I like to code!")

say_hello()
