from book_inventory import Book_inventory
from Fictionbook import Fictionbook
from Textbook import Textbook


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
                print("lägg till en bok")
                isbn=input("vad är är ISBN nummret för boken?:" )
                titel=input("vad heter boken?: ")
                author=input("vad heter författaren?: ")
                price=input("vad kostar boken?: ")
                print("är det en fiction eller textbook du vill lägga till?")
                bok_typ=input("fiction/textbook: ")

                kwargs = {}

                if bok_typ.lower() == "fiction":
                    kwargs["genre"]= input("vilken genre är boken?: ")
                    kwargs["age_rating"]= input("vilken åldersgräns har boken?: ")

                elif bok_typ.lower() == "textbook":
                    kwargs["subject"]= input("vilket ämne handlar boken om?: ")
                    kwargs["edition"]= input("vilken upplaga är det?: ")
                else:
                    print("ogiltigt val, försök igen.")
                    continue

                self.__books_invetory.add_book(isbn,titel,author,price, bok_typ, **kwargs)

            elif val == "2":
                print("visar produkterna")
                self.__books_invetory.show_all()

            elif val == "3":
                print("print uppdatera priset")
                isbn=input("skriv in isbn nummret på boken du vill ändra priset på: ")
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


