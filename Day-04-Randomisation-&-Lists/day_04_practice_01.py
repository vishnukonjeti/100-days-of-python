"""
Day 04 - Random Name Picker (Practice)
Course: 100 Days of Code - Python Bootcamp (Angela Yu)

This program randomly selects a person from a list.
"""

import random

friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]

# Method 1: Using random.choice (recommended)
print(random.choice(friends))

# Method 2: Using random index
number = random.randint(0, len(friends) - 1)
print(friends[number])