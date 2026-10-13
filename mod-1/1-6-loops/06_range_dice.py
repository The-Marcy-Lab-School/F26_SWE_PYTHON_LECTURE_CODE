# Predict, then run: What is the first number assigned to roll_number, and what is the last number?
# Why does the print statement use roll_number + 1?

import random

for roll_number in range(100):
    print(f"{roll_number + 1}. a {random.randint(1, 6)} was rolled")
