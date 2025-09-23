from Product import product
from Laptop import laptop
from Smartphone import smartphone

class inventory: 
    def __init__(self):
        self._product= []

    def add_product(self, product_nr, name, price, tel_lapt, ram, **kwargs):
        product_nr=int(product_nr)
        price=int(price)
        ram=int(ram)

        
        if tel_lapt.lower() == "laptop":
            screen_size = kwargs.get('screen_size')
            processor = kwargs.get('processor')
            ny_laptop = laptop (product_nr, name, price, ram, processor, screen_size)
            self._product.append(ny_laptop)

        elif tel_lapt.lower() == "smartphone":
            storage= kwargs.get('storage')
            os= kwargs.get('os')
            ny_phone = smartphone(product_nr, name, price, ram, storage, os)
            self._product.append(ny_phone)


    def show_all(self):
        if not self._product:
            print("finns inga produkter än")
        else: 
            for prod in self._product:
                if isinstance(prod, laptop):
                    print(f"- {prod}")
                elif isinstance(prod, smartphone):
                    print(f"- {prod}")

    def delete(self, product_nr):
        product_nr = int(product_nr)

        for prod  in self._product:
            if prod._product_nr == product_nr :
                self._product.remove(prod)
                print(f"Product with number {product_nr} has been deleted.")
                return # Avsluta funktionen när produkten har hittats och tagits bort
        
        print(f"Product with number {product_nr} not found.")
           

    def uppdate_price(self, prod_nr, new_price):
        found = False
        prod_nr= int(prod_nr)
        for produkter in self._product:
            if produkter._product_nr ==  prod_nr:
                produkter._price = new_price 
                found= True
                print("prisat är uppdaterad")
                break

        if not found:    
             print("produkten hittades inte")

    