import math


class Square:
    def __init__(self, side) -> None:
        self.side = side

    def area(self):
        area = self.side * self.side
        return round(area, 2)

    def diagonal(self):
        diagonal = math.sqrt(2) * self.side
        return round(diagonal, 2)


square1 = Square(side=1.5)
print(square1.area())  # 2.25
print(square1.diagonal())  # 2.12

square2 = Square(side=15)
print(square2.area())  # 225
print(square2.diagonal())  # 21.21
