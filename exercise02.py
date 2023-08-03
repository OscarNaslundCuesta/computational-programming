from numpy import *
from matplotlib.pyplot import *
from scipy import *
import sys

print("----- Task 1 -----\n")
"""
The point x with the property x = sin(x) − ax + 30 is called a fixed point of the
function f (x) = sin(x) − ax + 30. It can be computed with the so-called fixed
point iteration:
x(i+1) = sin(x(i)) − ax(i) + 30 .
Note: (i) denotes an iteration counter not exponentiation! Here you find
a piece of Python code which performs the first 200 steps of this iteration:
x = 0 . 5
a = 0 . 5
for i in range ( 200 ) :
x = sin ( x ) - a * x + 30
print ( f ' The result after { i + 1 } iterations is { x } ')
Modify the code in such a way that it stops iterating as soon as |x(i+1)−x(i)| < 10−8.
Furthermore it should print a little message if this condition was not met within
200 iteration steps. (The absolute value is computed in Python by the function
abs and 10−8 is written as 1.e-8.)
Test your code with a = 0.5 and a = 8.
"""

x = 8
a = 0.5
#
for i in range(200):
    if abs(((sin(x) - a * x + 30) - x)) < 1.e-8:
        i = i
        break
    else:
        x = sin(x) - a * x + 30

print(f' The result after {i + 1} iterations is {x} ')

print("\n----- Task 2 -----\n")
"""
Plot the function with a = 0.5 from the previous task in the range x ∈ [5, 30] and
in the same figure plot also the function y = x. Do you expect that the function
has several fixed points?
Hint: You may want to use the linspace command to generate the x-values.
"""

x = linspace(5, 30)
a = 0.5

plot(x, sin(x) - a * x + 30)
plot(x, x)
# show()


print("\n----- Task 3 -----\n")
"""
It is easy to show that limn→∞ xn = 0. Create a list containing all the elements of
this sequence xn for all n until xn < 10−9. How long is this list?
"""
list = []
n = 1
Found = False

while not Found:
    if (((sin(n)) ** 2) / n) < 1.e-9:
        Found = True
    list.append(n)
    n += 1

print(f"Length of list is {len(list)}")

print("\n----- Task 4 -----\n")
"""
Consider the sequence:
xn+1 = 0.2 xn − α(x2
n − 5) with x0 = 1
for α successively equal to -0.5, +0.5, -0.25, 0.25.
• Check the convergence; if the sequence converges, print the message
Sequence converged to x= <the value you got>
otherwise print
No convergence detected.
• Check whether there are negative elements in the sequence
Hint: If |xn − xn−1| < 10−9 consider a sequence to be convergent.
"""

list_task4 = [0.5, -0.5, 0.25, -0.25]
x = 1

for item in list_task4:
    a = item
    for i in range(1, 100):
        if abs((0.2 * x - a * ((x ** 2) - 5)) - x) < 1.e-9:
            print(f"a = {a} and sequence converged to x = {x} at i = {i}")
            break

        else:
            x = 0.2 * x - a * ((x ** 2) - 5)

print("\n----- Task 6 -----\n")
"""
Write a function which has α as input. The function should perform the con-
vergence test of the sequence given above. It should return True if the sequence
converged within 30 iterations and return False if it didn’t.
Test your function with the same values of α as in Task 4. Try it also with α = 1.
What happens?
"""


def convergence_check(a):
    x = 1
    for i in range(1, 30):
        if abs((0.2 * x - a * ((x ** 2) - 5)) - x) < 1.e-9:
            print(f"a = {a} and sequence converged to x = {x} at i = {i}")
            print("Returning True")
            return True

        else:
            x = 0.2 * x - a * ((x ** 2) - 5)
    print("Returning False")
    return False  # didn't converge


print("\n----- Task 7/8 -----\n")
"""
Give your function a second input argument x0 so that it allows you to test con-
vergence for different α and different starting values x0.

Give your functions two additional output parameters: pos and neg. One of them
should contain the positive elements of the sequence and the other the negative
ones. If there are only positive elements in the sequence neg should be an empty
list and vice versa.
"""


def convergence_check2(a, x0):
    x = x0
    neg = []
    pos = []

    for i in range(1, 30):
        if abs((0.2 * x - a * ((x ** 2) - 5)) - x) < 1.e-9:
            print(f"a = {a} and sequence converged to x = {x} at i = {i}")
            print("Returning True")
            print(f"pos = {pos}, neg = {neg}")
            return True

        else:
            x = 0.2 * x - a * ((x ** 2) - 5)

            if x > 0:
                pos.append(x)
            elif x < 0:
                neg.append(x)

    print("Returning False")
    print(f"pos = {pos}, neg = {neg}")
    return False  # didn't converge


convergence_check2(0.5, 1)
convergence_check2(-0.5, 1)
convergence_check2(0.25, 1)
convergence_check2(-0.25, 1)
