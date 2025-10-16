from vehicle import Vehicle

class Truck(Vehicle):
    def __init__(self, reg_nmr: str, brand: str, model: str, year: int, fuel_type: str, cargo_size: float):
        super().__init__(reg_nmr, brand, model, year, fuel_type)
        self.__cargo_size = cargo_size

    def calc_rental_price(self, days: int) -> float:
        if self.__cargo_size <= 10:
            base_price = 1500.0 
        elif self.__cargo_size <= 20:
            base_price = 2500.0
        else:
            base_price = 4000.0
        return base_price * days

    def get_cargo_size(self) -> float:
        return self.__cargo_size

    def __str__(self) -> str:
        return f"{super().__str__()}, Cargo Size: {self.__cargo_size} m³"
