from abc import ABC, abstractmethod

class Sizable(ABC):
    @abstractmethod
    def size(self):
        pass

