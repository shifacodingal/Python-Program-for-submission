

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def calculate_area(self):
        area = self.length * self.width
        return area



length = float(input("Enter the length of the rectangle: "))
width = float(input("Enter the width of the rectangle: "))


rect = Rectangle(length, width)

print("Area of the rectangle is:", rect.calculate_area())