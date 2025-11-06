
print("[Friend List]")
print()
friendlist = []
n = 0
d = 1
selection = ""
while selection != 3:
    n = 0
    d = 1
    selection = int(input("1 - Add friend\n2 - List friends\n3 - Quit\nMake your selection: "))
    print()
    match selection:
        case 1:
            name = input("Enter your friend's name: ")
            age = input("Enter your friend's age: ")
            print("Friend added")
            print()
            friendlist.append((name, age))
        case 2:
            for (n, a) in friendlist:
                print(f"Name: {n}, Age: {a}")
            print()
        case 3:
            print("Shutting down...")
            break
