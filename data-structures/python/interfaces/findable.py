from abc import ABC, abstractmethod

class Findable(ABC):
    @abstractmethod
    def find(self, val):
        pass

