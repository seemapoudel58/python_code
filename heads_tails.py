# Write a virtual coin toss program that randomly tell the user "Heads" or "Tails".

import random
side = random.randint(0, 1)
if (side == 1):
    print("Heads")
else:
    print("Tails")
