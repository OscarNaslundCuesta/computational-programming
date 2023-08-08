from numpy import *
from matplotlib.pyplot import *
import math

"""
Define a class ComplexNumber and write an appropriate __init__ method.
"""


class ComplexNumber:
    def __init__(self, real=0.0, imag=0.0):
        self.real = real
        self.imag = imag

    """
    TASK2
    Write a method which returns the complex number’s real part, and one which
    returns the imaginary part.
    """

    def real(self):
        return self.real

    def imag(self):
        return self.imag

    """
    TASK 3
    Write a method is_imaginary and is_real They should return Boolean answers.
    """

    def is_imaginary(self):
        return self.real == 0 and self.imag != 0

    def is_real(self):
        return self.imag == 0

    """
    TASK 4
    Write a representation method which represents a complex number in the mathe-
    matical notation a+ib
    """

    def __str__(self):
        if self.imag >= 0:
            return f"{self.real} + {self.imag}i"
        else:
            return f"{self.real} - {-self.imag}i"

    """
    TASK 5
    Write a method which returns the complex number’s argument and absolute value.
    """

    def get_arg_and_abs(self):
        arg = math.atan2(self.imag, self.real)

        absolute_val = sqrt(self.real ** 2 + self.imag ** 2)

        return arg, absolute_val

    """
    TASK 6
    Write a method which checks if two complex numbers are equal.
    """

    def __eq__(self, other):
        return self.real == other.real and self.imag == other.imag

    """
    TASK 7
    Define methods for operations such as addition, subtraction, multiplication, di-
    vision and power of complex numbers. These methods should work also for op-
    erations between complex numbers, integers and real numbers (floats). Where
    appropriate, make sure that the result is independent of the order of the argu-
    ments.
    """

    def __add__(self, other):
        if isinstance(other, (int, float)):
            real_sum = self.real + other
            imag_sum = self.imag

        elif isinstance(other, ComplexNumber):
            real_sum = self.real + other.real
            imag_sum = self.imag + other.imag

        else:
            raise ValueError("Cannot add ComplexNumber with an unsupported type.")

        return ComplexNumber(real_sum, imag_sum)

    def __radd__(self, other):
        return self + other


first = ComplexNumber(1, 1)
second = 1 + 1j
print(second == first)

c1 = ComplexNumber(3, 4)

c4 = 2.5 + c1
print(c4)
