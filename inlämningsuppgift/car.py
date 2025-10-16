from vehicle import Vehicle

class Car(Vehicle):
    def __init__(self, reg_nmr: str, brand: str, model: str, year: int, fuel_type: str, seats: int, is_automatic: bool):
        super().__init__(reg_nmr, brand, model, year, fuel_type)
        self.seats = seats
        self.is_automatic = is_automatic

    def calc_rental_price(self, days: int) -> float:
        pass

    def get_seats(self) -> int:
        return self.seats
    
    def set_seats(self, seats: int) -> None:
        self.seats = seats

    def get_is_automatic(self) -> bool:
        return self.is_automatic

    def set_is_automatic(self, is_automatic: bool) -> None:
        self.is_automatic = is_automatic

    def __str__(self) -> str:
        transmission = "Automatic" if self.is_automatic else "Manual"
        return f"{super().__str__()}, Seats: {self.seats}, Transmission: {transmission}"

    

    