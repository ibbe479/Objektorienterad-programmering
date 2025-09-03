def menu():
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
    print("Vad är ditt namn?")
    name = input(" ")
    
    print("Vad är ditt telefonnummer?")
    tel = input(" ")

    print("Vad är ditt email?")
    email = input(" ")

    print("Vad är din adress?")
    address = input(" ")
    
    # Stavfelet är korrigerat här från "addres" till "address"
    adress_book[name] = {
        "phone": tel,
        "email": email,
        "address": address
    }
    print(f"\nKontakt för {name} har lagts till!")

def ta_bort():
    if not adress_book:
        print("Det finns inga kontakter att ta bort.")
        return

    name_to_remove = input("Ange namnet på kontakten du vill ta bort: ")
    
    bort_namn = None
    for namn_adress in adress_book:
        if namn_adress.lower() == name_to_remove.lower():
            bort_namn = namn_adress
            break

    if bort_namn:
        del adress_book[bort_namn]
        print(f"Kontakten '{bort_namn}' har tagits bort!")
    else:
        print(f"Kontakten '{name_to_remove}' kunde inte hittas.")

def display_contacts():
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

def main():
    while True:
        val=menu()
        if val=="1":
            add()

        elif val=="2":
           ta_bort()

        elif val=="3":
            print("trean")
        
        elif val=="4":
          display_contacts()

        elif val=="5":
            print("feman")

        elif val=="0":
            print("sexan")
            break
        
        else:
            print(f"du måste välja mellan 0-5 \n")

main()