import math

class Shape:
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def describe(self):
        return "This {} is {}.".format(self.name, self.color)


class Circle(Shape):
    def __init__(self, name, color, radius):
        super().__init__(name, color)
        self.radius = radius

    def area(self):
        return math.pi * self.radius**2


class Rectangle(Shape):
    def __init__(self, name, color, length, width):
        super().__init__(name, color)
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width


class Triangle(Shape):
    def __init__(self, name, color, base, height):
        super().__init__(name, color)
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height



circle = Circle("circle", "red", 5)
rectangle = Rectangle("rectangle", "blue", 4, 6)
triangle = Triangle("triangle", "green", 3, 4)


print("Area of the", circle.name, ":", circle.area())
print("Area of the", rectangle.name, ":", rectangle.area())
print("Area of the", triangle.name, ":", triangle.area())