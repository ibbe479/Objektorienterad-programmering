# movie_collection.py
from movie import Movie

class MovieCollection:
    def __init__(self):
        self.__movies = []  # composition: owns Movie objects

    def add_movie(self, title, year):
        movie = Movie(title, year)   # creates Movie inside
        self.__movies.append(movie)

    def show_movies(self):
        if not self.__movies:
            print("No movies in the collection.")
        else:
            for movie in self.__movies:
                print(f"Movie title: {movie.get_title()} Year: ({movie.get_year()})")

    def search_movie(self, keyword):
        found = False
        for movie in self.__movies:
            if keyword.lower() in movie.get_title().lower():
                print(f"Movie title: {movie.get_title()} Year: ({movie.get_year()})")
                found = True
        if not found:
            print("No matching movies found.")

    def remove_movie(self, title):
        for i in range(len(self.__movies)):
            if self.__movies[i].get_title().lower() == title.lower():
                del self.__movies[i]
                print("Movie removed.")
                return
        print("Movie not found.")

    def update_movie(self, old_title, new_title, new_year):
        for movie in self.__movies:
            if movie.get_title().lower() == old_title.lower():
                movie.set_title(new_title)
                movie.set_year(new_year)
                print("Movie updated.")
                return
        print("Movie not found.")