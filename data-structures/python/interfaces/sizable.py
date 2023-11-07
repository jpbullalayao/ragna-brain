from abc import ABC, abstractmethod

class Sizeable(ABC):
    @abstractmethod
    def size(self):
        pass

