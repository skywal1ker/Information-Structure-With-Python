"""
4. There are websites such as http://www.kbb.com that provide information about
second-hand vehicles. Design a base class for vehicle with fields such as model year,
total mileage, Vehicle Identification Number (VIN), EPA class, EPA mileage, engine,
transmission, and options.
Design subclasses for car, truck, SUV, and minivan. Think about the specific fields
and methods required for the subclasses.
"""


class Vehicle(object):
    def __init__(self, vin, make, model, year, mileage):
        self.VIN = vin
        self.make = make
        self.model = model
        self.year = year
        self.mileage = mileage

    def get_VIN(self):
        return self.VIN
    def get_make(self):
        return self.make        
    def get_model(self):
        return self.model
    def get_year(self):
        return self.year
    def get_mileage(self):
        return self.mileage


class car(Vehicle):
    def __init__(self, vin, make, model, year, mileage, trunkSize):
        Vehicle.__init__(self, vin, make, model, year, mileage)
        self.trunk_size = trunkSize


class truck(Vehicle):
    def __init__(self, vin, make, model, year, mileage, capacity):
        Vehicle.__init__(self, vin, make, model, year, mileage)
        self.capacity = capacity


v = Vehicle("JH4TB2H26CC000000" , "Toyoto", "Hatch back", 2013, 23)
c = car("GH4MA2H26CC000000", "Mahindra", "SUV", 2009, 20, 500)
t = truck("MH4TB2H26CC000019", "Benz", "Ttuck",2010, 5, "15 Ton")

print("\n Vehicle class:")
print("\n VIN:", v.get_VIN(), "\n Make:", v.get_make(), "\n Model:", v.get_model(), "\n Year:", v.get_year(), "\n Mileage:", v.get_mileage())
print("\n Car class:")
print("\n VIN:", c.get_VIN(), "\n Make:", c.get_make(), "\n Model:", c.get_model(), "\n Year:", c.get_year(), "\n Mileage:", c.get_mileage())
print("\n Truck class:")
print("\n VIN:", t.get_VIN(), "\n Make:", t.get_make(),"\n Model:", t.get_model(), "\n Year:", t.get_year(),"\n Mileage:", t.get_mileage())