# movie.py
class Movie:
    def __init__(self, title, year):
        self.__title = title
        self.__year = year

    def get_title(self):
        return self.__title

    def get_year(self):
        return self.__year

    def set_title(self, new_title):
        self.__title = new_title

    def set_year(self, new_year):
        self.__year = new_year

    def __str__(self):
        return f"{self.__title} ({self.__year})"