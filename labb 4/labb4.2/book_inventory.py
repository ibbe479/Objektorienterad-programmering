from book import Book
from Fictionbook import Fictionbook
from Textbook import Textbook   


class Book_inventory:  
    def __init__(self):
        self.__books_list = [ ]
    
    def add_book(self, isbn, titel, author, price, bok_typ, **kwargs ):
        isbn= int(isbn)
        price=int(price)
        
        if bok_typ.lower() == "fiction":
            genre= kwargs.get('genre')
            age_rating= kwargs.get('age_rating')
            ny_bok_f=Fictionbook(isbn, titel, author, genre, age_rating , price)
            self.__books_list.append(ny_bok_f)
        elif bok_typ.lower() == "textbook":
            subject= kwargs.get('subject')
            edition= kwargs.get('edition')
            ny_bok_t=Textbook(isbn, titel, author, price, subject, edition)
            self.__books_list.append(ny_bok_t)
        else:
            print("ogiltig bok typ")
        print("boken är tillagd")

    def show_all(self):
        if not self.__books_list:
            print("det finns inga böker än")
        else: 
            for böcker in self.__books_list:
                if isinstance(böcker, Fictionbook):
                    print (f"- {böcker}")
                elif isinstance(böcker, Textbook):
                    print (f"- {böcker}")

    def uppdate(self, isbn, ny_price):
        isbn=int(isbn)
        ny_price=int(ny_price)
        uppdatera=False
        for böcker in self.__books_list:
            if böcker.get_isbn()==isbn:
                böcker.set_price(ny_price)
                uppdatera=True
                print("priset är uppdaterad")
        if not uppdatera:
            print("priset kunde inte uppdateras")


    def delete(self, isbn):
        isbn=int(isbn)
        bortagen=False
        for böcker in self.__books_list:
            if böcker.get_isbn()==isbn:
                self.__books_list.remove(böcker)
                print("boken är borttagen")
                bortagen=True
                return
        if not bortagen:
            print("kunde inte ta bort boken")
    
        