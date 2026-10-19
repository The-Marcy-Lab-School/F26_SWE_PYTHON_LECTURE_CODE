# Predict, then run: This program adds 100000 numbers to the back of one list and to the front of another.
# Which loop is slower, and by roughly how much?
# Then change both range(100000) calls to range(10000) and run it again. What changed?

import time

start = time.perf_counter()
back = []
for number in range(100000):
    back.append(number)
print(f"append took {time.perf_counter() - start:.3f} seconds")

start = time.perf_counter()
front = []
for number in range(100000):
    front.insert(0, number)
print(f"insert(0) took {time.perf_counter() - start:.3f} seconds")
