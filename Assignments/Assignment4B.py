
def printMenu():
    print("1. Espresso - $3.00\n2. Latte - $4.00\n3. Cappuccino - $4.00\n4. Tea - $2.00\n5. Exit and Checkout")
def getChoice():
    selection = ""
    selection = int(input("> "))
    if selection >= 1 and selection <= 5:
        return int(selection)
    else:
        return -1
def processOrder(selection):
    Eprice = 3.00
    Lprice = 4.00
    Cprice = 4.00
    Tprice = 2.00
    price = 0
    match selection:
        case 1:
            amt = int(input("How many Espresso(s) would you like? "))
            price = Eprice * amt
            print(f"Added {amt} Espresso(s) - ${price:.2f}")
        case 2:
            amt = int(input("How many Latte(s) would you like? "))
            price = Lprice * amt
            print(f"Added {amt} Latte(s) - ${price:.2f}")
        case 3:
            amt = int(input("How many Cappuccino(s) would you like? "))
            price = Cprice * amt
            print(f"Added {amt} Cappuccino(s) - ${price:.2f}")
        case 4:
            amt = int(input("How many Tea(s) would you like? "))
            price = Tprice * amt
            print(f"Added {amt} Tea(s) - ${price:.2f}")
    return price

def getTotal(subtotal):
    if subtotal < 0:
        pass
    else:
        tax = subtotal * 0.06
        total = subtotal + tax
        print(f"Subtotal: ${subtotal:.2f}\nTax (6%): ${tax:.2f}\nTotal: ${total:.2f}")
print("[Owl About Coffee]")
subtotal = 0
while True:
    printMenu()
    choice = getChoice()
    if choice == -1:
        print("\nInvalid choice, please select one of options displayed.\n")
        continue
    if choice == 5:
        print()
        getTotal(subtotal)
        print("[Program Terminated]")
        break
    subtotal += processOrder(choice)
    print()
