class Circle:
    def __init__(self, radius):
        self.radius = radius

    def get_area(self):
        return 3.14 * self.radius ** 2

    def __sub__(self, other):
        radius_difference = abs(self.radius - other.radius)
        if radius_difference == 0:
            return Point(0, 0)
        return radius_difference


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


circle1 = Circle(10)
circle2 = Circle(15)
print(circle1 - circle2)
