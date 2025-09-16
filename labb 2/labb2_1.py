class dog :
    def __init__(self, name, breed, age, asleep, color):
        self.name = name
        self.breed = breed
        self.age = age
        self.asleep = asleep
        self.color = color
    
    def __str__(self):
        return(f"namn: {self.name} ras: {self.breed} ålder: {self.age} sover hunden {self.asleep} färg: {self.color}")
    
    def show_info(self):
        pass

    def is_dog_asleep(self):
        """kollar om v'r """
        pass

    def wake_up_dog():
        pass

    def make_dog_go_to_slepp():
        pass

    def show_dog_fur_color():
        pass

Doug= dog ("Doug", "pug", 8, False,"black, white and beige"  )

print(Doug)

