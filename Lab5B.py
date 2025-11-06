
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
