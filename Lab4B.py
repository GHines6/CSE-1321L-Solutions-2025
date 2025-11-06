print("Welcome! ")
number = float(input("Please input a number: "))
print()
option = int(input("What would you like to do with this number:\n0) Get the additive inverse of the number\n1) Get the reciprocal of the number\n2) Square the number\n3) Cube the number\n4) Exit the program\n"))
if option == 0:
    print(f"The additive inverse of {number} is {number * -1}")
elif option == 1 and number == 0:
    print()
    print("Cannot divide by 0!")
elif option == 1:
    print(f"The reciprocal of {number} is {round(float(1 / number), 3)}")
elif option == 2:
    print(f"The square of {number} is {number ** 2}")
elif option == 3:
    print(f"The cube of {number} is {number ** 3}")
elif option == 4:
    print()
    print("Thank you, goodbye!")
else:
    print()
    print("Invalid option!")


