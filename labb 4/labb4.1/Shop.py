from Inventory import inventory
from Laptop import laptop
from Smartphone import smartphone


class shop: 
    def __init__(self):
        self._collection = inventory()
        

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
                print("är det en laptop eller smartphone du vill lägga till?")
                tel_lapt=input("laptop/smartphone: ")   
                kwargs = {} 
                
                if tel_lapt.lower() == "laptop":
                    kwargs["screen_size"]= input("hur stor är skärmen? ")
                    kwargs["processor"]= input("vilken processor har den? ")


                elif tel_lapt.lower() == "smartphone":
                    kwargs["storage"]= input("hur mycket lagring har den? ")
                    kwargs["os"]= input("vilket operativsystem har den? ")
                else:
                    print("ogiltigt val, försök igen.")
                    continue
                ram= input("hur mycket ram har den? ")
                
                self._collection.add_product(prod_nr, namnet, priset, tel_lapt, ram, **kwargs)

            elif val == "2":
                print("visar produkterna")
                self._collection.show_all()

            elif val == "3":
                print("raderar en produkt")
                art_nummer=input("skriv in artikelnummret du vill radera: ")
                self._collection.delete(art_nummer)
                
            elif val == "4":
                print("print uppdatera priset")
                prod_nr=input("vad är produckt nummret: ")
                nya_priset=input("vad är det nya priset du vill lägga in ")
                self._collection.uppdate_price(prod_nr, nya_priset)

            elif val == "5":
                print("hejdå")
                break

            else:
                print("oglitigt val försök igen")



if __name__ == "__main__":
    program = shop()
    program.run()


