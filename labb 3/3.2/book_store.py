from book_inventory import Book_inventory

class Book_store: 
    def __init__(self):
        self.__books_invetory = Book_inventory()

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
                isbn=input("vad är är ISBN nummret för boken?:" )
                titel=input("vad heter boken?: ")
                author=input("vad heter författaren?: ")
                price=input("vad kostar boken?: ")

                self.__books_invetory.add_book(isbn,titel,author,price)

            elif val == "2":
                print("visar produkterna")
                self.__books_invetory.show_all()

            elif val == "3":
                print("raderar en produkt")
                isbn=input("skriv in artikelnummret du vill radera: ")
                
                
            elif val == "4":
                print("print uppdatera priset")
                
            elif val == "5":
                print("hejdå")
                break

            else:
                print("oglitigt val försök igen")



if __name__ == "__main__":
    program = Book_store()
    program.run()


