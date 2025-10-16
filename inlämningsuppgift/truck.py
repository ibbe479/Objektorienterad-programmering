from vehicle import Vehicle

class Truck(Vehicle):
    def __init__(self, reg_nmr: str, brand: str, model: str, year: int, fuel_type: str, cargo_size: float):
        super().__init__(reg_nmr, brand, model, year, fuel_type)
        self.cargo_size = cargo_size

    def calc_rental_price(self, days: int) -> float:
       pass

    def get_cargo_size(self) -> float:
        return self.cargo_size

    def set_cargo_size(self, cargo_size: float) -> None:
        self.cargo_size = cargo_size

    def __str__(self) -> str:
        return f"{super().__str__()}, Cargo Size: {self.cargo_size} m³"
