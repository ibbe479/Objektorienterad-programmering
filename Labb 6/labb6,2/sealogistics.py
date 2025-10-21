from logistick import Logistick
from ship import Ship

class Sealogistics(Logistick):
   
    def create_transport(self):
        return Ship()


    