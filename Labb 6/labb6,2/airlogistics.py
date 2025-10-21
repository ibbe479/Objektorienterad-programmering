from logistick import Logistick
from airplane import Airplane

class Airlogistics(Logistick):

    def create_transport(self):
        return Airplane()
