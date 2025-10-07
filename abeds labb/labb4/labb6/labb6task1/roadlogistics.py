from logisticsfactory import LogisticsFactory
from truck import Truck

class RoadLogistics(LogisticsFactory):
    def create_transport(self):
        return Truck()