class product: 
    def __init__(self, product_nummber, name, price):
        self.product_nummber = product_nummber
        self.name = name
        self.price = price

    def see_product_nr(self): 
        return f"the  product number is {self.product_nummber}"
    
    def see_name(self):
        return f"the name  of this product is {self.name}"
    
    def see_price(self):
        return f"the price for tis profuct is {self.price}"
    
    def __str__(self):
        return f"the product nummber is {self.product_nummber} and the name for the product is {self.name} and the price is {self.price}"