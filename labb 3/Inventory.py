from Product import product
class inventory: 
    def __init__(self):
        self.product= []

    def add_product(self, product_nr, name, price):
        product_nr=int(product_nr)
        price=int(price)
        Product = product(product_nr, name, price )
        self.product.append(Product)


    def show_all(self):
        if not self.product:
            print("finns inga produkter än")
        else: 
            for prod in self.product:
                print(f" produkt nummret är: {prod.see_product_nr()}, produkten heter: {prod.see_name()} och den kostar {prod.see_price()}kr ")

    def delete(self, product_nr):
        product_nr = int(product_nr)

        for prod  in self.product:
            if prod.see_product_nr() == product_nr :
                self.product.remove(prod)
                print(f"Product with number {product_nr} has been deleted.")
                return # Avsluta funktionen när produkten har hittats och tagits bort
        
        print(f"Product with number {product_nr} not found.")
           

    def uppdate_price(self, prod_nr, new_price):
        found = False
        prod_nr= int(prod_nr)
        for produkter in self.product:
            if produkter.see_product_nr() ==  prod_nr:
                produkter.price = new_price 
                found= True
                print("prisat är uppdaterad")
                break

        if not found:    
             print("produkten hittades inte")

    