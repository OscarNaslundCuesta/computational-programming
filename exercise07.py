from numpy import *
from matplotlib.pyplot import *

# Also called exercise06a
print("----- Task 1 -----\n")
"""
A central theorem in linear algebra says that the eigenvalues of real symmetric
matrices are real and that their eigenvectors are orthogonal. Try to verify this
theorem by using square random matrices of dimensions not less then 5.
Test your function.
"""

print("\n----- Task 2 -----\n")
"""
Given a vector u ∈ Rn. Construct a n × nmatrix A with the properties
Ai,i = −2ui, i = 1, . . . , n
Ai+1,i = ui i = 1, . . . , n − 1
Ai,i+1 = ui+1 i = 1, . . . , n − 1
and all other elements being zero.
Do this task by using the numpy command diag and alternatively, by using for-
loops. Write a function, that takes a vector and returns such a matrix
"""



print("\n----- Task 3 -----\n")
"""
Call the function you created in the last task with u=linspace(0,2*pi,500)
as input to get a matrix D. Compute the matrix sin(D). Multiply this matrix
with the one-vector (a vector filled with 1’s.) and plot the result versus u.
"""