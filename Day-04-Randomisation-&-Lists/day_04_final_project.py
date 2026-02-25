"""
Day 04 - Rock Paper Scissors (Final Project)
Course: 100 Days of Code - Python Bootcamp (Angela Yu)

A simple Rock-Paper-Scissors game using lists and random module.
"""

import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

rps = [rock, paper, scissors]

player_num = int(input("What do you choose? Type 0 for Rock, 1 for Paper, 2 for Scissors.\n"))

if player_num < 0 or player_num > 2:
    print("You have entered an invalid number.")
else:
    print("You chose:")
    print(rps[player_num])

    computer_num = random.randint(0, 2)
    print("Computer chose:")
    print(rps[computer_num])

    if player_num == computer_num:
        print("It's a tie!")
    elif (player_num == 0 and computer_num == 2) or \
         (player_num == 1 and computer_num == 0) or \
         (player_num == 2 and computer_num == 1):
        print("You Win!")
    else:
        print("You Lose!")