import math

class Circle:
    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius
    
    def get_area(self):
        return math.pi * self.radius**2
    
    def get_perimeter(self):
        return 2 * math.pi * self.radius
    
    def get_circumference(self):
        return self.get_perimeter()

# Example usage:
# Creating an instance of Circle
circle1 = Circle(0, 0, 5)  # Circle centered at (0, 0) with radius 5

# Calculating and printing area, perimeter, and circumference
print(f"Area of the circle: {circle1.get_area():.2f} square units")
print(f"Perimeter of the circle: {circle1.get_perimeter():.2f} units")
print(f"Circumference of the circle: {circle1.get_circumference():.2f} units")
