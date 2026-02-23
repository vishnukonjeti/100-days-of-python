"""
Day 03 - Treasure Island
Course: 100 Days of Code - Python Bootcamp (Angela Yu)

A text-based adventure game using nested conditionals.
Only one correct path leads to the treasure.
"""

print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')

print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.\n")

# Level 1
path = input("You are at a crossroad. Where do you want to go? Left or Right?\n").lower()

if path == "left":
    print("You have reached a lake.")

    # Level 2
    action = input("Type 'wait' to wait for a boat. Type 'swim' to swim across.\n").lower()

    if action == "wait":
        print("You arrive at an island unharmed.")

        # Level 3
        door = input("There are three doors. One red, one blue, one yellow. Which colour?\n").lower()

        if door == "yellow":
            print("Congratulations! You found the treasure! You Win! 🎉")
        elif door == "red":
            print("Burned by fire. Game Over.")
        elif door == "blue":
            print("Eaten by beasts. Game Over.")
        else:
            print("That door does not exist. Game Over.")

    else:
        print("Attacked by trout. Game Over.")

else:
    print("You fell into a hole. Game Over.")