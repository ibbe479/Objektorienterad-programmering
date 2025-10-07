from abc import ABC, abstractmethod

class Transport(ABC):
    @abstractmethod
    def deliver(self):
        """här ska det skriva ut vart leveranses ska till och mrd vad"""
        pass