# Class: CSE 1321L
# Section: 01
# Term: Fall 2025
# Instructor: Michael Butler
# Name: Giovanni Hines
# Lab#: 6A

x = 0
while x == 0 :
    print("Multiplication and Exponent Calculator")
    choice = input("Choose option 1 for Multiplication\nChoose option 2 for Exponentiation\nChoose option 3 to Exit\n")
    print()
    if choice == "1":
        number = 0
        operand = int(input("Enter an operand: "))
        operand2 = int(input("Enter the other operand: "))
        for _ in range(operand2):
            number = number + operand
        print(f"{operand} x {operand2} = {number}")
        print()
    elif choice == "2":
        number = 1
        base = int(input("Enter the base: "))
        exponent = int(input("Enter the exponent: "))
        for _ in range(exponent):
            value = 0
            for _ in range(base):
                value = value + number
            number = value
        print(f"{base}^({exponent}) = {number}")
        print()
    elif choice == "3":
        print("Closing the Calculator...")
        x = x + 1
    else:
        print("Invalid Choice")





