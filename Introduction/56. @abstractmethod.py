from abc import ABC , abstractmethod
from math import pi

class Shape(ABC):
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def area(self):
        pass

    def perimeter(self):
        pass