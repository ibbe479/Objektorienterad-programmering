from roadlogistics import Roadlogistics
from sealogistics import Sealogistics
from airlogistics import Airlogistics

class Client :

    def menu():
        print("1. Road delevery (truck)")
        print("2. sea delevery (ship)")
        print("3. air delevery (airplane)")
        print("0. avsluta programmet")
        choice = input("välj ett alternativ (1-3): ")
        return choice
    
    def main():
        while True:
            choice = Client.menu()

            if choice == '1':
            
                road_logistics = Roadlogistics()
                road_logistics.plan_delevery()
            elif choice == '2':
            
                sea_logistics = Sealogistics()
                sea_logistics.plan_delevery()
            elif choice == '3':
                
                air_logistics = Airlogistics()
                air_logistics.plan_delevery()

            elif choice =="0":
                print("avslutar programmet...")
                break

            else:
                print("ogiltigt val, försök igen.")
                Client.main()

if __name__ == "__main__":
    Client.main()
