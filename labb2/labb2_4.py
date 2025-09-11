

class dog :
    """
    detta är som innhåller namn, ras, ålder, om hunden sover och vilken färg 
    klassen inehåller även funkrioner som visar info om hunden och visar färgen och pälsen på hunden.
    """
    def __init__(self, name, breed, age, asleep, color):
        self.name = name
        self.breed = breed
        self.age = age
        self.asleep = asleep
        self.color = color
    
    def __str__(self):
        return(f"namn: {self.name} ras: {self.breed} ålder: {self.age} sover hunden {self.asleep} färg: {self.color}")
    
    '''
    def se_info(self):
        """this will print out info"""
        return f"mitt namn är {self.name} och jag är {self.age} år gammal"
    '''
    def show_fur_and_color(self):
        """show waht color the dog have"""
        return f"färgena på {self.name} är {self.color} "
    
    

Doug= dog("Doug", "Pug", 8, True, "black white beige")
Max= dog ("Max", "pug", 6, True, "svart")
Bob = dog("Bob", "ptibull", 5, False, "vit")
Alex=dog("alex", "bulldog", 9, True, "vit och svart")
sett=dog("Sett", "pitbull", 6, False, "vit och grå")
print(Doug)

dogs=[Doug, Max, Bob, Alex, sett]


def visa_all_info_om_hunden():  
    """visar info genom att loopa i listan"""
    for hund in dogs:
        print(hund)
        print(hund.show_fur_and_color())

visa_all_info_om_hunden()