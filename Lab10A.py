
class Chair:
    def __init__(self, numOfLegs = 4, rolling = False, material = "Wood"):
        self.numOfLegs = numOfLegs
        self.rolling = rolling
        self.material = material

print("You are about to create a chair.")
legs = input("How many legs does your chair have: ")
rolling = input("Is your chair rolling (true/false): ")
material = input("What is your chair made of: ")

if rolling == "true":
    roll_bool = True
else:
    roll_bool = False

c = Chair(int(legs), roll_bool, material)

if c.rolling:
    is_rolling_text = "rolling"
else:
    is_rolling_text = "not rolling"

print(f"Your chair has {c.numOfLegs} legs, is {is_rolling_text}, and is made of {c.material}.")

print("This program is going to change that.")

c.numOfLegs = 4
c.rolling = False
c.material = "Wood"

if c.rolling:
    is_rolling_text = "rolling"
else:
    is_rolling_text = "not rolling"

print(f"Your chair has {c.numOfLegs} legs, is {is_rolling_text}, and is made of {c.material}.")

