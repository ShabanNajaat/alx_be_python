import math

class Shape:
    def area(self):
        """
        Raises a NotImplementedError, indicating that derived classes need to override this method.

        Raises:
            NotImplementedError: This method must be overridden in derived classes.
        """
        raise NotImplementedError("Subclass must implement abstract method")

class Rectangle(Shape):
    def __init__(self, length: float, width: float):
        """
        Initializes a Rectangle instance with length and width.

        Args:
            length (float): The length of the rectangle.
            width (float): The width of the rectangle.
        """
        self.length = length
        self.width = width

    def area(self):
"""
        Calculates the area of the rectangle.

        Returns:
            float: The area of the rectangle (length × width).
        """
        return self.length * self.width

class Circle(Shape):
    def __init__(self, radius: float):
        """
        Initializes a Circle instance with radius.

        Args:
            radius (float): The radius of the circle.
        """
        self.radius = radius

    def area(self):
        """
        Calculates the area of the circle.

        Returns:
            float: The area of the circle (π × radius²).
        """
        return math.pi * (self.radius ** 2)

