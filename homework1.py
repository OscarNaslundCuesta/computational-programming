from numpy import *
from matplotlib.pyplot import *
from scipy import *
import sys
import math


# Task 1


def approx_ln(x, n):
    if x <= 0 or n <= 0:
        print("Error: x and n must be greater than 0")
        return

    # Initialize a & g
    a = (1 + x) / 2
    g = x ** 0.5

    def update_a(a, g):
        a = (a + g) / 2
        return a

    def update_g(a, g):  # a i+1 is used as input
        g = (a * g) ** 0.5
        return g

    for i in range(n):
        # print(f"Updating for the {i} time")
        a = update_a(a, g)
        g = update_g(a, g)

    # approximate ln(x)
    # print(f"Approximate for ln(x) = {(x - 1) / a}")
    return (x - 1) / a


# Task 2
xplot = [i for i in range(1, 11)]
approx_ln_y = [approx_ln(i, 1) for i in xplot]
ln_y = [log(i) for i in xplot]
diff = [y1 - y1 for y1, y2 in zip(approx_ln_y, ln_y)]

#plot(xplot, approx_ln_y)
#plot(xplot, ln_y)
#plot(xplot, diff)
#show()


# Task 3

approx_ln_n_value = [approx_ln(1.41, i) for i in xplot]
ln_y = log(1.41)
diff2 = [abs(y1 - ln_y) for y1 in approx_ln_n_value]

plot(xplot, diff2)
show()


# Task 4


def fast_approx_ln(x, n):
    if x <= 0 or n <= 0:
        print("Error: x and n must be greater than 0")
        return

    # Initialize a & g
    a = (1 + x) / 2
    g = sqrt(x)

    a_list = [a]
    g_list = [g]

    def update_a(a, g):
        a = (a + g) / 2
        a_list.append(a)
        return a

    def update_g(a, g):  # a i+1 is used as input
        g = sqrt(a * g)
        g_list.append(g)
        return g


    def d(k, n):


        d0n = a[n]
        d0n_neg1 = a[n-1]
        d1n = (d0n - (2 ** (-2 * k)) * d0n_neg1) / (1 - (2 ** (-2 * k)))

        def update_d(k, d_k_neg1_n, d_k_neg1_n_neg1):
            pass




    for i in range(n):
        print(f"Updating for the {i} time")
        a = update_a(a, g)
        g = update_g(a, g)

    # approximate ln(x)
    print(f"Approximate for ln(x) = {(x - 1) / a}")
    return (x - 1) / a

