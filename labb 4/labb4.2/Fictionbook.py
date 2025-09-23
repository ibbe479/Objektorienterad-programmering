from book import Book

class Fictionbook (Book):
    def __init__(self, titel, author, genre, age_rating , isbn, price):
        super().__init__(isbn, titel, author, price)  
        self.__genre = genre
        self.__year = age_rating
        
    def get_genre(self):
        return self.__genre
    def set_genre(self, ny_genre):
        self.__genre = ny_genre
        return ny_genre
    
    def get_age_rating(self):
        return self.__year
    def set_age_rating(self, ny_year):
        self.__year = ny_year
        return ny_year

    def __str__(self):
        return f"{super().__str__()}, Genre: {self.__genre}, Age Rating: {self.__year}"