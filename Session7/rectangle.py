class Vehicle:

    def __init__(self,make,model,colour,capacity,max_speed,fuel_tank):
        self.make = make
        self.model = model
        self.colour = colour
        self.capacity = capacity
        self.max_speed = max_speed
        self.fuel_tank = fuel_tank

    
    def __str__(self):
        return f"Vehicle Summary\nMake: {self.make}\nModel: {self.model}\nColour: {self.colour}\nCapacity: {self.capacity} people\nMax Speed: {self.max_speed} km/h\nFuel Tank: {self.fuel_tank} L"
    

my_car = Vehicle("Toyota","Hilux","Blue",5,200,250)

print(my_car)

    

