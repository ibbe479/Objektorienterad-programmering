from logistick import Logistick

class sealogistics(Logistick):
    def __init__(self, size, weight, destination, dock):
        super().__init__(size, weight, destination)
        self.dock = dock

    def create_transport():
        pass
