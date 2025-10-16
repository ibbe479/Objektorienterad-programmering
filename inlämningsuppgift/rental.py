from cargogo import Cargogo
from vehicle import Vehicle
from car import Car
from truck import Truck


class Rental:

    def __init__(self):
        self.cargogo = Cargogo()
    
    def show_menu(self) -> None:
        print("1. Add Vehicle")
        print("2. Remove Vehicle")
        print("3. Update Vehicle")
        print("4. Show All Vehicles")
        print("5. Search Vehicle by Registration Number")
        print("6. Exit")

    def run(self) -> None:
        pass



if __name__ == "__main__":
    rental_system = Rental()
    rental_system.run()