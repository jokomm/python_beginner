"""Shapes."""

from math import pi


class Shape:
    """General shape class."""

    def __init__(self, color: str):
        """Constructor, sets the color."""
        self.color = color

    def set_color(self, color: str):
        """Set the color of the shape."""
        self.color = color

    def get_color(self) -> str:
        """Get the color of the shape."""
        return self.color

    def get_area(self) -> float:
        """Get area method which every subclass has to override."""
        print("Implement area")


class Circle(Shape):
    """Circle is a subclass of Shape."""

    def __init__(self, color: str, radius: float):
        """
        Constructor of the circle.

        The color is stored using superclass constructor:
        super().__init__(color)

        The radius value is stored here.
        """
        super().__init__(color)
        self.radius = radius

    def __repr__(self) -> str:
        """
        Return representation of the circle.

        For this exercise, this should return a string:
        Circle (r: {radius}, color: {color})
        """
        return f"Circle (r: {self.radius}, color: {self.color})"

    def get_area(self) -> float:
        """
        Calculate the area of the circle.

        Area of the circle is pi * r * r.
        """
        return pi * self.radius * self.radius


class Square(Shape):
    """Square is a subclass of Shape."""

    def __init__(self, color: str, side: float):
        """
        Constructor of the square.

        The color is stored using superclass constructor:
        super().__init__(color)

        The side value is stored here.
        """
        super().__init__(color)
        self.side = side

    def __repr__(self) -> str:
        """
        Return representation of the square.

        For this exercise, this should return a string:
        Square (a: {side}, color: {color})
        """
        return f"Square (a: {self.side}, color: {self.color})"

    def get_area(self) -> float:
        """
        Calculate the area of the square.

        Area of the square is side * side.
        """
        return self.side * self.side


class Rectangle(Shape):
    """Rectangle is a subclass of Shape."""

    def __init__(self, color: str, side_a: float, side_b: float):
        """
        Constructor of the square.

        The color is stored using superclass constructor:
        super().__init__(color)

        The side value is stored here.
        """
        super().__init__(color)
        self.side_b = side_b
        self.side_a = side_a

    def __repr__(self) -> str:
        """
        Return representation of the square.

        For this exercise, this should return a string:
        Rectangle (a: {side_a}, b: {side_b}, color: {color})
        """
        return f"Rectangle (l: {self.side_a}, w: {self.side_b}, color: {self.color})"

    def get_area(self) -> float:
        """
        Calculate the area of the square.

        Area of the square is side a * side b.
        """
        return self.side_a * self.side_b


class Paint:
    """The main program to manipulate the shapes."""

    def __init__(self):
        """Constructor should create a list to store all the shapes."""
        self.shapes = []

    def add_shape(self, shape: Shape) -> None:
        """Add a shape to the program."""
        self.shapes.append(shape)

    def get_shapes(self) -> list:
        """Return all the shapes."""
        return self.shapes

    def calculate_total_area(self) -> float:
        """Calculate total area of the shapes."""
        total = 0
        for shape in self.shapes:
            total += shape.get_area()
        return total

    def get_circles(self) -> list:
        """Return only circles."""
        circles = [shape for shape in self.shapes if type(shape) == Circle]
        return circles

    def get_squares(self) -> list:
        """Return only squares."""
        squares = [shape for shape in self.shapes if type(shape) == Square]
        return squares

    def get_rectangles(self) -> list:
        """Return only rectangles."""
        rectangles = [shape for shape in self.shapes if type(shape) == Rectangle]
        return rectangles


if __name__ == '__main__':
    paint = Paint()
    circle = Circle("blue", 10)
    square = Square("red", 11)
    rectangle = Rectangle("grey", 10, 20)
    paint.add_shape(circle)
    paint.add_shape(square)
    paint.add_shape(rectangle)
    print(paint.calculate_total_area())
    print(paint.get_circles())
