# -*- coding: utf-8 -*-
"""
Simulate dice roll using random library

@author: raina
"""

import random

def roll_dice():
    return random.randint(1, 6)

print(f"Dice is rolling!")
# Simulate rolling the dice
dice_roll = roll_dice()
print(f"You rolled a {dice_roll}!")





