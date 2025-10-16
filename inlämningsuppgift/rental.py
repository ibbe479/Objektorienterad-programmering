from cargogo import Cargogo
from vehicle import Vehicle


class Rental:

    def __init__(self):
        self.__cargogo = Cargogo()
    
    def show_menu(self) -> None:
        print("1. Add Vehicle")
        print("2. Remove Vehicle")
        print("3. Show All Vehicles")
        print("4. Search Vehicle by Registration Number")
        print("5. rent out a vehicle")
        print("0. Exit")

    def run(self) -> None:
        while True:
            self.show_menu()
            choice = input("Choose an option: ")

            if choice == "1":
                reg_nmr = input("Enter registration number: ")
                brand = input("Enter brand: ")
                model = input("Enter model: ")
                year = int(input("Enter year: "))
                fuel_type = input("Enter fuel type: ")
                vehicle_type = input("Enter vehicle type (car/truck): ").lower()

                kwargs = {}
                if vehicle_type == "car":
                    kwargs["seats"] = int(input("Enter number of seats (Max: 7 seats): "))
                    kwargs["is_automatic"] = input("Is it automatic? (yes/no): ").strip().lower() == "yes"

                elif vehicle_type == "truck":
                    kwargs["cargo_size"] = float(input("Enter cargo size in m³: "))
                else:
                    print("Invalid vehicle type.")
                    continue 
                self.__cargogo.add_vehicle(reg_nmr, brand, model, year, fuel_type, vehicle_type, **kwargs)
     
            elif choice == "2":
                print("Removing vehicle !")
                reg_nmr = input("Enter registration number to remove: ")
                self.__cargogo.remove_vehicle(reg_nmr)

            elif choice == "3":
                self.__cargogo.show_vehicles()

            elif choice == "4":
                reg_nmr = input("Enter registration number to search: ")
                vehicle = self.__cargogo.search_vehicle(reg_nmr)
                if vehicle:
                    print(vehicle)
                else:
                    print("Vehicle not found.")
            
            elif choice == "5":
                reg_nmr = input("Enter registration number to rent: ")
                days = int(input("Enter number of days to rent: "))
                self.__cargogo.rent_vehicle(reg_nmr, days)
            
            elif choice == "0":
                break

            else:
                print("Invalid choice. Please try again.")
                
if __name__ == "__main__":
    rental_system = Rental()
    rental_system.run()
    