from book import Book

class Book_inventory:  
    def __init__(self):
        self.__books_list = [ ]
    
    def add_book(self, isbn, titel, author, price):
        isbn= int(isbn)
        price=int(price)
        #den tar och lägger in i klassen Book
        ny_bok=Book(isbn, titel, author, price)
        self.__books_list.append(ny_bok)
        print("boken är tillagd")


        """if isbn == self.__books_list[isbn]"""
        """ if isbn == self.books_list.:
                print(f"detta isbn nummret finns redan ")
            elif isbn != Book.get_isbn():
                ny_bok=Book_inventory(isbn, titel, author, price)
                self.books_list.append(ny_bok)

        """
    def show_all(self):
        if not self.__books_list:
            print("det finns inga böker än")
        else: 
            for böcker in self.__books_list:
                print (f"isbn nummret är: {böcker.get_isbn()} titeln är {böcker.get_titel()} författaren är {böcker.get_author()} och priset är {böcker.get_price()}")

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
    
        