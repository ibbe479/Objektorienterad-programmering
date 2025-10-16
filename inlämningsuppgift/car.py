from vehicle import Vehicle

class Car(Vehicle):
    def __init__(self, reg_nmr: str, brand: str, model: str, year: int, fuel_type: str, seats: int, is_automatic: bool):
        super().__init__(reg_nmr, brand, model, year, fuel_type)
        self.__seats = seats
        self.__is_automatic = is_automatic

    def calc_rental_price(self, days: int) -> float:
        if self.__seats <= 4 and self.__is_automatic == True: 
            return 300.0 * days
        
        elif self.__seats <= 7 and self.__is_automatic == True:
            return 400.0 * days
        
        elif self.__seats <= 4 and self.__is_automatic == False:
            return 250.0 * days
        
        elif self.__seats <= 7 and self.__is_automatic == False:
            return 350.0 * days
        
        
        

    def get_seats(self) -> int:
        return self.__seats

    def get_is_automatic(self) -> bool:
        return self.__is_automatic

    def __str__(self) -> str:
        transmission = "Automatic" if self.__is_automatic else "Manual"
        return f"{super().__str__()}, Seats: {self.__seats}, Transmission: {transmission}"

    

    