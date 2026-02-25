"""
Day 05 - Find Highest Score (Practice 1)
Course: 100 Days of Code - Python Bootcamp (Angela Yu)

This program finds the highest score in a list
without using the built-in max() function.
"""

student_scores = [150, 142, 185, 120, 171, 184,
                  149, 24, 59, 68, 199, 78, 65,
                  89, 86, 55, 91, 64, 89]

max_score = student_scores[0]

for score in student_scores:
    if score > max_score:
        max_score = score

print(max_score)