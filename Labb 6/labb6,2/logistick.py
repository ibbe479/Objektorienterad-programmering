from abc import ABC, abstractmethod

class Logistick(ABC):
   
    @abstractmethod        
    def create_transport(self):
        """detta är en abstrackt metod som skaåar en transport"""
        pass

    def plan_delevery(self):
        transport=self.create_transport()
        print(transport.deliver())
        