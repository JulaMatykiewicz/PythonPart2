from abc import ABC, abstractmethod
import math

class Shape(ABC):
    def __init__(self):
        pass
    
    @abstractmethod
    def calculate_area(self):
        pass
    
    @abstractmethod
    def calculate_perimeter(self):
        pass

class Rectangle(Shape):
    def __init__(self, length, width):
        super().__init__()
        self._length = length
        self._width = width
    
    def calculate_area(self):
        return self._length * self._width
    
    def calculate_perimeter(self):
        return 2 * (self._length + self._width)

class Circle(Shape):
    def __init__(self, radius):
        super().__init__()
        self._radius = radius
    
    def calculate_area(self):
        return math.pi * self._radius**2
    
    def calculate_perimeter(self):
        return 2 * math.pi * self._radius

rectangle = Rectangle(4, 6)
circle = Circle(5)

print("Prostokąt:")
print("Pole:", rectangle.calculate_area())
print("Obwód:", rectangle.calculate_perimeter())

print("Koło:")
print("Pole:", circle.calculate_area())
print("Obwód:", circle.calculate_perimeter())

