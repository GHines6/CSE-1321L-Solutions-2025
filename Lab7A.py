
def isValid(width, height):
    combined = width + height
    if combined > 30:
        return True
    else:
        return False
def area(width, height):
    area = width * height
    return area
def perimeter(width, height):
    perimeter = 2 * (width + height)
    return perimeter
run = True
again = "Y"
num = 0
while run:
    if num >= 1:
        print()
        again = input("Do you want to enter another width and height (Y/N)?: ")
        if again == "Y":
            print()
    if again == "Y":
        width = float(input("Enter width: "))
        height = float(input("Enter height: "))
        if isValid(width, height):
            print("This is a valid rectangle. ")
            print(f"The area is: {area(width, height)}")
            print(f"The perimeter is: {perimeter(width, height)}")
        else:
            print("This is an invalid rectangle. ")
    else:
        run = False
        print()
        print("Program Ends")
    num += 1
