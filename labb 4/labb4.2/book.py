class Book:
    def __init__(self, isbn, titel, author, price):
        self.__isbn=isbn
        self.__titel=titel
        self.__author=author
        self.__price=price

    def get_isbn(self):
        return self.__isbn
    
    def set_isbn(self, ny_isbn):
        self.__isbn=ny_isbn

    def get_titel(self):
        return self.__titel
    
    def set_titel(self, ny_titel):
        self.__titel=ny_titel

    def get_author(self):
        return self.__author
    
    def set_author(self, ny_author):
        self.__author=ny_author

    def get_price(self):
        return self.__price

    def set_price(self, ny_price):
        self.__price=ny_price

    def __str__(self):
        return f"isbn nummer är: {self.__isbn}, titel är {self.__titel}, författare är {self.__author}, och priset är {self.__price}"
        