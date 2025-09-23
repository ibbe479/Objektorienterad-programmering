from Product import product 

class smartphone(product):
    def __init__(self, product_nr, name, price, Ram, Storage, OS):
        super().__init__(product_nr, name, price)
        self._ram=Ram
        self._storage=Storage
        self._os=OS

    def get_ram(self):
        return self._ram
    def set_ram(self, ny_ram):
        self._ram=ny_ram
        return ny_ram
    
    def get_storage(self):
        return self._storage
    def set_storage(self, ny_storage):
        self._storage=ny_storage
        return ny_storage   
    
    def get_os(self):
        return self._os
    def set_os(self, ny_os):
        self._os=ny_os
        return ny_os
    
    def __str__(self):
        return f"{super().__str__()}, Ram: {self._ram}, Storage: {self._storage}, OS: {self._os}"
    
    