from logistick import Logistick
from truck import Truck

class Roadlogistics(Logistick):
    
    def create_transport(self):
        return Truck()
    
