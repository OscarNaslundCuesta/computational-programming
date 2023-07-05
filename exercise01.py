from scipy import *
from matplotlib.pyplot import *
import sys
import numpy


print("----- Task 2 -----\n")

x = 2.3
equation = x ** 2 + 0.25 * x - 5
print(equation)


print("\n----- Task 6/8 -----\n")

L1_task6 = []
for i in range(100):
    L1_task6.append(i)

L2_task6 = [i / 99 for i in L1_task6]

len(L2_task6)


print("\n----- Task 9 -----\n")

xplot = L2_task6
yplot = [numpy.arctan(i) for i in xplot]


print("\n----- Task 10 -----\n")

plot(xplot, yplot)
plot(yplot, xplot)
show()


print("\n----- Task 11 -----\n")

sum = 0
for i in range(1, 201):
    sum += 1 / (i**0.5)
print(sum)