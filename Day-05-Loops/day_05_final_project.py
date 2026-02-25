"""
Day 05 - Password Generator (Final Project)
Course: 100 Days of Code - Python Bootcamp (Angela Yu)

Generates a password based on user input:
- Easy mode: ordered characters
- Hard mode: shuffled characters
"""

import random

letters = [
    'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p',
    'q','r','s','t','u','v','w','x','y','z',
    'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P',
    'Q','R','S','T','U','V','W','X','Y','Z'
]

numbers = ['0','1','2','3','4','5','6','7','8','9']
symbols = ['!','#','$','%','&','(',')','*','+']

print("Welcome to the PyPassword Generator!")

nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input("How many symbols would you like?\n"))
nr_numbers = int(input("How many numbers would you like?\n"))

password_list = []

# Add letters
for _ in range(nr_letters):
    password_list.append(random.choice(letters))

# Add symbols
for _ in range(nr_symbols):
    password_list.append(random.choice(symbols))

# Add numbers
for _ in range(nr_numbers):
    password_list.append(random.choice(numbers))

# Easy Password
print("Easy Password Generated:")
print("".join(password_list))

# Hard Password
random.shuffle(password_list)
print("Hard Password Generated:")
print("".join(password_list))
