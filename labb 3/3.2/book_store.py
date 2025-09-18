from book_inventory import Book_inventory

class Book_store: 
    def __init__(self):
        self.__books_invetory = Book_inventory()

    def show_menu(self):
        print("\nMenu:")
        print("1. Lägg till en bok")
        print("2. visa böker")
        print("3. uppadtera priset på en bok")
        print("4. ta bort en bok ")
        print("5. avsluta programmet")

    def run(self):
        while True:
            self.show_menu()
            val= input("vad vill du göra? ")
            

            if val=="1":
                print("lägg till en produkt")
                isbn=input("vad är är ISBN nummret för boken?:" )
                titel=input("vad heter boken?: ")
                author=input("vad heter författaren?: ")
                price=input("vad kostar boken?: ")

                self.__books_invetory.add_book(isbn,titel,author,price)

            elif val == "2":
                print("visar produkterna")
                self.__books_invetory.show_all()

            elif val == "3":
                print("print uppdatera priset")
                isbn=input("skriv in artikelnummret på boken du vill ändra priset på: ")
                nya_priset = input("vad är det nya priset:? ")
                self.__books_invetory.uppdate(isbn, nya_priset)
                
            elif val == "4":
                print("raderar en bok")
                isbn=input("skriv in isbn nummret på boken du vill radera: ")
                self.__books_invetory.delete(isbn)
                
            elif val == "5":
                print("hejdå")
                break

            else:
                print("oglitigt val försök igen")



if __name__ == "__main__":
    program = Book_store()
    program.run()


