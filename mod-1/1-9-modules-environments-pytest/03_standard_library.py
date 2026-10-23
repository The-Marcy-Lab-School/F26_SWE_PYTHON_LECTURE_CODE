# The standard library is the collection of modules that come with Python.
# They are imported exactly the same way as your own orders.py, and they need no installation.
# Predict, then run: Run this file twice. Which lines print something different the second time?

import random
import math

print(random.random())                    # a float ≥ 0 and < 1
print(random.randint(1, 10))              # a whole number from 1 to 10, inclusive
print(random.choice(["heads", "tails"]))  # one item from a list, chosen at random

print(math.pi)          # 3.141592653589793
print(math.ceil(4.2))   # 5
print(math.floor(4.8))  # 4
