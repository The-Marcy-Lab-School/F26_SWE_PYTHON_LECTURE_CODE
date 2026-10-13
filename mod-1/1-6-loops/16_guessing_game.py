# Challenge: Write a number guessing game program that:
# 1. Generates a random number from 1-10. This is the secret number.
# 2. Asks the user to guess the number using the input() function.
# 3. If the guess is correct, prints a winning message and ends the program.
# 4. If the guess is incorrect, asks the user to guess again.
# 5. If the user ever types "Exit", ends the program.
#
# Bonus Features
# 1. Keep track of the guesses, and when the guess is correct, print how many guesses it took.
# 2. Limit the user to 5 guesses. If they guess incorrectly 5 times, they lose!

import random

secret_number = random.randint(1, 10)
