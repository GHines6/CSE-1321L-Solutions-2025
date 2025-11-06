
print("[Mailing List]")
print()
mylist = []
selection = ""
emailList = ""
while selection != 4:
    selection = int(input("1 - Add email\n2 - Delete email\n3 - List all emails\n4 - Quit\nMake your selection: "))
    print()
    match selection:
        case 1:
            email = input("Enter the email to be added: ")
            print("Email added to mailing list.")
            print()
            mylist.append(email)
        case 2:
            email = input("Enter the email to be removed: ")
            if email in mylist:
                mylist.remove(email)
                print(f"{email} has been removed from the mailing list.")
                print()
            else:
                print(f"No such email in mailing list: {email}")
                print()
        case 3:
            for num in range(len(mylist)):
                print(mylist[num])
            print()

        case 4:
            print("Shutting down...")
            break
