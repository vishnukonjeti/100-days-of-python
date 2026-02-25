"""
Day 05 - FizzBuzz (Practice 2)
Course: 100 Days of Code - Python Bootcamp (Angela Yu)

Print numbers from 1 to 100.
- If divisible by 3 → print "Fizz"
- If divisible by 5 → print "Buzz"
- If divisible by both → print "FizzBuzz"
"""

for number in range(1, 101):
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    elif number % 5 == 0:
        print("Buzz")
    elif number % 3 == 0:
        print("Fizz")
    else:
        print(number)
