# Run this file with ada, then lovelace, then a word with capital letters.

word = input("Give me a word: ").strip().lower()

vowels = 0
for letter in word:
    if letter in "aeiou":
        vowels += 1

print(f"{word} has {vowels} vowels.")
