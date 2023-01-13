
# base class made in collab with Christoffer

import math


class Vec2:
    x, y = 0, 0

    def __init__(self, x, y):
        self.x = x
        self.y = y

    # Returns the length of the vector 2
    def length(self):
        return math.sqrt(self.x**2 + self.y**2)

    # Returns the angle in degrees between 2 vectors
    def degrees_between(self, other):
        return math.degrees(math.acos((self.x * other.x + self.y * other.y) / (self.length() * other.length())))

    # Returns the cross vector of the current vec2
    def get_cross_vector(self):
        return Vec2(-self.y, self.x)

    # define vector2's + operator's function
    def __add__(self, other):
        return Vec2(self.x + other.x, self.y + other.y)

    # define vector2's - operator's function
    def __sub__(self, other):
        return Vec2(self.x - other.x, self.y - other.y)

    # define vector2's * operator's function
    def __mul__(self, other):
        return self.x * other.x + self.y * other.y

    # define vector2's == operator's function
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    # define vector2's != operator's function
    def __ne__(self, other):
        return self.x != other.m_x and self.y != other.y

    # define what to return when converting vector2 to string
    def __str__(self):
        return f'[x: {self.x}, y: {self.y}]'


if __name__ == "__main__":
    # Use cases
    firstVec = Vec2(-3, 5)
    secondVec = Vec2(4, 6)

    print(f"\nDegrees between firstVec and secondVed: {firstVec.degrees_between(secondVec)}\n")

    thirdVec = firstVec + secondVec

    print(f"Third vectors length: {thirdVec.length()}\n")

    scalarProduct = firstVec * secondVec
    print(f"The scalar product is: {scalarProduct}\n")






