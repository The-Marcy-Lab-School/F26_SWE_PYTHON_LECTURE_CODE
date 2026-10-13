# Everything can easily be turned into a string
print(str(1))          # -> "1"
print(str(True))       # -> "True"

# Not everything becomes a number in a nice way
print(int(False))      # -> 0
print(int("42"))       # -> 42
print(float("0.50"))   # -> 0.5
print(int("hello"))    # -> crashes with ValueError
