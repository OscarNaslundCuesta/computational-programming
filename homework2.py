"""
NUMA01: Computational Programming with Python
Homework 2
Authors: Oscar Näslund Cuesta, Levi Tuoremaa
Date: 2023-07-06
"""

import numpy as np
from matplotlib.pyplot import *

"""
TASK 1
Construct a class Interval which is initialized with two real numbers 
representing the left and right endpoints respectively.
"""


class Interval:
    def __init__(self, start, end=None):  # end = start if not specified when initialized
        if end is None:
            end = start
        self.interval_array = [start, end]

    """
    TASK 3
    Provide a method on your class so that the code
    i = Interval(1,2)
    print( i )
    prints [1, 2]

    """

    def __repr__(self):
        """
        Returns the interval as a string
        :return:
        """
        return f"{self.interval_array}"

    """
    TASK 2
    Provide methods for the four basic arithmetic operations.
    """

    def __add__(self, other):
        """
        [a, b] + [c, d] = [a + c, b + d]
        :param other:
        :return:
        """
        if isinstance(other, (int, float)):
            # When 'other' is a scalar (single number).
            return Interval(self.interval_array[0] + other, self.interval_array[1] + other)
        elif isinstance(other, Interval):
            # When 'other' is also an Interval object.
            p1 = self.interval_array[0] + other.interval_array[0]
            p2 = self.interval_array[1] + other.interval_array[1]
            return Interval(p1, p2)
        else:
            raise TypeError("You can only add an Interval or a scalar to an Interval.")

    def __radd__(self, other):
        # Addition is commutative, so we can just call our existing __add__ method
        return self.__add__(other)

    def __sub__(self, other):
        """
        [a, b] − [c, d] = [a − d, b − c]
        :param other:
        :return:
        """
        if isinstance(other, (int, float)):
            # When 'other' is a scalar (single number).
            return Interval(self.interval_array[0] - other, self.interval_array[1] - other)
        elif isinstance(other, Interval):
            # When 'other' is also an Interval object.
            p1 = self.interval_array[0] - other.interval_array[1]
            p2 = self.interval_array[1] - other.interval_array[0]
            return Interval(p1, p2)

        else:
            raise TypeError("You can only add an Interval or a scalar to an Interval.")

    def __rsub__(self, other):
        if isinstance(other, (int, float)):
            # Indexes are flipped from __sub__ because [0] must be smaller
            return Interval(other - self.interval_array[1], other - self.interval_array[0])
        else:
            raise TypeError("You can only subtract an Interval from a scalar or another Interval.")

    def __mul__(self, other):
        """
        [a, b] · [c, d] = [min(ac, ad, bc, bd), max(ac, ad, bc, bd)]
        :param other:
        :return:
        """
        if isinstance(other, (int, float)):
            # When 'other' is a scalar (single number).
            return Interval(self.interval_array[0] * other, self.interval_array[1] * other)

        elif isinstance(other, Interval):
            # When 'other' is also an Interval object.

            # min(ac, ad, bc, bd)
            p1 = min(self.interval_array[0] * other.interval_array[0],
                     self.interval_array[0] * other.interval_array[1],
                     self.interval_array[1] * other.interval_array[0],
                     self.interval_array[1] * other.interval_array[1])

            # max(ac, ad, bc, bd)
            p2 = max(self.interval_array[0] * other.interval_array[0],
                     self.interval_array[0] * other.interval_array[1],
                     self.interval_array[1] * other.interval_array[0],
                     self.interval_array[1] * other.interval_array[1])
            return Interval(p1, p2)

        else:
            raise TypeError("You can only add an Interval or a scalar to an Interval.")

    def __rmul__(self, other):
        # Addition is commutative, so we can just call our existing __add__ method
        return self.__mul__(other)

    def __truediv__(self, other):
        """
        [a, b] / [c, d] = [min(a/c, a/d, b/c, b/d), max(a/c, a/d, b/c, b/d)], 0 ∈/ [c, d].
        :param other:
        :return:
        """

        try:
            # min(a/c, a/d, b/c, b/d)
            p1 = min(self.interval_array[0] / other.interval_array[0],
                     self.interval_array[0] / other.interval_array[1],
                     self.interval_array[1] / other.interval_array[0],
                     self.interval_array[1] / other.interval_array[1])

            # max(a/c, a/d, b/c, b/d)
            p2 = max(self.interval_array[0] / other.interval_array[0],
                     self.interval_array[0] / other.interval_array[1],
                     self.interval_array[1] / other.interval_array[0],
                     self.interval_array[1] / other.interval_array[1])
            return Interval(p1, p2)

        except (ValueError, ZeroDivisionError):
            print("Wrong value or division by zero.")
        except TypeError:
            print("Wrong type.")
        """
        Task 6
        Extend your division function so that it raises appropriate exceptions 
        if the dividing interval contains zero, or if the resulting interval 
        would be infinitely large.
        """

    def __rtruediv__(self, other):
        return self / other

    def __contains__(self, item):
        """
        Task 5: Implement the __contains__ method for checking
        if a real value is within the given interval.
        :param item:
        :return:
        """
        # p1 = self.interval_array[0] - item
        # p2 = self.interval_array[1] - item
        # if p1 * p2 <= 0:

        # Cleaner solution
        if self.interval_array[0] <= item <= self.interval_array[1]:
            print(f"Item {item} is in {self.interval_array}")
            return True
        else:
            print(f"Item {item} is not in {self.interval_array}")
            return False

    def __neg__(self):
        """
        Negates the interval.
        :return:
        """
        return Interval(-self.interval_array[1], -self.interval_array[0])

    def __pow__(self, int):
        """
        Power function
        :param int:
        :return:
        """
        if int % 2 == 0:
            if self.interval_array[0] >= 0:
                return Interval(self.interval_array[0] ** int, self.interval_array[1] ** int)
            elif self.interval_array[1] < 0:
                return Interval(self.interval_array[1] ** int, self.interval_array[0] ** int)
            else:
                return Interval(0, max(self.interval_array[0] ** int, self.interval_array[1] ** int))
        else:
            return Interval(self.interval_array[0] ** int, self.interval_array[1] ** int)


