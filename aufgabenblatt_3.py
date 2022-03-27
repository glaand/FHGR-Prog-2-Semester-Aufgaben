import random
import csv

class Vehicle:
    transmission = "automatic"  # Klassenattribut
    def __init__(self, color, brand, construction_year, number_of_tyres, power):
        self.color = color 
        self.brand = brand
        self.construction_year = construction_year 
        self.number_of_tyres = number_of_tyres
        self.power = power

    def getTires(self):
        return self.number_of_tyres

    def getConstructionYear(self):
        return self.construction_year

    def getCSVRow(self):
        return [self.color, self.brand, self.construction_year, self.number_of_tyres, self.power]

    def __repr__(self) -> str:
        return f"Vehicle(color={self.color}, brand={self.brand}, construction_year={self.construction_year}, number_of_tyres={self.number_of_tyres}, power={self.power})"

def aufgabe11():
    print("----- Aufgabe 11 ------")
    v1 = Vehicle("black", "BMW", 2019, 4, 300)
    print(f"Brand: {v1.brand}")
    print(f"Transmission: {v1.transmission}")
    print("")

def aufgabe12():
    print("----- Aufgabe 12 ------")
    v2 = Vehicle("blue", "AUDI", 2000, 4, 100)
    print(f"Tyres: {v2.getTires()}")
    print(f"Construction Year: {v2.getConstructionYear()}")
    print("")

def aufgabe13():
    print("----- Aufgabe 13 ------")
    def populateVehicles():
        vehicles = []

        colorOptions = ["black", "white", "yellow", "red", "green", "silver", "gold"]
        brandOptions = ["BMW", "AUDI", "MERCEDES-BENZ", "OPEL", "FERRARI"]
        constructionYearOptions = [2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010]
        numberOfTyresOptions = [4,8,12]
        powerOptions = [70,100,200,300,500]

        for _ in range(random.randint(10,20)):
            newVehicle = Vehicle(
                random.choice(colorOptions),
                random.choice(brandOptions),
                random.choice(constructionYearOptions),
                random.choice(numberOfTyresOptions),
                random.choice(powerOptions),
            )
            vehicles.append(newVehicle)
        return vehicles

    vehicles = populateVehicles()
    print(vehicles)
    print("")

def aufgabe14():
    print("----- Aufgabe 14 ------")
    class Car(Vehicle):
        def __init__(self, color, brand, construction_year, number_of_tyres, power, hasAutoPark):
            super().__init__(color, brand, construction_year, number_of_tyres, power)
            self.hasAutoPark = hasAutoPark

        def doAutoPark(self):
            if self.hasAutoPark:
                print("Parking the car automatically. Please do not touch the wheel.")
            else:
                print("This car does not have autopark installed. Please do it yourself!")

    class Motorbike(Vehicle):
        def __init__(self, color, brand, construction_year, number_of_tyres, power, hasSecondSeat):
            super().__init__(color, brand, construction_year, number_of_tyres, power)
            self.hasSecondSeat = hasSecondSeat

        def measureWindFlow(self):
            print("Measuring the wind flow, please wait...")

    class Truck(Vehicle):
        def __init__(self, color, brand, construction_year, number_of_tyres, power, workingHours):
            super().__init__(color, brand, construction_year, number_of_tyres, power)
            self.workingHours = workingHours

        def addWorkhours(self, hours):
            self.workingHours += hours
            print(f"Added {hours} hours to logbook. New total: {self.workingHours}")

    c1 = Car("black", "BMW", 2020, 4, 100, True)
    c1.doAutoPark()

    m1 = Motorbike("Yellow", "Yamaha", 2022, 2, 300, False)
    m1.measureWindFlow()

    t1 = Truck("white", "Dacia", 2000, 12, 500, 10)
    t1.addWorkhours(5)
    print("")

def aufgabe15():
    print("----- Aufgabe 15 ------") 
    header = ["color", "brand", "construction_year", "number_of_tyres", "power"]
    amount_vehicles = int(input("Please define how many vehicles you want to insert: "))
    vehicles = []
    for i in range(amount_vehicles):
        nr = i + 1
        print(f"Vehicle Nr. {nr}")
        print("======================")
        color = input("Color: ")
        brand = input("Brand: ")
        construction_year = input("Constr. Year: ")
        number_of_tyres = input("Nr. of tyres: ")
        power = input("Power: ")
        vehicles.append(Vehicle(color, brand, construction_year, number_of_tyres, power))
    
    f = open("vehicles.csv", "w")
    writer = csv.writer(f)
    writer.writerow(header)
    for vehicle in vehicles:
        writer.writerow(vehicle.getCSVRow())

    print(f"{len(vehicles)} Vehicles have been written to ./vehicles.csv")

if __name__ == "__main__":
    aufgabe11()
    aufgabe12()
    aufgabe13()
    aufgabe14()
    aufgabe15()