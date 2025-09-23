from Product import product

class laptop(product):
    def __init__(self, product_nr, name, price, Ram, processor, screen_size):
        super().__init__(product_nr, name, price)
        self._ram=Ram
        self._processor=processor
        self._screen_size=screen_size
        

    def get_ram(self):
        return self._ram
    def set_ram(self, ny_ram):
        self._ram=ny_ram
        return ny_ram
    
    def get_processor(self):
        return self._processor  
    def set_processor(self, ny_processor):
        self._processor=ny_processor
        return ny_processor
    
    def get_screen_size(self):
        return self._screen_size
    def set_screen_size(self, ny_screen_size):
        self._screen_size=ny_screen_size
        return ny_screen_size
    
    def __str__(self):
        return f"{super().__str__()}, Ram: {self._ram}, Processor: {self._processor}, Screen size: {self._screen_size}"