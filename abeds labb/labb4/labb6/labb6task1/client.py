from roadlogistics import RoadLogistics
from sealogistics import SeaLogistics
from airlogistics import AirLogistics

class Client:
  
    def display_menu(self):
        print("\nFactory")
        print("1. Road Delivery (Truck)")
        print("2. Sea Delivery (Ship)")
        print("3. Air Delivery (Airplane)")
        print("0. Exit")

    
    def run_menu(self):
        while True:
            self.display_menu()
            choice = input("Choose an option: ")
            
            if choice == "1":
                self.road_delivery()
            elif choice == "2":
                self.sea_delivery()
            elif choice == "3":
                self.freight_delivery()
            elif choice == "0":
                break
            else:
                print("Invalid choice!")
    
    def road_delivery(self):
        print("Road delivery will now be planned.")
        road_factory = RoadLogistics()
        road_factory.plan_delivery()
        print("Road delivery completed!")
    
    def sea_delivery(self): 
        print("Sea delivery will now be planned.")
        sea_factory = SeaLogistics()
        sea_factory.plan_delivery()
        print("Sea delivery completed!")

    def freight_delivery(self):
        print("Freight delivery will now be planned.")
        air_factory = AirLogistics()
        air_factory.plan_delivery()
        print("Freight delivery completed!")
    

if __name__ == "__main__":
    client = Client()
    client.run_menu()
