from abc import ABC, abstractmethod

class Vehicle(ABC):
    def __init__(self, reg_nmr: str, brand: str, model: str, year: int, fuel_type: str):
        self.__reg_nmr = reg_nmr
        self.__brand = brand
        self.__model = model
        self.__year = year
        self.__fuel_type = fuel_type

    @abstractmethod
    def calc_rental_price(self, days: int) -> float:
        pass

    def get_reg_nmr(self) -> str:
        return self.__reg_nmr

   
    def get_brand(self) -> str:
        return self.__brand

    def get_model(self) -> str:
        return self.__model

    def get_year(self) -> int:
        return self.__year

    def get_fuel_type(self) -> str:
        return self.__fuel_type

    def __str__(self) -> str:
        return f"{self.__brand} {self.__model} ({self.__year}) - Reg: {self.__reg_nmr}, Fuel: {self.__fuel_type}"