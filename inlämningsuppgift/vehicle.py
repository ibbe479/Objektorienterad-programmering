from abc import ABC, abstractmethod

class Vehicle(ABC):
    def __init__(self, reg_nmr: str, brand: str, model: str, year: int, fuel_type: str):
        self.reg_nmr = reg_nmr
        self.brand = brand
        self.model = model
        self.year = year
        self.fuel_type = fuel_type

    @abstractmethod
    def calc_rental_price(self, days: int) -> float:
        pass

    def get_reg_nmr(self) -> str:
        return self.reg_nmr
   
    def set_reg_nmr(self, reg_nmr: str) -> None:
        self.reg_nmr = reg_nmr
   
    def get_brand(self) -> str:
        return self.brand
    
    def set_brand(self, brand: str) -> None:
        self.brand = brand

    def get_model(self) -> str:
        return self.model

    def set_model(self, model: str) -> None:
        self.model = model

    def get_year(self) -> int:
        return self.year

    def set_year(self, year: int) -> None:
        self.year = year

    def get_fuel_type(self) -> str:
        return self.fuel_type

    def set_fuel_type(self, fuel_type: str) -> None:
        self.fuel_type = fuel_type

    def __str__(self) -> str:
        return f"{self.brand} {self.model} ({self.year}) - Reg: {self.reg_nmr}, Fuel: {self.fuel_type}"