# abs(): A built-in Python function that returns the absolute value of a number. This means it strips away the sign and returns the positive magnitude of self.j. means no matter it is positive or negative, it will return only the value without any signs

class Vector:
    def __init__(self, i, j, k):
        self.i = i
        self.j = j
        self.k = k

    def __str__(self):        # basic scenario
        return f"{self.i}i + {self.j}j + {self.k}k"

    def __add__(self, other): # it will perform operator overloading for +  (addition)
        return Vector(self.i + other.i, self.j + other.j, self.k + other.k)

    def __sub__(self, other): # it will perform operator overloading for -  (substraction)
        result = Vector(self.i - other.i, self.j - other.j, self.k - other.k)
        return result.format_subtraction()     # include the formatting

    def format_subtraction(self):
        formatted = []
        formatted.append(f"{self.i}i")
        formatted.append(f"{'-' if self.j < 0 else '+'} {abs(self.j)}j")
        # in this conditional expression, add - if the value is negative otherwise +
        # abs(): A built-in Python function that returns the absolute value of a number. This means it strips away the sign and returns the positive magnitude of self.j. Means no matter it is positive or negative, it will return only the value without any signs

        formatted.append(f"{'-' if self.k < 0 else '+'} {abs(self.k)}k")
        return ' '.join(formatted)

# Example usage:
v = Vector(3, 7, 2)
print(v)

w = Vector(1, 8, 6)
print(w)

print("Adding these two vectors we get:")
print(v + w)  # This will include the + signs

print("Subtracting these two vectors we get:")
print(v - w)  # This will omit the + signs where not needed
