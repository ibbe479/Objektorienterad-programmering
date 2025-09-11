
class dog :

    """detta är som innhåller namn, ras, ålder, om hunden sover och vilken färg 
    classen inehåller även funktioner som att se info, se om hunden sver, få hunden att somna eller vakna, se fägen och pälsen på hudnen """

    def __init__(self, name, breed, age, asleep, color):
        self.name = name
        self.breed = breed
        self.age = age
        self.asleep = asleep
        self.color = color
    
    def __str__(self):
        return(f"namn: {self.name} ras: {self.breed} ålder: {self.age} sover hunden {self.asleep} färg: {self.color}")
    
    def se_info(self):
        """this will print out info"""
        return f"mitt namn är {self.name} och jag är {self.age} år gammal"

    def is_dog_asleep(self):
        """will chek if the dog is asleep with true or false"""
        if self.asleep == True:
            #if dog is sleeping
            return f"{self.name} sover just nu"
        else:
            #if dog is not sleeping
            return f"{self.name} är vaken"

    def wake_up_dog(self):
        """if dog is asleep(true) then make it false"""
        if self.asleep==True:
            #if dog is sleping
            self.asleep=False
            return f"nu är {self.name} vaken"
        else:
            #id dog is not sleeping
            return f"{self.name} är redan vaknen"



    def make_dog_go_to_sleep(self):
        """if dog is awake(false) then make it true"""
        if self.asleep!=True:
            #if dog is sleping
            self.asleep=True
            return f"nu har {self.name} sommant"
        else:
            #id dog is not sleeping
            return f"{self.name} sover redan"


    def show_fur_and_color(self):
        """show waht color the dog have"""
        return f"färgena på {self.name} är {self.color} "

Doug= dog("Doug", "Pug", 8, True, ["black", "white", "beige"])


"""print(Doug.se_info())
print(Doug.is_dog_asleep())
print(Doug.wake_up_dog())
print(Doug.make_dog_go_to_sleep())
print(Doug.show_fur_and_color())"""