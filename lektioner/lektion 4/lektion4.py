"""
singel inheritance
class dog:
    def __init__(self, name, age):
        pass
    
    class hund(dog): hund kommer vara en subklass till dog attlså barnet till dog
        def __init__(self, name, age, breed):
            pass
    
    class person:
        def __init__(self, name, age):
            pass
    
    class student(person): student kommer vara en subklass till person attlså barnet till person
        def __init__(self, name, age, student_id):
            super().__init__(name, age) #anropar init metoden från person klassen
            self.student_id = student_id

    multi inheritance

    class father:
        def __init__(self, name):
            self.name = name
    class mother:
        def __init__(self, name):
            self.name = name
        
    class child(father, mother): child kommer vara en subklass till både father och mother
        def __init__(self, name, age):
            father.__init__(self, name) #anropar init metoden från father kl
            mother.__init__(self, name) #anropar init metoden från mother klassenassen
            self.age = age

    hierarchical inheritance
    class vihicle:
        def __init__(self, brand, model):
            self.__lisence_plate = licence_plate #private attribute

            def get_licence_plate(self): #getter method
                return self.__licence_plate
        
    class car(vihicle): car kommer vara en subklass till vihicle
        def __init__(self, brand, model, doors):
            super().__init__(brand, model) #anropar init metoden från vihicle klassen super används bara för att det finns en paretn klass
            self.doors = doors
        
    class truck(vihicle): truck kommer vara en subklass till vihicle
        def __init__(self, brand, model, capacity):
            super().__init__(brand, model) #anropar init metoden från vihicle klassen
            self.capacity = capacity
"""