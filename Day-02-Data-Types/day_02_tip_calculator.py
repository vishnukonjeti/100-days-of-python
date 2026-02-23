"""
Day 02 - Tip Calculator
Course: 100 Days of Code - Python Bootcamp (Angela Yu)

This program calculates the total bill including tip
and splits it equally among a group of people.
"""

print("Welcome to the tip calculator!")

bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10 12 15 "))
people = int(input("How many people to split the bill? "))

# Calculate tip amount
tip_amount = bill * tip / 100

# Calculate total bill including tip
total_bill = bill + tip_amount

# Calculate amount per person
split = total_bill / people

# Display result with exactly 2 decimal places
print(f"Each person should pay ${split:.2f}.")