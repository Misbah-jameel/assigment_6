from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass  # Sirf signature, implementation nahi

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

# Object bana rahe hain
rect = Rectangle(5, 10)
print("Area of rectangle:", rect.area())
