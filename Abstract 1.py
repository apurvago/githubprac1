# When we want to provide common interface for different implementations of a component, we use an abstract class.
# So, it has declaration but does not have an implementation
from abc import ABC, abstractmethod
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
    def perimeter(self):
        pass

class Circle(Shape):
    def __init__(self,radius):              # self: allows to access the variables, attributes, methods of a class
        self.radius=radius
    def area(self):
        return 3.14*self.radius**2
    def perimeter(self):
        return 2*3.14*self.radius

class Square(Shape):
    def __init__(self,side):
        self.side=side
    def area(self):
      return self.side**2
    def perimeter(self):
      return self.side*4

# create objects of class - objectname= Classname()
circle = Circle(int(input("Enter radius of circle: ")))    #(value of radius)   (3)
square = Square(int(input("Enter side of square: ")))    #(value of side)    (6)

# f - formatted literal strings - to evaluate/format the expression within f-string i.e {}
print(f"Area of a circle is {circle.area()}")
print(f"Perimeter of a circle is {circle.perimeter()}")
print(f"Area of a square is {square.area()}")
print(f"Perimeter of a square is {square.perimeter()}")
