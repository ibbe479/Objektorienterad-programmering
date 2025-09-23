from book import Book

class Textbook (Book):
    def __init__(self, isbn, titel, author, price, subject, edition):
        super().__init__(isbn, titel, author, price)  
        self.__subject = subject
        self.__edition = edition

    def get_subject(self):
        return self.__subject
    def set_subject(self, ny_subject):
        self.__subject = ny_subject
        return ny_subject
    
    def get_edition(self):
        return self.__edition   
    def set_edition(self, ny_edition):
        self.__edition = ny_edition
        return ny_edition

    def __str__(self):
        return f"{super().__str__()}, Subject: {self.__subject}, Edition: {self.__edition}"