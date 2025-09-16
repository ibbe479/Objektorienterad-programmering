# main.py
from movie_collection import MovieCollection

class MovieProgram:
    def __init__(self):
        self.__collection = MovieCollection()  # composition: owns MovieCollection

    def show_menu(self):
        print("\nMenu:")
        print("1. Add Movie")
        print("2. Show Movies")
        print("3. Search Movie")
        print("4. Remove Movie")
        print("5. Update Movie")
        print("6. Exit")

    def run(self):
        while True:
            self.show_menu()
            choice = input("Choose an option: ")

            if choice == "1":
                title = input("Enter movie title: ")
                year = input("Enter movie year: ")
                self.__collection.add_movie(title, year)
            elif choice == "2":
                self.__collection.show_movies()
            elif choice == "3":
                keyword = input("Enter search keyword: ")
                self.__collection.search_movie(keyword)
            elif choice == "4":
                title = input("Enter title to remove: ")
                self.__collection.remove_movie(title)
            elif choice == "5":
                old_title = input("Enter the title of the movie to update: ")
                new_title = input("Enter new title: ")
                new_year = input("Enter new year: ")
                self.__collection.update_movie(old_title, new_title, new_year)
            elif choice == "6":
                print("Goodbye!")
                break
            else:
                print("Invalid choice. Try again.")

if __name__ == "__main__":
    program = MovieProgram()
    program.run()
