
hund={
    "namn": "Doug",
    "ras":"pug",
    "ålder": 8,
    "sover": False,
    "färg":["svart", "vit", "beige"]
}
 
def print_info():
    """här kommer hundens info att skrivas """    
    print (f"woof! i'm {hund['namn']} the {hund['ras']} ({hund['ålder']} år)") 

def is_dog_asleep1():
    """kollar om hunder sover eller inte"""
    if hund["sover"]==True:
        #om hunden sover
        print(f"{hund['namn']} sover")
    else:
        #om hunder är vaken
        print(f"{hund['namn']} är vaken")

def wake_up_dog1():
    """kollar om hunder sover och får den att vakna"""
    if hund["sover"]==True:
        #om hunden sover 
        hund["sover"]=False
        print(f"{hund['namn']} är vaken nu")
    else:
        #om hunden redan är vakne
        print(f"{hund['namn']} är redan vaken")

def make_dog_go_to_sleep1():
    """kollar om hunden är vaken och får den att somna """
    if hund["sover"]!=True:
        #om hunden är vaken 
        hund["sover"]=True
        print(f"{hund['namn']} har somnat")
    else:
        #om hunden redan är vakne
        print(f"{hund['namn']} sover redan")

def show_fur_and_color1():
    """visar vilka fägrer hunden har"""
    print(f"{hund['namn']} har färgerna {hund['färg']}")

        
print_info()
is_dog_asleep1()
wake_up_dog1()
make_dog_go_to_sleep1()
show_fur_and_color1()


