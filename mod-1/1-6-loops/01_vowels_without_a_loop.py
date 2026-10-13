# Run this file twice. Type ada the first time and lovelace the second time.
# What goes wrong each time? Why can't more if statements fix it?

word = input("Give me a word: ").strip().lower()

vowels = 0
if word[0] in "aeiou":
    vowels += 1
if word[1] in "aeiou":
    vowels += 1
if word[2] in "aeiou":
    vowels += 1
if word[3] in "aeiou":
    vowels += 1

print(f"{word} has {vowels} vowels.")
