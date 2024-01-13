import math
print('Compute the area and perimeter of a circle using classes and objects \nSubmitted by: Clyde Joshua C.Belongilot')
print('--------------------------------------------------------------------')
class Circle:
    def __init__(self, radius):
        self.radius = radius

    def calc_area(self):
        circle_area = math.pi * self.radius**2
        print("Area of the circle: {:.2f}".format(circle_area))

    def calc_perimeter(self):
        circle_perimeter = 2 * math.pi * self.radius
        print("Perimeter of the circle: {:.2f}".format(circle_perimeter))



radius = float(input("Enter the radius: "))
lingin = Circle(radius)

lingin.calc_area()
lingin.calc_perimeter()
