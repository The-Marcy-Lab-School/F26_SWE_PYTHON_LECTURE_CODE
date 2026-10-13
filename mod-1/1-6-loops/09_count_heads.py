# Challenge: Write the count_heads function so that it:
# 1. Takes in a number of flips as a parameter.
# 2. Flips a coin that many times, keeping count of how many times heads was flipped.
# 3. Prints back the final number of heads like this:
#    You flipped [heads flipped] heads out of [total] flips! That is [percent]%!

import random

def flip_coin():
    flip_result = random.randint(0, 1)
    return "heads" if flip_result == 1 else "tails"

def count_heads(flips):
    pass  # replace this line with your code

count_heads(10)
count_heads(100)
