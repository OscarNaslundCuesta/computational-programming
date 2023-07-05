from numpy import *
from matplotlib.pyplot import *
from numpy.linalg import norm

print("----- Task 1 -----\n")
"""
Write a function, which takes a matrix as parameter. It should check if this matrix
is symmetric. The function should return 1 for a symmetric matrix, −1 for a skew-
symmetric matrix and 0 otherwise.
Test your function
"""


def symmetric_check(matrix):
    """
    Checks if matrix is symmetric, skew-symmetric or asymmetric.
    :param matrix:
    :return:
    """
    if allclose(matrix, matrix.T):
        print("Matrix is symmetric.")
        return 1
    elif allclose(matrix, -matrix.T):
        print("Matrix is skew-symmetric.")
        return -1
    else:
        print("Matrix is asymmetric.")
        return 0


matrix1 = zeros((5, 5))
symmetric_check(matrix1)

print("\n----- Task 2 -----\n")
"""
Write a function, which takes two vectors as parameters. It should check if these
vectors are orthogonal. If they are orthogonal it should return True, otherwise
False.
Don’t forget to provide your function with a docstring.
Test your function.
"""


def orthogonal_check(vector1, vector2):
    """
    Checks if two vectors are orthogonal.
    :param vector1:
    :param vector2:
    :return:
    """
    if dot(vector1, vector2) == 0:
        print("They are orthogonal.")
        return True
    else:
        print("They are not orthogonal.")
        return False


a = np.array([3, 2])
b = np.array([-2, 3])

orthogonal_check(a, b)

print("\n----- Task 3 -----\n")
"""
Write a function, which takes a vector as parameter and which returns the cor-
responding normalized vector, i.e. x
‖x‖ . Write two variants of this program: one
in which you compute the norm (use the 2-norm) of the vector by yourself and
another, which uses the function norm from the module numpy.linalg.
"""


def normalize_own(vector):
    norm = sqrt(sum(element**2 for element in vector))
    normalized_vector = vector / norm
    return normalized_vector

def normalize_numpy(vector):
    norm = linalg.norm(vector)
    normalized_vector = vector / norm
    return normalized_vector


print("\n----- Task 4 -----\n")
"""
Show experimentally that the inverse of a rotation matrix is its transpose.
Hint: B is the inverse of A if AB = BA = I, the identity matrix.
Note, in 2D a rotation matrix has the form
(
cos α sin α
− sin α cos α
)
where α can be any angle.
"""

# define the angle in radians
alpha = np.pi / 6  # 30 degrees

# create the rotation matrix
R = array([[cos(alpha), sin(alpha)],
          [-sin(alpha), cos(alpha)]])

# compute the inverse of the rotation matrix
R_inverse = linalg.inv(R)

# compute the transpose of the rotation matrix
R_transpose = R.T

# check if the inverse and transpose are equal
print(allclose(R_inverse, R_transpose))


print("\n----- Task 5 -----\n")
"""
(If you don’t know eigenvalues (yet) skip this task) Construct a 20 × 20 matrix
with the value 4 on its diagonal and the value 1 on its sub- and super-diagonal.
The rest of the matrix is zero. Compute its eigenvalues. (Use the function eig
from the module numpy.linalg). You might also want to check the function diag
for this task
"""