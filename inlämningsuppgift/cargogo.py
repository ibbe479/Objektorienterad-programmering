from vehicle import Vehicle
from car import Car
from truck import Truck

class Cargogo(Vehicle):
    def __init__(self):
        self.show_vehicles = []

    def add_vehicle(self, vehicle: Vehicle) -> None:
        pass
    
    def remove_vehicle(self, reg_nmr: str) -> None:
        pass

    def update_vehicle(self, reg_nmr: str, new_vehicle: Vehicle) -> None:
        pass
    
    def show_vehicles(self) -> None:
        pass

    def searcjh_vehicle(self, reg_nmr: str) -> Vehicle | None:
        pass