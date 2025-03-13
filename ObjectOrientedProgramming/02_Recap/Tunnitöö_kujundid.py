""" Three different shape a classes that each calculate
the shapes area and perimeter"""
import math


class Shape:
    # Minu versioon oli selline:
    # def __init__(self, a, b, c):
    #     self.a = 0
    #     self.b = 0
    #     self.c = 0

    # Õpetaja versioon on selline:
    def __init__(self, dimension):
        self.dimension = dimension
    # arvuta pindala
    def calculate_area(self):
        return self.dimension * 15.5

    def calculate_perimeter(self):
        return 2 * self.dimension

class Square:

    def __init__(self, length):
        """Initialize square instance"""
        self.length = length

    def __str__(self):
        length = self.length
        return f"Square({self.length=})"

    def calculate_area_square(self):
        """Calculate the area of the square"""
        return self.length ** 2

    def calculate_perimeter_square(self):
        return 2 * self.length ** 2

class Rectangle:

    def __init__(self, width, height):
        """Initialize rectangle instance"""
        self.width = width
        self.height = height

    def __str__(self):
        width = self.width
        height = self.height
        return f"Rectangle({self.width and self.height=})"

    def calculate_area_rectangle(self):
        """Calculate the area of the square"""
        return self.width * self.height

    def calculate_perimeter_rectangle(self):
        return 2 * (self.width + self.height)

class Triangle:

    def __init__(self, a, b, c, height):
        """Initialize triangle instance"""
        self.a = a
        self.b = b
        self.c = c
        self.height = height

    def __str__(self):
        a = self.a
        b = self.b
        c = self.c
        return f"Rectangle({self.a and self.b and self.c and self.height=})"

    def calculate_area_triangle(self):
        """Calculate the area of the triangle"""
        return self.a * self.height / 2

    def calculate_perimeter_triangle(self):
        """Calculate the perimeter of the triangle"""
        return self.a + self.b + self.c

class Circle:
    """Circle class"""
    def __init__(self, radius):
        """Initialize circle instance"""
        self.radius = radius

    def __repr__(self):
        """Reproduce this circle"""
        radius = self.radius
        return f"Circle({self.radius=})"

    def calculate_area_circle(self):
        """Calculate the area of the circle"""
        return self.radius ** 2 * math.pi

    def calculate_perimeter_circle(self):
        """Calculate the perimeter of the circle"""
        return self.radius * 2 * math.pi


if __name__ == '__main__':
    square = Square(4)
    print(f"{square} area is {square.calculate_area_square()}")
    print(f"{square} perimeter is {square.calculate_perimeter_square()}")

    rectangle = Rectangle(4, 5)
    print(f"{rectangle} area is {rectangle.calculate_area_rectangle()}")
    print(f"{rectangle} perimeter is {rectangle.calculate_perimeter_rectangle()}")

    triangle = Triangle(4, 5, 6, 7)
    print(f"{triangle} area is {triangle.calculate_area_triangle()}")
    print(f"{triangle} perimeter is {triangle.calculate_perimeter_triangle()}")

    circle = Circle(radius=3)
    print(f"{circle} area is {circle.calculate_area_circle()}")