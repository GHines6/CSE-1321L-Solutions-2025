
escape = 0 #change this value to anything but 0 and the game will be complete
iron = 0
brass = 0
mattress = 0
plank = 0
chest = 0
print("You wake up in a dimly lit room. The air smells faintly of dust and old wood.\nThe only visible exit is a heavy iron door with a large lock.\nLooking around, you notice:")
print("- A small wooden chest sitting on a table in the corner\n- A bare mattress on the floor\n- A section of the floorboards that looks slightly uneven, almost as if one plank doesn’t quite fit")
print()
while escape == False:
    answer = input("What do you do?\nA. Open the heavy iron door.\nB. Inspect the wooden chest.\nC. Inspect the mattress.\nD. Inspect the suspicious plank in the floorboard.\n")
    match answer:
        case "A":
            if iron == False and brass == False:
                print("You tug the handle. It doesn't budge. The key must be somewhere in this room...")
            elif brass == True and iron == False:
                print("The brass key is too small for the door's lock. Maybe it opens something else.")
            elif iron == True:
                print("The iron key slides into the lock. You turn it, the mechanism clicks. The door swings open. You're free!")
                escape = 1
        case "B":
            if iron == False and brass == False and chest == False:
                print("The chest is locked. The key has to be around here somewhere...")
            elif brass == True and iron == False:
                print("The brass key fits the chest lock. It clicks open. Inside rests a heavier iron key. This one looks it is made for a door.")
                iron = 1
            elif brass == True and iron == True:
                print("You check the chest again, nothing else inside.")
            elif chest == True:
                print("You check the chest again, nothing else inside.")
            chest = 1
            iron = 1
        case "C":
            if mattress == False:
                print("You inspect the thin mattress, there is nothing on it. You lift it, there is nothing underneath either.")
            else:
                print("You already checked the mattress. There is nothing there.")
            mattress = 1
        case "D":
            if plank == False:
                print("You pry up the loose plank. Hidden in the dust lies a small brass key.")
            elif plank == True:
                print("You've already pried up the plank. There is nothing else underneath.")
            plank = 1
            brass = 1
    print()


