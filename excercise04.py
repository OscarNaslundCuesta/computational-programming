from numpy import *
from matplotlib.pyplot import *
from scipy.integrate import quad
from scipy.optimize import fsolve

print("----- Task 1 -----\n")
"""
Compute approximately the integral
∫ π/2
0
sin(ωx)dx
for ω = 2π.
For this end run at the beginning of your program the import statement
from scipy . integrate import quad
The method to integrate a function f over an interval [a, b] is quad (quadrature is
another word for integrate) and it is used as quad(f,a,b).
It returns a tuple with the approximated solution and the estimated error. Check
the help page of that function to see if it has some default arguments which you
could set by other values.
"""


def f(x, w):
    return sin(w * x)


integral = quad(f, 0, pi / 2, args=(2 * pi,))  # args gives the second argument w to f()
print(integral)

print("\n----- Task 2 -----\n")
"""
Compute the integral
π/2
∫ sin(ωx)dx
0

for 1000 equidistant values of ω in the interval [0, 2π]
and plot the results versus ω.
Label the axes and put a title to the plot
"""

w = linspace(0, 2 * pi, 1000)  # 1000 equidistant values
x = linspace(0, pi / 2, 1000)

integral_values = []
for value in w:
    integral = quad(f, 0, pi / 2, args=(value,))
    integral_values.append(integral[0])  # appends the value, not the error

plot(w, integral_values)
xlabel('ω')
ylabel('Integral value')
title('Integral of sin(ωx) from 0 to π/2 for various ω')
grid(True)
show()

print("\n----- Task 3 -----\n")
"""
Zeros of a function
In a previous training exercise you wrote your own program to find a zero (noll-
ställe) of a given function. Now we see how this can be done by a scipy method.
For this end use first
from scipy . optimize import fsolve
The simplest use of the method is fsolve(f,x0) where f is the function of which
a zero is calculated and x0 is a guess where you expect the zero.
Compute the positive zero of the polynomial p(x) = x2 + x − 3 .
"""


def p(x):
    return x ** 2 + x - 3


x0 = 1.5
print(fsolve(p, x0))


print("\n----- Task 4 -----\n")
"""
Zeros of a parameter dependent function
Plot the positive zeros of the polynomials p(x) = ax2 + x − 3 for a ∈ [1, 5] versus
a.
Do the zeros depend linearly on a?
"""
a = linspace(1, 5)
x0 = 1

def p(x, a):
    return (a * x ** 2) + x - 3


zero_values = [fsolve(p, x0, args=(value,)) for value in a]     # using list comprehension

plot(a, zero_values)
xlabel('a')
ylabel('Zero values')
title('Positive zeros of ax2 + x − 3 versus a')
grid(True)
show()