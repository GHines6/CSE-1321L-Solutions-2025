
transaction = ""
Balance = 0
print("[Welcome to OwlBanking]")
option = 0 #option != Q
while option != "Q":
    option = (input("Select an option:\n1 - Deposit\n2 - Withdraw\n3 - Check Balance\n4 - Check Transaction History\nQ - Quit\n"))
    print()
    match option:
        case "1":
            deposit = int(input("How much do you want to deposit: $"))
            old_bal = Balance
            Balance += deposit
            transaction += f"${deposit} was deposited balance went from ${old_bal} to ${Balance}\n"
        case "2":
            if Balance == 0:
                print("Error: Cannot Withdraw with balance of zero")
            else:
                old_bal = Balance
                withdraw = int(input("How much do you want to withdraw: $"))
                Balance -= withdraw
                transaction += f"${withdraw} was withdrawn, balance went from ${old_bal} to ${Balance}\n"
                if withdraw > old_bal:
                    print("Error: Cannot Withdraw a larger amount than balance")
        case "3":
            print(f"Balance: ${Balance:.2f}")
        case "4":
            print(transaction)
        case"Q":
            break

