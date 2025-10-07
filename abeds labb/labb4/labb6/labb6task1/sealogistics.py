from logisticsfactory import LogisticsFactory
from ship import Ship

class SeaLogistics(LogisticsFactory):
    def create_transport(self):
        return Ship()