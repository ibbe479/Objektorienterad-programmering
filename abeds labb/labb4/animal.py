from abc import ABC, abstractmethod
class Animal(ABC):
    
    def __init__(self, name, age, food):
        self.__name = name
        self.__age = age
        self.__food = food
    
    def get_name(self):
        return self.__name
    
    def get_age(self):
        return self.__age
    
    def get_name(self):
        return self.__food
    
    def set_name(self, new_name):
        self.__name = new_name

    def set_age(self, new_age):
        self.__name = new_age
    
    def set_food(self, new_food):
        self.__name = new_food

    def add_food(self, food):
        self.__food.append(food)
    
    def remove_food(self, food):
        if food in self.__food:
            self.__food.remove(food)
    
    @abstractmethod
    def talk(self):
        pass

class Fish(Animal):

    def talk(self):
        return "Blub Blub"
    

class Cow(Animal):

    def talk(self):
        return "Muuuuuuuuuuuuuuuuuuuuuu"
    
class Dog(Animal):

    def talk(self):
        return "Woof Woof"
    
class Cat(Animal):

    def talk(self):
        return "Meow Meow"
    

if __name__ == "__main__":
    bob = Cat("bob", 10, "food")
    pak = Dog("Pak", 1, "bones")
    nemo = Fish("Nemo", 2, "eggs")
    mu = Cow("Mu", 1, "grass")


    animals = [bob, pak, nemo, mu]

    for animal in animals:
        print(animal.talk())