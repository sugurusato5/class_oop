class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        pi = self.radius * self.radius * 3.14  # 半径
        return round(pi, 2)

    def perimeter(self):
        circle = self.radius * 2 * 3.14
        return round(circle, 2)


# 半径1の円
circle1 = Circle(radius=1)  # インスタンス化
print(circle1.area())  # 3.14
print(circle1.perimeter())  # 6.28

# 半径3の円
circle3 = Circle(radius=3)
print(circle3.area())  # 28.27
print(circle3.perimeter())  # 18.85
