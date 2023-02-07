# Vector2D class for operating with vector objects
import math

class Vector2D():
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
        self.thresh = 0.000001
        
    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Vector2D(x,y)

    def __sub__(self, other):
        x = self.x - other.x
        y = self.y - other.y
        return Vector2D(x,y)

    def __neg__(self):
        x = -self.x
        y = -self.y
        return Vector2D(x,y)

    def __mul__(self, scalar):
        return Vector2D(self.x * scalar, self.y * scalar)

    def __div__(self, scalar):
        if scalar != 0:
            return Vector2D(self.x / scalar, self.y / scalar)
        else:
            return None
        
    def __truediv__(self, scalar):
        return self.__div__(scalar)

    def __eq__(self, other):
        if abs(self.x - other.x) < self.thresh:
            if abs(self.y - other.y) < self.thresh:
                return True
        return False

    def __ge__(self, other):
        return self.x >= other.x, self.y >= other.y

    def __lt__(self, other):
        return self.x <= other.x, self.y <= other.y

    def __hash__(self):
        return id(self)

    def __str__(self):
        return "<" + str(self.x) + ", " + str(self.y) + ">"

    def magnitudeSquared(self):
        return (self.x**2 + self.y**2)

    def magnitude(self):
        return (self.x**2 + self.y**2)**(1/2)

    def normalize(self):
        mag = self.magnitude()
        if mag != 0:
            return (1 / mag)
        return None
    
    def dot(self, other):
        self = self.dot
        other = other.dot
        return (self, other)

    def copy(self):
        return Vector2D(self.x, self.y)
            
if __name__ == '__main__':
    v1 = Vector2D(2, 3)
    v2 = Vector2D(0.5, -1.5)
    print(f'The sum of {v1} and {v2} is {v1+v2}')
    print(f'The dot product of {v1} and {v2} is {v1.dot(v2)}')
