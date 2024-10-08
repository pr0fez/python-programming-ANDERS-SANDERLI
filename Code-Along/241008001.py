import matplotlib.pyplot as plt


class Vector:           # vector är som matematiska listor
    """A class to represent Euclidean vectors"""

    def __init__(self, *numbers):         # *numbers är som en dict med alla följande parametrar i
        # error checking
        for number in numbers:
            if not isinstance(number, (float, int)):
                raise TypeError(f"{number} is not a valid number")
        if len(numbers) <= 0:
            raise ValueError("Vectors can't be empty")
        
        self._numbers = tuple(float(number) for number in numbers)

    @property
    def numbers(self):
        return self._numbers
    
    @staticmethod
    def validate2d(instance):
        if not len(instance) == 2:
            raise ValueError("The vector is not 2D")
        return True
    
    def __add__(self, other):
        if self.validate_vector(other):
            numbers = (a + b for a, b in zip(self.numbers, other.numbers))
            return Vector(*numbers)
        
    def __sub__(self, other):
        if self.validate_vector(other):
            numbers = (a - b for a, b in zip(self.numbers, other.numbers))
            return Vector(*numbers)
    
    def __mul__(self, value):                       # här kan vi bara multiplicera t ex u * 3
        if not isinstance(value, (int, float)):
            raise TypeError("Value must be a scalar (int or float).")
        numbers = (a * value for a in self.numbers)
        return Vector(*numbers)
    
    def __rmul__(self, value):                      # detta gör vi för att kunna multiplicera t ex 3 * u
        return self * value

    def __len__(self):
        return len(self.numbers)

    def validate_vector(self, other):
        if not isinstance(other, Vector) or len(self.numbers) != len(other.numbers):
            raise ValueError(f"{other} is not a Vector")
        return True
    
    def __abs__(self):
        """Returns the Euclidean norm of the vector, aka the L2-norm"""   # kallas även manhattan distance ??? enligt Raphael
        return sum(a ** 2 for a in self.numbers) ** 0.5                   # ** 0.5 är samma sak som att ta kvadratroten ur

    def __repr__(self):
        return f"Vector{self.numbers}"
    
    def __getitem__(self, index):
        return self.numbers[index]
    
    @staticmethod
    def plot(*vectors):
        X, Y = [], []
        for v in vectors:
            if Vector.validate2d(v):
                X.append(v[0])
                Y.append(v[1])
        
        originX = originY = tuple(0 for _ in range(len(X)))
        plt.quiver(originX, originY, X, Y, angles = "xy", scale_units = "xy", scale = 1)
        plt.xlim(-2, 10)
        plt.ylim(-2, 10)
        plt.grid()
        plt.show()