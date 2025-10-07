from abc import ABC, abstractmethod

class LogisticsFactory(ABC):
    @abstractmethod
    def create_transport(self):
        pass

    def plan_delivery(self):
        transport = self.create_transport()
        transport.deliver()