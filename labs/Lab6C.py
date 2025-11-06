
while True:
    n = int(input("Enter Number for Rows or 0 to quit: "))
    if n == 0:
        break

    for r in range(1, n + 1):
        print(" " * (n - r), end="")
        for k in range(r, 0, -1):
            print(k, end="")
        for k in range(2, r + 1):
            print(k, end="")
        print()






