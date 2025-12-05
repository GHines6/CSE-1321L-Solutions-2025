menu_items = {
    1: ("Coffee", 3.50),
    2: ("Sandwich", 5.75),
    3: ("Smoothie", 4.25),
    4: ("Muffin", 2.75)
}

daily_sales = []

def display_menu():
    print("[Owl Cafe]")
    print("1. Place Order")
    print("2. View Daily Sales")
    print("3. Exit")
    choice = input("> ")
    return choice

def take_order():
    total = 0.00
    while True:
        print("Menu Items:")
        print("1. Coffee - $3.50")
        print("2. Sandwich - $5.75")
        print("3. Smoothie - $4.25")
        print("4. Muffin - $2.75")
        try:
            item_select = int(input("Select an item (1-4): "))
            if item_select < 1 or item_select > 4:
                print("Error: Please enter a number between 1 and 4.")
                print()
                continue
            quantity = int(input("Enter quantity: "))
            if quantity <= 0:
                print("Error: Quantity must be at least 1.")
                print()
                continue
        except ValueError:
            print("Error: Please enter a valid number.")
            print()
            continue
        item, price = menu_items[item_select]
        subtotal = quantity * price
        total += subtotal
        daily_sales.append({"item": item, "quantity": quantity, "cost": subtotal})
        print(f"Added {quantity} {item}(s) - ${subtotal:.2f}")
        another = input("Add another item? (Y/N): ").lower()
        if another == "n":
            print()
            print(f"Order complete! Total for this order: ${total:.2f}")
            print()
            break
        else:
            print()

def show_sales():
    if not daily_sales:
        print("No sales recorded yet.")
        print()
        return

    print("Today's Sales:")

    summary = {}
    for order in daily_sales:
        item = order["item"]
        qty = order["quantity"]
        cost = order["cost"]

        if item not in summary:
            summary[item] = {"quantity": 0, "revenue": 0.0}

        summary[item]["quantity"] += qty
        summary[item]["revenue"] += cost

    total_revenue = 0.0
    for item_name in ["Coffee", "Sandwich", "Smoothie", "Muffin"]:
        if item_name in summary and summary[item_name]["quantity"] > 0:
            qty = summary[item_name]["quantity"]
            rev = summary[item_name]["revenue"]
            total_revenue += rev
            print(f"- {qty} {item_name}(s): ${rev:.2f}")

    print(f"Total Sales: ${total_revenue:.2f}")
    print()

def main():
    doRun = True
    while doRun:
        choice = display_menu()
        match choice:
            case "1":
                print()
                take_order()
            case "2":
                print()
                show_sales()
            case "3":
                print("Thank you for visiting Owl Cafe!")
                doRun = False
            case _:
                print("Error: Invalid menu option.\n")
main()