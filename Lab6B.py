# Class: CSE 1321L
# Section: 01
# Term: Fall 2025
# Instructor: Michael Butler
# Name: Giovanni Hines
# Lab#: 6B

import random
random_number = random.randint(1, 100)
print("Guess the number I am thinking!")
number = int(input("Enter any number between 1 and 100: "))
while number != random_number:
    if number > random_number:
        print("Too high!")
    elif number < random_number:
        print("Too low!")
    number = int(input("Enter any number between 1 and 100: "))
print(f"Correct! I was thinking of {random_number}")
