def menu():
    """Visar en meny med alternativ för användaren och tar emot input"""

    print("1) Add Contact")
    print("2) Remove Contact")
    print("3) Update Contact")
    print("4) Display Contacts")
    print("5) Search Contact")
    print("0) Exit")
    print("------------------")


    user_choise=input("vad vill du göra? välj mellan 0-5 ")
    return user_choise
adress_book = {}

def add():
    """Lägger till en ny kontakt i adressboken med namn, telefonnummer, e-post och adress."""

    print("Vad är ditt namn?")
    name = input(" ")
    
    print("Vad är ditt telefonnummer?")
    tel = input(" ")

    print("Vad är ditt email?")
    email = input(" ")

    print("Vad är din adress?")
    address = input(" ")
    
    adress_book[name] = {
        "phone": tel,
        "email": email,
        "address": address
    }
    print(f"\nKontakt för {name} har lagts till!")

def ta_bort():
    """Tar bort en kontakt från adressboken efter användar input."""

    if not adress_book:
        print("Det finns inga kontakter att ta bort.")
        return

    namnet_som_ska_bort = input("Ange namnet på kontakten du vill ta bort: ")
    
    bort_namn = None
    for namn_adress in adress_book:
        if namn_adress.lower() == namnet_som_ska_bort.lower():
            bort_namn = namn_adress
            break

    if bort_namn:
        del adress_book[bort_namn]
        print(f"Kontakten '{bort_namn}' har tagits bort!")
    else:
        print(f"Kontakten '{namnet_som_ska_bort}' kunde inte hittas.")

def display_contacts():
    """Visar alla kontakter som finns lagrade i adressboken."""

    if not adress_book:
        print("\nAdressboken är tom.")
    else:
        print("\n--- Alla kontakter ---")
        for name, info in adress_book.items():
            print(f"Namn: {name}")
            print(f"  Telefon: {info['phone']}")
            print(f"  Email: {info['email']}")
            print(f"  Adress: {info['address']}")
            print("-" * 20)

def uppdatera():
    """Uppdaterar en kontakt som finns i adressboken genom att ändra dess uppgifter."""

    if not adress_book:
        print("Det finns inga kontakter att ta bort.")
        return

    namn_som_ska_ändras = input("Ange namnet på kontakten du vill uppdatera: ")
    
    bort_namn = None
    for namn_adress in adress_book:
        if namn_adress.lower() == namn_som_ska_ändras.lower():
            bort_namn = namn_adress
            break

    if not bort_namn:
        print("namnet kunnde inte hittas")
        return
    
    kontakt= adress_book[bort_namn]

    print("nurvarnde uppgifter")
    print("phone", kontakt["phone"])
    print("email", kontakt["email"])
    print("address", kontakt["address"])

    print("skriv in dina nya detaljer")
    ny_tel=input("skriv in ditt nya tel ")
    if ny_tel:
        kontakt["phone"]=ny_tel
    ny_email=input("skriv in ditt nya mail ")
    if ny_email:
        kontakt["email"]=ny_email
    ny_address=input("skriv in dina nya address")
    if ny_address:
        kontakt["address"]=ny_address

    print("uppfigterna har uppdaterads")

def söka():
    """denna funktionen tar emot input från användaren och går igenom adress_book för att retunera en kontakt"""
    if not adress_book:
        print("Det finns inga kontakter att ta bort.")
        return

    hitta_namn = input("Ange namnet på kontakten du vill söka: ")
    
    
    hitta = False
    for name, kontakt in adress_book.items():
        if hitta_namn in name.lower():
            print("namn", name)
            print("phone", kontakt ["phone"] )
            print("email", kontakt ["email"] )
            print("address", kontakt ["address"] )
            hitta=True
    if not hitta:
        print("kunde inte hitta kontkaten")

def main():
    """ detta är main funktinen som har alla funktioner i sig"""

    while True:
        val=menu()
        if val=="1":
            add()

        elif val=="2":
           ta_bort()

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