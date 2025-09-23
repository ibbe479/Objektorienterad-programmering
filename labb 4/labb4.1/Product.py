class product: 
    def __init__(self, product_nr, name, price):
        self._product_nr = product_nr
        self._name = name
        self._price = price

    def get_pro(self):
        return self._product_nr
    def set_pro(self,ny_pro):
        self._product_nr=ny_pro
        return ny_pro

    def get_name(self):
        return self._name
    def set_name(self,ny_name):
        self._name=ny_name
        return ny_name

    def get_price(self):
        return self._price
    def set_price(self, ny_price):
        self._price=ny_price

    def __str__(self):
        return f"the product nummber is {self._product_nr} and the name for the product is {self._name} and the price is {self._price}"
    
    