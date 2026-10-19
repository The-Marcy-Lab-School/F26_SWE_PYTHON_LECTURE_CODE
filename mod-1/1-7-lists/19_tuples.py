# Predict, then run: Everything that reads a list works on a tuple. What happens on the last line?

coordinate = (30, 90)

print(coordinate[0])      # 30
print(len(coordinate))    # 2
print(90 in coordinate)   # True

coordinate[0] = 31
