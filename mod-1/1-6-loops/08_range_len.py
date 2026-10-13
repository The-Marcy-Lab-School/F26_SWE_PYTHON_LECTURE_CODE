# Predict, then run: This loop iterates over a range() instead of over the string itself.
# What does each pass print?

word = "loop"
for i in range(len(word)):
    print(i, word[i])
