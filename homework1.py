# -*- coding: utf-8 -*-
"""
NUMA01: Computational Programming with Python
Homework 1
Authors: Oscar Näslund Cuesta, Levi Tuoremaa
Date: 2023-06-29
"""

from numpy import sqrt, zeros, linspace, log, subtract
from matplotlib.pyplot import figure, plot, legend, yscale, title, scatter, xlabel, ylabel, ylim, show


def approx_ln(x, n):
    # Initialize a & g
    a0 = (1 + x) / 2
    g0 = sqrt(x)

    a = [a0]
    g = [g0]

    for i in range(0, n):
        an = (a[i] + g[i]) / 2
        gn = sqrt(an * g[i])

        a.append(an)
        g.append(gn)

    approx = (x - 1) / a[n]
    return (approx)


def fast_approx_ln(x, n):
    a0 = (1 + x) / 2
    g0 = sqrt(x)

    a = [a0]
    g = [g0]

    for i in range(0, n):
        an = (a[i] + g[i]) / 2
        gn = sqrt(an * g[i])

        a.append(an)
        g.append(gn)

    # Create a matrix of zeros with dimensions (n+1)*(n+1)
    d = zeros((n + 1, n + 1))

    for i in range(0, n + 1):
        d[0, i] = a[i]
        for k in range(1, i + 1):
            d[k, i] = (d[k - 1, i] - (4 ** (-k)) * d[k - 1, i - 1]) / (1 - 4 ** (-k))

    return ((x - 1) / d[n, n])


# Task 2: Plot both functions

lin_x = linspace(0.01, 20, 100)  # Creates 100 evenly spaced points in the interval [0.01, 20]
ln_x = [log(k) for k in lin_x]
approx1 = [approx_ln(k, 1) for k in lin_x]
approx3 = [approx_ln(k, 3) for k in lin_x]
approx5 = [approx_ln(k, 5) for k in lin_x]

figure()
plot(lin_x, ln_x, label="ln(x)")
plot(lin_x, approx1, label="approx_ln with n=1")
plot(lin_x, approx3, label="n=3")
plot(lin_x, approx5, label="n=5")
legend()
yscale("log")  # Set the scale of the y-axis to logarithmic
title("Comparison of ln(x) with approx_ln")

# Task 2b: Plot the difference of the functions
figure()
# The 'subtract' method is used for element-wise subtraction.
plot(lin_x, subtract(approx1, ln_x), label="n=1")
plot(lin_x, subtract(approx3, ln_x), label="n=3")
plot(lin_x, subtract(approx5, ln_x), label="n=5")
title("Difference between ln(x) and approx_ln")
legend()

# Task 3

x = 1.41

n_error = []
for i in range(1, 20):
    approximation = approx_ln(x, i)
    correct_ln = log(x)
    n_error.append(abs(approximation - correct_ln))

figure()
plot(n_error)
title("Error value between ln(x) and approx_ln for different values of n")
xlabel("n")
yscale("log")

# Task 5

lin_x = linspace(0.01, 20, 1000)
it2 = [fast_approx_ln(k, 2) for k in lin_x]
it3 = [fast_approx_ln(k, 3) for k in lin_x]
it4 = [fast_approx_ln(k, 4) for k in lin_x]
it5 = [fast_approx_ln(k, 5) for k in lin_x]
it6 = [fast_approx_ln(k, 6) for k in lin_x]
ln = [log(k) for k in lin_x]
figure(figsize=(9, 6))  # Sets the size of the figure to higher than default
scatter(lin_x, abs(subtract(it2, ln)), label="Iteration 2")
scatter(lin_x, abs(subtract(it3, ln)), label="Iteration 3")
scatter(lin_x, abs(subtract(it4, ln)), label="Iteration 4")
scatter(lin_x, abs(subtract(it5, ln)), label="Iteration 5")
scatter(lin_x, abs(subtract(it6, ln)), label="Iteration 6")
legend()
title("Error behavior of the accelerated Carlson method for the log")
xlabel("x")
ylabel("error")
ylim([1.0e-19, 1.0e-5])  # Limit the y-axis to this range
yscale("log")  # Set the scale of the y-axis to logarithmic
show()
