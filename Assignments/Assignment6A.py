class Car:
    def __init__(self, make, model, year, rate):
        self.make = make
        self.model = model
        self.year = year
        self.rate = rate
        self.isRented = False


    def is_available(self):
        return not self.isRented

    def set_rented(self, days):
        self.isRented = True
        print(f"{self.year} {self.make} {self.model} has been rented for {days} days.")
        print(f"Customer will be charged ${self.rate * days:.2f} at return")

    def set_returned(self):
        self.isRented = False
        print(f"{self.year} {self.make} {self.model} has been returned")


    def info(self):
        if not self.isRented:
            return (f"{self.year} {self.make} {self.model} - AVAILABLE, PER DAY RATE: ${self.rate}")
        else:
            return (f"{self.year} {self.make} {self.model} - RENTED")

class OwlRental:
    def __init__(self):
        self.depot = []

    def add_car(self, make, model, year, rate):
        self.depot.append(Car(make, model, year, rate))

    def list_cars(self):
        for INDEX, car in enumerate(self.depot):
            print(f"{INDEX} - {car.info()}")

    def rent_car(self, index, days):
        car = self.depot[index]
        if not car.is_available():
            print("Error: Car is already rented")
            return
        car.set_rented(days)


    def return_car(self, index):
        car = self.depot[index]

        if car.is_available():
            print("Error: Car is not rented")
            return
        car.set_returned()

def main():
    rental = OwlRental()

    rental.add_car("Toyota", "Corolla", 2025, 49.99)
    rental.add_car("Honda", "Civic", 2023, 45.50)
    rental.add_car("Tesla", "Model 3", 2023, 119.00)

    print("[Owl Rent-a-Car]")

    while True:
        print("1. Rent\n2. Return\n3. View cars\n4. Exit")
        choice = input("> ")
        print()
        match choice:
            case "1":
                rental.list_cars()
                INDEX = int(input("Select an index: "))
                days = int(input("How many day(s)?: "))
                rental.rent_car(INDEX, days)
            case "2":
                rental.list_cars()
                INDEX = int(input("Select an index: "))
                rental.return_car(INDEX)
            case "3":
                rental.list_cars()
            case "4":
                break
        print()
main()