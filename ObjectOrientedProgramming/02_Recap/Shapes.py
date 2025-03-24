"""
Three different shape classes that each calculate the shapes area and circumference
"""
import math


class Rectangle:
    """
    Class Rectangle.
    """

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def rectangle_area(self):
        """
        Calculate the area of the rectangle.
        :return: rectangle area
        """
        return self.width * self.height

    def rectangle_circumference(self):
        """
        Calculate the circumference of the rectangle.
        :return: rectangle circumference
        """
        return (self.width + self.height) * 2

    def __str__(self):
        return f'Rectangle (width={self.width}, height={self.height})'


class Circle:
    """Class Circle."""

    def __init__(self, radius):
        self.radius = radius

    def circle_area(self):
        """Calculate the area of the circle."""
        return math.pi * pow(self.radius, 2)

    def circle_circumference(self):
        """Calculate the circumference of the circle."""
        return 2 * math.pi * self.radius

    def __str__(self):
        return f'Circle with radius {self.radius}'


class Square:
    """Class Triangle."""

    def __init__(self, side):
        self.a = side

    def square_area(self):
        """Calculate the area of the square."""
        return self.a * self.a

    def square_circumference(self):
        """Calculate the circumference of the square."""
        return 4 * self.a

    def __str__(self):
        return f'Square with side {self.a}'


if __name__ == '__main__':
    square = Square(5)
    print(f'{square} area is {square.square_area()}')
    print(f'{square} circumference is {square.square_circumference()}')
    circle = Circle(3)
    print(f'{circle} area is {circle.circle_area()}')
    print(f'{circle} circumference is {circle.circle_circumference()}')
    rectangle = Rectangle(4, 5)
    print(f'{rectangle} area is {rectangle.rectangle_area()}')
    print(f'{rectangle} circumference is {rectangle.rectangle_circumference()}')