"""
Day 06 - Function Practice (Practice 1)
Course: 100 Days of Code - Python Bootcamp (Angela Yu)

Demonstrates creating and calling a simple function.
"""

def get_user_name():
    """Asks for user's name and prints greeting."""
    name = input("What is your name? ")
    print(f"Hello, {name}")

print("Program Started")
get_user_name()