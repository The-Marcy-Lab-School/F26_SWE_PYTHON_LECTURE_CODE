import random

# The stop value is always excluded from the range
for i in range(1, 101):      # 1, 2, 3, ... 100
    print(f"{i}. a {random.randint(1, 6)} was rolled")

for i in range(0, 20, 5):    # 0, 5, 10, 15
    print(i)

for i in range(10, 0, -1):   # 10, 9, 8, ... 1
    print(i)
