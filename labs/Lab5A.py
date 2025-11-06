max = -999999999999999
print("Please enter 10 numbers and this program will display the largest.")
for x in range(1 , 11):
    x = int(input(f"Please enter number {x}: "))
    print()
    if x > max:
        max = x
print()

print(f"The largest number was {max}")
