"""
Day 03 - BMI Categorization (Practice 1)
Course: 100 Days of Code - Python Bootcamp (Angela Yu)

This program calculates BMI and categorizes it
as underweight, normal weight, or overweight.
"""

weight = 85
height = 1.85

bmi = weight / (height ** 2)

if bmi < 18.5:
    print("underweight")
elif bmi < 25:
    print("normal weight")
else:
    print("overweight")