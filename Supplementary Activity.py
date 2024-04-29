import math

class RegularPolygon:
    def __init__(self, side):
        self.side = side

class Square(RegularPolygon):
    def area(self):
        return self.side * self.side

class EquilateralTriangle(RegularPolygon):
    def area(self):
        return (self.side ** 2) * 0.433

class Star(RegularPolygon):
    def area(self):
        return math.sqrt(3) * self.side ** 2

class Hexagon(RegularPolygon):
    def area(self):
        return (3 * math.sqrt(3) * self.side ** 2) / 2

class Heptagon(RegularPolygon):
    def area(self):
        return (7 * self.side ** 2) / (4 * math.tan(math.pi / 7))

obj1 = Square(4)
obj2 = EquilateralTriangle(3)
obj3 = Star(5)
obj4 = Hexagon(6)
obj5 = Heptagon(7)

print("Area of Square:", obj1.area())
print("Area of Equilateral Triangle:", obj2.area())
print("Area of Star:", obj3.area())
print("Area of Hexagon:", obj4.area())
print("Area of Heptagon:", obj5.area())
