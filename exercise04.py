from numpy import *
from matplotlib.pyplot import *

print("----- Task 1 -----\n")
"""
Complex valued functions
(For this task you need knowledge from the following chapters of the course book:
Ch. 2 (numeric types), Ch. 6 (Basic Plotting), Ch. 7 (Passing arguments, Return
Values). The complex valued function f (ϕ, r) = r exp(iϕ) describes a circle with
radius r in the complex plane, when r is kept fixed and ϕ varied between 0 and
2π. Set up a function which evaluates f . Plot this function for a fixed value of
r in the complex plane. (Note: The real part of a complex variable z is obtained
by the command z.real and its imaginary part by z.imag. Recall also that the
imaginary unit i is expressed in Python by 1j)
Let then r vary from 0.1 to 1.0 and make a plot of the corresponding concentric
circles
"""
# imaginary number
z = 1 + 1j


def f(p, r):
    return r * exp(p * 1j)


r_values = linspace(0.1, 1.0, 10)
p_values = linspace(0, 2 * pi)

figure(figsize=(6, 6))

for r in r_values:
    y_values = array([f(p, r) for p in p_values])

    plot(y_values.real, y_values.imag, label=f'r={r:.1f}')

xlabel('Real part')
ylabel('Imaginary part')
title('Concentric Circles in Complex Plane')
legend()
grid(True)
axis('equal')  # to ensure the plot is not distorted
show()


print("\n----- Task 2 -----\n")
"""
Newton’s Method
(For this task you need knowledge from Ch. 7 (Passing arguments, Return
Values), Ch. 9 (Controlling the flow inside the loop) Newton’s method is an
iterative process for finding a zero (root) of a given function f . It is defined
as follows:
xn+1 = xn − f (xn)/f ′(xn).
The iteration is started with a given value x0 and it is ended when |xn+1 − xn|
is less than a given tolerance TOL.
Write a function newton which takes as arguments:
1
• f , the function whose zeroes we are looking for
• f p, a function, which is the derivative of f
• x0 (the start value)
• Tol (the tolerance).
The function should do at most 400 iterations. It is supposed to return the last
obtained value xn+1 together with a variable conv, which tells if convergence was
observed or not.
Note that your function might produce error messages when the sequence diverges
and the numbers grow out of the range of machine numbers. We will show in a
forthcoming lecture how these error messages can be taken care of.
Write a function myfunc which describes a mathematical function of your choice.
You should know its derivative which you are supposed to code as myfuncp.
Test Newton’s method on these functions.
Plan your solution to this task first on paper. Discuss the approach with your
neighbours and with the teaching assistants. Start programming first, when this
sketch of your program was made.
"""


def myfunc(x):  # example function
    return x ** 4 + 20 * x + 1


def myfuncp(x):  # derivative of myfunc
    return 4 * x + 20


def newton(f, fp, x0, tol, i):

    x = x0 - (f(x0) / fp(x0))
    i += 1

    if abs(x - x0) < tol:
        conv = True
        return x, conv, i

    elif i >= 400:
        conv = False
        return x, conv, i

    else:
        return newton(f, fp, x, tol, i)


x0 = -10
i = 0.01
tol = 0.1
final_x, conv, iterations = newton(myfunc, myfuncp, 1, tol, i)

if conv:
    print(f"Root was found at {final_x} after {iterations} iterations")
else:
    print(f"Final x (n+1) was at {final_x} after {iterations} iterations")
