class BuildingBlueprint:
    def __init__(self, stories = 10, apartments = 20, occupancy = 1.0):
        self.stories = stories
        self.apartments = apartments
        self.occupancy = occupancy
        self.full = (self.occupancy == 1.0)
    def update_occupancy(self, new_occupancy):
        self.occupancy = new_occupancy
        self.full = (self.occupancy == 1.0)


def main():
    buildingOne = BuildingBlueprint()
    buildingTwo = BuildingBlueprint(30,30,0.75)

    print("Year 2025:")
    print(f"Building 1 has {buildingOne.stories} floors, {buildingOne.apartments} apartments, and is {int(buildingOne.occupancy * 100)}% occupied. Full? {buildingOne.full}")
    print(f"Building 2 has {buildingTwo.stories} floors, {buildingTwo.apartments} apartments, and is {int(buildingTwo.occupancy * 100)}% occupied. Full? {buildingTwo.full}")
    print()
    print("Many years passed")
    print()

    buildingOne.update_occupancy(0.0)
    buildingTwo.update_occupancy(1.0)

    print(f"Building 1 has {buildingOne.stories} floors, {buildingOne.apartments} apartments, and is {int(buildingOne.occupancy * 100)}% occupied. Full? {buildingOne.full}")
    print(f"Building 2 has {buildingTwo.stories} floors, {buildingTwo.apartments} apartments, and is {int(buildingTwo.occupancy * 100)}% occupied. Full? {buildingTwo.full}")
    print("Looks like people prefer taller buildings.")

main()