# lets add some more expressions for operator overlaoding
'''
Explanation:
Initialization (__init__): Sets the x and y components of the vector.
Addition (__add__): Defines how to add two Vector instances.
Subtraction (__sub__): Defines how to subtract one Vector from another.
Multiplication (__mul__): Multiplies the vector by a scalar.
True Division (__truediv__): Divides the vector by a scalar.
Floor Division (__floordiv__): Divides the vector by a scalar using floor division.
Modulus (__mod__): Finds the modulus of each component with a scalar.
Exponentiation (__pow__): Raises each component to the power of an exponent.
Bitwise AND (__and__): Applies bitwise AND to each component.
Bitwise OR (__or__): Applies bitwise OR to each component.
Bitwise XOR (__xor__): Applies bitwise XOR to each component.
Left Shift (__lshift__): Shifts the bits of each component to the left.
Right Shift (__rshift__): Shifts the bits of each component to the right.
Equality (__eq__): Compares two vectors for equality.
Inequality (__ne__): Compares two vectors for inequality.
Less Than (__lt__): Compares the magnitudes of two vectors.
Magnitude (magnitude): Calculates the magnitude (length) of the vector.
Representation (__repr__): Returns a string representation of the vector.
'''
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)

    def __truediv__(self, scalar):
        return Vector(self.x / scalar, self.y / scalar)

    def __floordiv__(self, scalar):
        return Vector(self.x // scalar, self.y // scalar)

    def __mod__(self, scalar):
        return Vector(self.x % scalar, self.y % scalar)

    def __pow__(self, exponent):
        return Vector(self.x ** exponent, self.y ** exponent)

    def __and__(self, other):
        return Vector(self.x & other.x, self.y & other.y)

    def __or__(self, other):
        return Vector(self.x | other.x, self.y | other.y)

    def __xor__(self, other):
        return Vector(self.x ^ other.x, self.y ^ other.y)

    def __lshift__(self, shifts):
        return Vector(self.x << shifts, self.y << shifts)

    def __rshift__(self, shifts):
        return Vector(self.x >> shifts, self.y >> shifts)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __ne__(self, other):
        return not self.__eq__(other)

    def __lt__(self, other):
        return self.magnitude() < other.magnitude()

    def magnitude(self):
        return (self.x**2 + self.y**2) ** 0.5

    def __repr__(self):
        return f"Vector({self.x}, {self.y})"

# Example usage:
v1 = Vector(2, 3)
v2 = Vector(1, 5)

print("v1 + v2 =", v1 + v2)  # Vector(3, 8)
print("v1 - v2 =", v1 - v2)  # Vector(1, -2)
print("v1 * 3 =", v1 * 3)    # Vector(6, 9)
print("v1 / 2 =", v1 / 2)    # Vector(1.0, 1.5)
print("v1 == v2?", v1 == v2) # False
print("v1 < v2?", v1 < v2)   # True based on magnitude

''' o/p 
v1 + v2 = Vector(3, 8)
v1 - v2 = Vector(1, -2)
v1 * 3 = Vector(6, 9)
v1 / 2 = Vector(1.0, 1.5)
v1 == v2? False
v1 < v2? True
'''
