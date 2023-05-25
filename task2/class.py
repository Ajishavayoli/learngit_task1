class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def calculate_area(self):
        return self.length * self.width

    def calculate_perimeter(self):
        return 2 * (self.length + self.width)


# Creating an instance of the Rectangle class
my_rectangle = Rectangle(5, 3)

# Accessing attributes and methods of the object
area = my_rectangle.calculate_area()
perimeter = my_rectangle.calculate_perimeter()

print(f"Rectangle area: {area}")
print(f"Rectangle perimeter: {perimeter}")
