first = int(input("Enter the first side of the triangle: "))
second = int(input("Enter the second side of the triangle: "))
third = int(input("Enter the third side of the triangle: "))
total = (first) + (second) + (third)
any = bool((first > 0)  and (second > 0) and (third > 0))
equilateral = bool(first == second and first == third)
isosceles = bool((first == second and first != third) or (second == third and second != first))
scalene = bool((first != second and first != third) and (second != third and second != first))
invalid = bool((first + second <= third) or (first + third <= second) or (second + third <= first))

if any == True:
    match invalid:
        case True:
            print("The sides do not form a valid triangle.")
        case False:
            match equilateral:
                case True:
                    print("The triangle is an equilateral triangle.")
                case False:
                    match isosceles:
                        case True:
                            print("The triangle is an isosceles triangle.")
                        case False:
                            match scalene:
                                case True:
                                    print("The triangle is a scalene triangle.")
else:
    print("Invalid input. All sides must be greater than 0.")
    