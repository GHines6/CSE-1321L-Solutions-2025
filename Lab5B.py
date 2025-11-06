# Class: CSE 1321L
# Section: 01
# Term: Fall 2025
# Instructor: Michael Butler
# Name: Giovanni Hines
# Lab#: 5B

print("[Factorial Calculator]")
while True:
    num = int(input("Enter a number: "))
    if num < 0:
        print("Error: Number must be 0 or positive, try again.")
        continue
    factorial = 1
    n = num
    for i in range(1, n + 1):
        factorial *= i
    print()
    print(f"Calculating {num}! ...")
    print(f"{num}! is {factorial}")
    print()
    print("Program Terminated")
    break