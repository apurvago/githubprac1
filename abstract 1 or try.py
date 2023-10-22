from abc import ABC, abstractmethod
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
    def perimeter(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return 3.14 * self.radius ** 2
    def perimeter(self):
        return 2 * 3.14 * self.radius

class Square(Shape):
    def __init__(self, side):
        self.side = side
    def area(self):
        return self.side ** 2
    def perimeter(self):
        return self.side * 4

# Initializing the loop
for i in range(0, 100):
    rad = int(input("Enter radius of circle: "))
    s = int(input("Enter side of square: "))
    circle = Circle(rad)
    square = Square(s)
    print("When radius is", rad)
    print("--------------------")
    print(f"Area of a circle is {circle.area()}")
    print(f"Perimeter of a circle is {circle.perimeter()}")
    print("--------------------")
    print("When side is", s)
    print("--------------------")
    print(f"Area of a square is {square.area()}")
    print(f"Perimeter of a square is {square.perimeter()}")
    print("--------------------")
