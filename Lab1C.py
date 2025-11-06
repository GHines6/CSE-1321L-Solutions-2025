# Class: CSE 1321L
# Section: 01
# Term: Fall 2025
# Instructor: Michael Butler
# Name: Giovanni Hines
# Lab#: 1C

# Program Lab1C.py
# Demonstrate the use of the input function to read numeric data.
# Calculates fuel efficiency based on values entered by the user.
miles = input("Enter the number of miles: ")
gallons = input("Enter the gallons of fuel used: ")
mpg = int (miles) / float (gallons)
print ("Miles Per Gallon: " + str (mpg))