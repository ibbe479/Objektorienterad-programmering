from Product import product
class inventory: 
    def __init__(self):
        self.product= []

    def add_product(self, product_nr, name, price):
        Product = product(product_nr, name, price )
        self.product.append(Product)

    def delete(self, product_nr):
        for i in range(len(self.product)):
            if self.product[i].see_product_nr().lower() == product_nr.lower():
                del self.product[i]
                print ("produckt bortagen")
                return
            print("produkt hittades inte")

    def uppdate_price(self, name, new_price):
        found = False
        for produkter in self.product:
            if produkter.see_name().lower() ==  name.lower():
                produkter.price = new_price 
                found= True
                print("prisat är uppdaterad")
                break

        if not found:    
             print("produkten hittades inte")

    def show_all(self):
        if not self.product:
            print("finns inga produkter än")
        else: 
            for prod in self.product:
                print(f" {prod.see_product_nr()} {prod.see_name()} {prod.see_price()} ")