from Inventory import inventory

class shop: 
    def __init__(self):
        self.collection = inventory()

    def show_menu(self):
        print("\nMenu:")
        print("1. Add product")
        print("2. Show products")
        print("3. Remove product")
        print("4. Update price")
        print("5. Exit")

    def run(self):
        while True:
            self.show_menu()
            val= input("vad vill du göra? ")
            

            if val=="1":
                print("lägg till en produkt")
                prod_nr=input("vad är produkt nummret? ")
                namnet= input("vad heter produkten? ")
                priset= input ("vad kostar varan? ")
                self.collection.add_product(prod_nr, namnet, priset)

            elif val == "2":
                print("visar produkterna")
                self.collection.show_all()

            elif val == "3":
                print("raderar en produkt")
                art_nummer=input("skriv in artikelnummret du vill radera: ")
                self.collection.delete(art_nummer)
                
            elif val == "4":
                print("print uppdatera priset")
                namn=input("vad heter produkten du vill uppdatrera priset på: ")
                nya_priset=input("vad är det nya priset du vill lägga in ")
                self.collection.uppdate_price(namn, nya_priset)
            elif val == "5":
                print("hejdå")
                break

            else:
                print("oglitigt val försök igen")



if __name__ == "__main__":
    program = shop()
    program.run()
