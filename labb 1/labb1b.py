library_catalog = {
    "The Great Gatsby": {
        "author": "F. Scott Fitzgerald",
        "year_published": 1925,
        "genre": "Classic Fiction",
        "ISBN": "978-0743273565",
        "summary": "A portrait of the Jazz Age in all of its decadence and excess, Gatsby believed in the green light, the orgastic future that year by year recedes before us."
    },
    "Pride and Prejudice": {
        "author": "Jane Austen",
        "year_published": 1813,
        "genre": "Romance Novel",
        "ISBN": "978-1986431484",
        "summary": "A tale of love and values unfolds in the class-conscious England of the late 18th century. The five Bennet sisters - including strong-willed Elizabeth and young Lydia - have been raised well aware of their mother's fixation on finding them husbands and securing set futures."
    }
}

def menu():
    """Visar en meny med alternativ för användaren och tar emot input"""

    print("1) Add Book")
    print("2) Remove Book")
    print("3) Update Book Details")
    print("4) Display All Books")
    print("5) Search for a Book")
    print("0) Exit")
    print("------------------")


    user_choise=input("vad vill du göra? välj mellan 0-5 ")
    return user_choise

def add_book():
    print("lägg till information om din ny bok")
    namn = input("vad heter boken? ").lower()
    författare = input("vad heter förfataren? ").lower() 
    år= input("vilket åt publicerades den? ").lower()
    kategori = input("vilken typ av kategori är boken? ").lower()
    isbn = input("ISBN nummer: ").lower()
    sammanfatning = input("sammanfattning: ").lower()
    try:
        library_catalog[namn]={
            "author": författare,
            "year_published":år,
            "genre": kategori,
            "ISBN": isbn,
            "summary": sammanfatning
        }


    except: 
        print("ett fel uppstog försök igen")  

def ta_bort_en_bok():
    if not library_catalog:
        print("Det finns inga kontakter att ta bort.")
        return
    
    boken_som_ska_bort=input("vad heter boken som du vill ta bort? ")
    try:
        boken_som_ska_bort=None
        for varej_bok in library_catalog:
            if varej_bok == boken_som_ska_bort:
                boken_som_ska_bort=varej_bok
                break
        print(f"{boken_som_ska_bort} har tagit sbort")
    except:
        print(f"kunde inte ta bort {boken_som_ska_bort} försök igen")
    
def  uppdatera():
    if not library_catalog:
        print("Det finns inga böcker att ta uppdatera.")
        return
        
    print("uppdatera information om din bok")
    

    bok = input("vilken bok vill du uppdatera? ")
    print(f"du ändarar i {library_catalog[bok]}")#måste fixa denna
    if bok not in library_catalog:
            print(f"Boken '{bok}' finns inte i katalogen.")
            return
    
    print("1) ändra författare")
    print("2) ändra år publicerad")
    print("3) ändra kategori")
    print("4) ändra ISBN nummer")
    print("5) ändra sammanfattning")
    print("------------------")
    
    try:  
        val=input("vad vill du ändra? välj mellan 1-5? ")
        if val=="1":
            ny_författare=input("vad är den nya författaren? ")
            library_catalog[bok]["author"]=ny_författare
        elif val=="2":
            nyyt_år=input("vad är det nya året? ")
            library_catalog[bok]["year_published"]=nyyt_år
        elif val=="3":
            ny_kategori=input("vad är den nya kategorin? ")
            library_catalog[bok]["genre"]=ny_kategori
        elif val=="4":
            ny_isbn=input("vad är det nya ISBN numret? ")
            library_catalog[bok]["ISBN"]=ny_isbn
        elif val=="5":
            ny_sammanfatning=input("vad är den nya sammanfattningen? ")
            library_catalog[bok]["summary"]=ny_sammanfatning
        else:
            print("du måste välja mellan 1-5")
        print("uppfigterna har uppdaterads")
    except:
        print(f"kunde inte ta bort {bok} försök igen")

def display_contacts():
    """Visar alla kontakter som finns lagrade i adressboken."""

    if not library_catalog:
        print("bibloteket är tomt.")
    else:
        print("\n--- Alla kontakter ---")
        for name, info in library_catalog.items():
            print(f"Namn: {name}")
            print(f"  författare: {info['author']}")
            print(f"  år: {info['year_published']}")
            print(f"  kategori: {info['genre']}")
            print(f"  ISBN: {info['ISBN']}")
            print(f"  sammanfattnig: {info['summary']}")
            print("-" * 20)


def main():
    while True:
        val=menu()
        if val=="1":
            add_book()

        elif val=="2":
           ta_bort_en_bok()

        elif val=="3":
           uppdatera()

        elif val=="4":
          display_contacts()

        elif val=="5":
            söka()

        elif val=="0":
            break
        
        else:
            print(f"du måste välja mellan 0-5 \n")

main()