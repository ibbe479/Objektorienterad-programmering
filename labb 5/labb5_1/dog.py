from animals import Animal

class Dog(Animal):
    def __init__(self, name, age, food):
        super().__init__(name, age, food)
       

    def __str__(self):
        return super().__str__() 

    def talk(self):
        return "Voff"

