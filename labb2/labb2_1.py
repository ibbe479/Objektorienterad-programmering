class dog :
    def __init__(self, name, breed, age, aspleep, color):
        self.name = name
        self.breed = breed
        self.age = age
        self.aspleep = aspleep
        self.color = color
    
    def __str__(self):
        print(f"namn: {self.name} ras: {self.breed} ålder: {self.age} sover hunden {self.aspleep} färg: {self.color}")

print(dog)