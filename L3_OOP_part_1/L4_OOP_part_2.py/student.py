class student:
    def __init__(self, name, age):
        self._name = name
        self.age = age
       

    def __str__(self):
        return f"{self.name}, {self.age} år gammal"
    
ibbe = student ("Ibrahim", 25)

print(ibbe.name)  
print(ibbe.age)  