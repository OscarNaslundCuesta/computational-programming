from numpy import *
from matplotlib.pyplot import *
from scipy import *
import sys

print("\n----- Task 4 -----\n")

# Let a distance table between some villages be given by the following data
dist_table = [
    0, 20, 30, 40,
    20, 0, 50, 60,
    30, 50, 0, 70,
    40, 60, 70, 0
]

# Construct a list (of lists) which contains this data. Call this list distance. Con-
# struct from this list a list reddistance which contains only the relevant data in
# the following form

# Use slicing for this task. Solve this task in two ways:
# 1. by using for-loops
# 2. by using only list comprehension and slicing (no for loops at all)

reddistance = []

for item in dist_table:
    if item in reddistance or item == 0:
        pass
    else:
        reddistance.append(item)

print(reddistance)

print("\n----- Task 5 -----\n")

A = {'apple', 'pear', 'banana'}
B = {'pear', 'banana', 'strawberry', 'lemon'}


def sym_diff(a, b):
    temp_list = []

    for set_item in a:
        if set_item not in b:
            temp_list.append(set_item)
    set1 = set(temp_list)
    temp_list = []

    for set_item in b:
        if set_item not in a:
            temp_list.append(set_item)
    set2 = set(temp_list)
    final_set = set1.union(set2)

    print(final_set)
    return final_set


sym_diff(A, B)

print("\n----- Task 8 -----\n")
"""
Bisection Method
A continuous function which changes its sign in an interval [a, b] has at least
one root in this interval. Such a root can be found by the bisection method.
This method starts from the given interval. Then it investigates the sign
changes in the subintervals [a, a+b
2 ] and [ a+b
2 , b]. If the sign changes in the
first subinterval, b is redefined to be
b := a + b
2
otherwise a is redefined in the same manner to be
a := a + b
2
and the process is repeated until b − a is less than a given tolerance.
Note, a sign change is characterized by the condition
f (a)f (b) < 0.
Task 8
• Implement this method as a function bisec. It needs the initial interval [a, b]
and the tolerance as arguments.
• bisec should return the final interval and its midpoint.
• Test the method with the function arctan and also with the polynomial
f (x) = 3x2 − 5
in the interval [−0.5, 0.6] and alternatively in [−1.5, −0.4].
If you are uncertain of your results it might be helpful to plot the functions
in the given intervals.
"""


def bisec(a, b):
    if ((3 * (a ** 2) - 5) * ((3 * ((a + b) / 2) ** 2) - 5)) < 0:
        print("Sign change in first interval!")
        b = (a + b) / 2

        if b - a > 0.01:
            bisec(a, b)
        else:
            print(f"a = {a}, b = {b}. Midpoint = {(a + b) / 2}")
            return
    elif ((3 * (((a + b) / 2) ** 2) - 5) * (3 * (b ** 2) - 5)) < 0:
        print("Sign change in second")
        a = (a + b) / 2

        if b - a > 0.01:
            bisec(a, b)
        else:
            print(f"a = {a}, b = {b}. Midpoint = {(a + b) / 2}")
            return
    else:
        print("No sign change detected in interval")


bisec(-1.5, -0.4)

print("\n----- Task 9 -----\n")
"""
Task 9
In the next exercise we will work more with functions. A nice thing in Python is
that functions are objects like everything else, and can be passed to other functions
as input. Try changing your bisec method so that it also has f as an input
argument, i.e. the first line could look like
def bisec (f , interval , tol ) :
Then you can call it like
bisec ( arctan , [1 , 2 ] , 1e - 3 ) % Not a good initial guess
"""


def bisec(f, interval, tol):
    a, b = interval

    if (f(a) * f((a + b) / 2)) < 0:
        print("Sign change in first interval!")
        b = (a + b) / 2

        if b - a > tol:
            interval = (a, b)
            bisec(f, interval, tol)
        else:
            print(f"a = {a}, b = {b}. Midpoint = {(a + b) / 2}")
            return
    elif (f((a+b)/2)) * (f(b)) < 0:
        print("Sign change in second")
        a = (a + b) / 2

        if b - a > tol:
            interval = (a, b)
            bisec(f, interval, tol)
        else:
            print(f"a = {a}, b = {b}. Midpoint = {(a + b) / 2}")
            return
    else:
        print("No sign change detected in interval")


interval_test = (-1.5, -0.4)


def function1(x):
    return 3 * (x ** 2) - 5


bisec(function1, interval_test, 0.01)
