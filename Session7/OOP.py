#Object Oriented Programming (OOP)

#Everything that exists in Python evolves from an object
#Once we build a class, we can create objects from this class
#Style of programming based on objects

class Dog:
    #age,breed,size etc. are all attributes of the class
    def __init__(self, age, breed):
        self.age = age
        self.breed = breed

    def talk(self):
        return "Bark"


Jett = Dog(3,"pug")
print(Jett.talk())