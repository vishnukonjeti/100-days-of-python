"""
Day 02 - BMI Calculator (Practice 1)
Course: 100 Days of Code - Python Bootcamp (Angela Yu)

This program calculates BMI using
the formula: weight / (height^2)
"""

height = 1.65
weight = 84

# Calculate BMI
bmi = weight / (height ** 2)

# Print BMI rounded to 2 decimal places
print(round(bmi, 2))