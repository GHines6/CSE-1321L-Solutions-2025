
dictionary = {}
run = True
login = False
while run == True:
    choice = input("Choose an option\n1 - Login\n2 - Register\nE - Exit\n")
    print()
    match choice:
        case "1":
            print("[Login]")
            username = input("Username: ")
            password = input("Password: ")
            if dictionary.get(username) == password:
                print("Success!")
                login = True
                print()

                while login == True:
                    option = input("Choose an option\n3 - Change Password\n4 - Logout\nE - Exit\n")
                    match option:
                        case "3":
                            print()
                            print("[Changin password]")
                            newpass = input("Password: ")
                            dictionary[username] = newpass
                            print()
                        case "4":
                            print()
                            print("Logging Out...")
                            login = False
                            continue
                        case "E":
                            print("Terminating...")
                            run = False
                            break


            else:
                print("Incorrect username/password!")
        case "2":
            print("[Register]")
            username = input("Username: ")
            password = input("Password: ")
            dictionary[username] = password
            print("User successfully added!")
        case "E":
            print("Terminating...")
            run = False
            break
    print()