"""
Task 4
Make sure that the following code works as expected and prints the values given in the comments
"""
I1 = Interval(1, 4)
I2 = Interval(-2, -1)
print(I1 + I2)  # [-1, 3]
print(I1 - I2)  # [2, 6]
print(I1 * I2)  # [-8, -1]
print(I1 / I2)  # [-4.,-0.5]

"""
Task 7
A real number r is naturally identified with a degenerate interval [r,r]. 
Extend the class so that it can be initialized with only one real value, i.e.
Interval(1) # [1, 1]
"""
I3 = Interval(1)
print(I3)  # [1, 1]

"""
Task 8
Modify your code so that the following works:
"""
print("\n----- Task 8 -----")
print(Interval(2, 3) + 1)  # [3, 4]
print(1 + Interval(2, 3))  # [3, 4]
print(1.0 + Interval(2, 3))  # [3.0, 4.0]
print(Interval(2, 3) + 1.0)  # [3.0, 4.0]
print(1 - Interval(2, 3))  # [-2, -1]
print(Interval(2, 3) - 1)  # [1, 2]
print(1.0 - Interval(2, 3))  # [-2.0, -1.0]

print("\nPart 2 (Task 8)")
print(Interval(2, 3) - 1.0)  # [1.0, 2.0]
print(Interval(2, 3) * 1)  # [2, 3]
print(1 * Interval(2, 3))  # [2, 3]
print(1.0 * Interval(2, 3))  # [2.0, 3.0]
print(Interval(2, 3) * 1.0)  # [2.0, 3.0]
print(-Interval(4, 5))  # see the special method __neg__

"""
Task 9
Implement the power function x 􏰀→ xn (see equations (1) and (2)) as the __pow__ function, so that one can write
"""
x = Interval(-2, 2)  # [-2, 2]
print(x ** 2)  # [0, 4]
print(x ** 3)  # [-8, 8]

"""
Task 10 
Define a list of 1000 intervals by creating a list of lower boundary values with xl=linspace(0.,1,1000) 
and upper boundaries xu=linspace(0.,1,1000)+0.5.
Evaluate the polynomial
p(I)=3I3 −2I2 −5I−1
on each interval I of your list of intervals and create in such a way another list of intervals. 
Extract from this lists a list of lower boundaries yl and upper boundaries yu and plot both versus xl.
The result should look like this:
"""
xl = np.linspace(0., 1, 1000)  # lower boundaries
xu = np.linspace(0., 1, 1000) + 0.5  # upper boundaries
intervals = [Interval(l, u) for l, u in zip(xl, xu)]


def polynomial(interval):
    return (3 * interval ** 3) - (2 * interval ** 2) - (5 * interval) - 1


boundaries = [polynomial(i) for i in intervals]

yl = [i.interval_array[0] for i in boundaries]
yu = [i.interval_array[1] for i in boundaries]

figure(figsize=(10, 6))
plot(xl, yl, label='Lower Boundaries')
plot(xl, yu, label='Upper Boundaries')
legend()
title("p(I)=3I^3 − 2I^2 − 5I − 1, I = Interval(x, x + 0,5)")
xlabel('x')
ylabel('p(I))')
show()
