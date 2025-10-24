from vehicle import Vehicle
from car import Car
from truck import Truck

class Cargogo():
    def __init__(self):
        self.__vehicles = []

    def add_vehicle(self, reg, brand, model, year, fuel, type,**kwargs) -> None:
        print("Adding vehicle !")    
        
        if type.lower() == "car":
            seats = kwargs.get("seats")
            is_automatic = kwargs.get("is_automatic")
            vehicle = Car(reg, brand, model, year, fuel, seats, is_automatic)
            self.__vehicles.append(vehicle)
            print(f"Car with registration number {reg} added.")

        elif type.lower() == "truck":
            cargo_size = kwargs.get("cargo_size")
            vehicle = Truck(reg, brand, model, year, fuel, cargo_size)
            self.__vehicles.append(vehicle)
            print(f"Truck with registration number {reg} added.") 

        else:
            print("Choose either car or truck as vehicle type.")
        
        print("Vehicle added successfully.")
    
    def remove_vehicle(self, reg_nmr: str) -> None:
        removed = False
        for bil in self.__vehicles:
            if bil.get_reg_nmr() == reg_nmr:
                self.__vehicles.remove(bil)
                removed = True
                print(f"Vehicle with registration number {reg_nmr} removed.")
        if not removed:
            print(f"No vehicle found with registration number {reg_nmr}.")
    
    def show_vehicles(self) -> None:
        if not self.__vehicles:
            print("No vehicles available.")
        else:
            for bil in self.__vehicles:
                if isinstance(bil, Car):
                    print(f"- {bil} {bil.calc_rental_price(1)} SEK/day")
                elif isinstance(bil, Truck):
                    print(f"- {bil} {bil.calc_rental_price(1)} SEK/day")

    

    def search_vehicle(self, reg_nmr: str) -> Vehicle:
        for bil in self.__vehicles:
            if bil.get_reg_nmr().lower() == reg_nmr:
                return bil
        print(f"No vehicle found with registration number {reg_nmr}.")
        return None
    

    def rent_vehicle(self, reg_nmr: str, days: int) -> None:
        vehicle = self.search_vehicle(reg_nmr)
        if vehicle:
            price = vehicle.calc_rental_price(days)
            print(f"Vehicle: {vehicle.get_reg_nmr()} ({vehicle.get_brand()} {vehicle.get_model()}) rented for {days} days. Total price: {price} SEK.")
        else:
            print(f"Cannot rent vehicle with registration number {reg_nmr}. It does not exist.")