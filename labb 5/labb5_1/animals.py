from abc import  ABC, abstractmethod

class Animal(ABC):

    def __init__(self, name, age, food):
        self.__name = name
        self.__age = age 
        self.__food = food

    def get_name(self):
        return self.__name  
    def set_name(self, ny_name):
        self.__name = ny_name

    def get_age(self):
        return self.__age
    def set_age(self, ny_age):
        self.__age = ny_age

    def get_food(self):
        return self.__food
    def set_food(self, ny_food):
        self.__food = ny_food
    
    
    def __str__(self):
        return f"namn: {self.__name}, ålder: {self.__age}, mat: {self.__food}"

    @abstractmethod
    def talk(self):
        """funktionen som får djuret att prata """
        pass


    
if __name__ == "__main__":
    from cat import Cat
    from dog import Dog
    from fish import Fish

    cat1 = Cat("Misse", 3, "Kattmat")
    dog1 = Dog("Bosse", 5, "Hundmat")
    fish1 = Fish("Nemo", 1, "Fiskmat")

    djur = [cat1, dog1, fish1]
    for djuren in djur:
        print(djuren.talk())