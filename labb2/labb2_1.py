class dog :
    def __init__(self, name, breed, age, asleep, color):
        self.name = name
        self.breed = breed
        self.age = age
        self.asleep = asleep
        self.color = color
    
    def __str__(self):
        return(f"namn: {self.name} ras: {self.breed} ålder: {self.age} sover hunden {self.asleep} färg: {self.color}")
    
    def se_info():
        """this will print out info"""
        pass

    def is_dog_asleep():
        """will chek if the dog is asleep with true or false"""
        pass

    def wake_up_dog():
        """if dog is asleep(true) then make it false"""
        pass

    def make_dog_go_to_sleep():
        """if dog is awake(false) then make it true"""
        pass

    def show_fur_and_color():
        """show waht color the dog have"""
        pass


Doug= dog ("Doug", "pug", 8, False,"black, white and beige"  )

print(Doug)

