def main():
    print("[Division]")

    while True:
        try:
            first = float(input("Enter first number: "))
            second = float(input("Enter second number: "))
            result = first / second
        except ZeroDivisionError:
            print("We cannot divide by zero.")
            print()
        except ValueError:
            print("Please enter numerical values.")
            print()
        else:
            print(f"{first} / {second} = {result:.2f}")
        again = input("Do you want to perform another division (Y/N)?: ")
        if again.upper() != "Y":
            print()
            break
        else:
            print()

main()

