from abc import ABC, abstractmethod

class Logistick:
    def __init__(self, size, weight, destination, transport_type):
        self.size = size
        self.wheight = weight
        self.destination = destination
        self.transport_type = transport_type

    @abstractmethod        
    def create_transport(self):
        """detta är en abstrackt metod som skaåar en transport"""
        pass

    def plan_delevery(self):
        transport=self.create_transport()
        print(transport.deliver())
        