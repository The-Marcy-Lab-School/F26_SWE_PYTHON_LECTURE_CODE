# Run this file a few times. Does it take the same number of rolls each time?

import random

roll = None
roll_count = 0
while (roll != 6):
    roll = random.randint(1, 6)
    roll_count += 1

print(f"It took {roll_count} rolls to get a 6!")
