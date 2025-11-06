# Class: CSE 1321L
# Section: 01
# Term: Fall 2025
# Instructor: Michael Butler
# Name: Giovanni Hines
# Lab#: 3A

NumberOfSmall = int(input("Enter the number of small sandwiches: "))
NumberOfMedium = int(input("Enter the number of medium sandwiches: "))
NumberOfLarge = int(input("Enter the number of large sandwiches: "))
NumberOfXL = int(input("Enter the number of extra-large sandwiches: "))
print() #Gradescope was printing it out weird without this space
print(f"You've entered {NumberOfSmall} small sandwiches.")
print(f"You've entered {NumberOfMedium} medium sandwiches.")
print(f"You've entered {NumberOfLarge} large sandwiches.")
print(f"You've entered {NumberOfXL} extra-large sandwiches.")
TimeSmall = int(NumberOfSmall * 30)
TimeMedium = int(NumberOfMedium * 60)
TimeLarge = int(NumberOfLarge * 75)
TimeXL = int(NumberOfXL * 135)
TotalTime = int(TimeXL + TimeLarge + TimeMedium + TimeSmall)
Minutes = int(TotalTime / 60)
Seconds = float(TotalTime /60 - Minutes)
seconds = int(Seconds * 60)
print() #Gradescope was counting it wrong without this space
print(f"Total cooking time is {Minutes} minutes and {seconds} seconds.")
