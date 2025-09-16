"""
ANTECKINKGAR 
objket är saker som har atributer och metoder (är instanser av klasser)
klasser sammling av atributer och metoder (är bluprints för objekter) 

__init__ är en speciell metod som körs när en ny instans av klassen skapas
self är en referens till den aktuella instansen av klassen, används för att komma åt objektets atributer och metoder
__init__ OCH self måste vara med i en klass allt annat är valfritt

__str__ är en speciell metod som definierar hur objektet ska representeras som en sträng
__repr__ är en speciell metod som definierar en officiell strängrepresentation av objektet, används ofta för debugging

stub class är en tom klass som används som en plats hållare för framtida kod, alltså användes när du inte vet vad klassen kommer 
att innehålla än, gör att koden blir enklare att testa och utveckla i små steg
ett exempel på en stub class är:
class MyClass:
    pass

__init__ (self, name)
    self.name = name
    detta är publick atributer

__init__ (self, name):
    self.__name = name
    detta är private atributer

    private atributer kan inte nås utanför klassen, används för att skydda data
    publick atributer kan nås utanför klassen, används för att dela data
    __ två streck gör atributet privat
    _ ett streck gör atributet "protected" (kan nås av subklasser)
"""

class Book:
    def __init__(self, titel , författare):
        self.titel = titel
        self.författare = författare

    def __str__(self):
        return f"'{self.titel}' av {self.författare}"
    
    #create a book object
book1 = Book("1984", "George Orwell")
print(book1)  # Output: '1984' av George Orwell



class person:
    def __del__ (self):
        print(f"{self.namn} har tagit bort")

#exepmel två (libaryBook)
class book:
    def __init__(self,titel ,year, authotr):
        self.titel = titel
        self.year = year
        self.author = authotr

        def set_titel(self, titel):
            pass
        def set_year(self, year):
            pass
        def set_author(self, author):
            pass

        def __str__(self):
            return f"{self.namn}, {self.ålder} år gammal"