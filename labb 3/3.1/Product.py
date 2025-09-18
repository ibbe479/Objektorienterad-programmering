class product: 
    def __init__(self, product_nummber, name, price):
        self.product_nummber = product_nummber
        self.name = name
        self.price = price

    
    
    def __str__(self):
        return f"the product nummber is {self.product_nummber} and the name for the product is {self.name} and the price is {self.price}"