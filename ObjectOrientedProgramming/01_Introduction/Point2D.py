"""Point2D"""
class Point2D:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x:.2f}, {self.y:.2f})"

    def __repr__(self):
        return f"Point2D({self.x}, {self.y})"

p1 = Point2D(1, 2)
p2 = eval(repr(p1))

print(p1) # (1.00, 2.00)
print(p2)
print(p2 == p1)