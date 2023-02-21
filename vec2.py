import math
import sys

class Vec2:
    x: float = 0
    y: float = 0
    length: float = 0

    def __init__(self, x, y):
        try:
            float(x)
            float(y)
        except:
            sys.exit("Not valid number")
        
        if x == 0 and y == 0:
            sys.exit("Both vector components can't be zero")
        
        self.x = x
        self.y = y

        self.length = math.sqrt(self.x**2 + self.y**2)

    # Returns the length of the vector 2
    # def length(self):
    #     return math.sqrt(self.x**2 + self.y**2)

    # Returns the angle in degrees between 2 vectors
    def degrees_between(self, other):
        return math.degrees(math.acos((self.x * other.x + self.y * other.y) / (self.length * other.length)))

    # Returns the cross vector of the current vec2
    def get_cross_vector(self):
        return Vec2(-self.y, self.x)
    
    # Returns the cross vector of the current vec2
    def normalize(self):
        return Vec2(self.x / self.length, self.y / self.length)

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
