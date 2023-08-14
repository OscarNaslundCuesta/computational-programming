"""
NUMA01: Computational Programming with Python
Final Project: Sparse Matrices (Draft)
Authors:
Date: 2023-08-08
"""
import numpy as np
from scipy.sparse import csr_matrix, csc_matrix, lil_matrix
import time


class SparseMatrix:
    def __init__(self, input_matrix, tol=10 ** -8):
        """
        Initializes a CSR matrix
        :param input_matrix:
        """
        self.tol = tol
        if not isinstance(input_matrix, np.ndarray):  # Checks if it is a numpy.array
            raise ValueError("Input must be a numpy array")
        else:
            self.matrix = input_matrix

        # Task 6, removing any value lower than tol and replacing with 0
        for i in range(len(self.matrix[0])):
            for j in range(len(self.matrix)):
                if abs(self.matrix[j][i]) == 0:

                    pass
                else:
                    if abs(self.matrix[j][i]) < tol:
                        self.matrix[j][i] = 0

        # Initialize arrays for storing matrix in CSR form
        self.values = []
        self.col_index = []
        self.row_index = [0]  #
        self.number_of_nonzero = 0  # total count of nonzero for the matrix
        self.intern_represent = "CSR"
        self.transposed_matrix = None  # used in CSC

        for row in self.matrix:
            nonzero_count = 0  # the count for the current row
            for i, value in enumerate(row):  # i = col_index
                if value != 0:
                    self.values.append(value)
                    self.col_index.append(i)
                    nonzero_count += 1
            self.number_of_nonzero += nonzero_count  # total count of nonzero
            self.row_index.append(self.row_index[-1] + nonzero_count)  #

        # Convert to numpy arrays (not sure if needed)
        self.values = np.array(self.values)
        self.col_index = np.array(self.col_index)
        self.row_index = np.array(self.row_index)

    def set_element(self, i, j, aij):
        """
        Sets an element of the matrix
        :param i:
        :param j:
        :param aij:
        :return:
        """
        max_row_index = len(self.matrix) - 1
        max_col_index = len(self.matrix[0]) - 1

        # Handling errors
        if not 0 <= i <= max_row_index:
            raise IndexError(f"i (row index) is out of range. Expected between 0 and {max_row_index}, got {i}.")
        if not 0 <= j <= max_col_index:
            raise IndexError(f"j (column index) is out of range. Expected between 0 and {max_col_index}, got {j}.")

        # extract start/end of chosen row i
        row_start = self.row_index[i]
        row_end = self.row_index[i + 1]

        row_values = self.values[row_start:row_end]  # extract the values for the chosen row i
        sublist_col_index = self.col_index[row_start:row_end]  # extract the columns for the values in row_values

        # Check if the current element is zero and aij is not zero
        if j not in sublist_col_index and abs(aij) >= self.tol:
            self.matrix[i, j] = aij
            self.number_of_nonzero += 1

            # inserts the new index in the right order in the sublist
            index = np.searchsorted(sublist_col_index, j)
            sublist_col_index = np.insert(sublist_col_index, index, j)

            row_values = np.insert(row_values, index, aij)

            # Delete old values and insert new ones at right indices
            self.values = np.delete(self.values, slice(row_start, row_end))
            self.values = np.insert(self.values, row_start, row_values)

            # Delete old column indices and insert new ones at right indices
            self.col_index = np.delete(self.col_index, slice(row_start, row_end))
            self.col_index = np.insert(self.col_index, row_start, sublist_col_index)

            # Increase all the elements by one because a value has been added
            self.row_index[i + 1:] += 1

        # Check if the current element is not zero and aij (new value) is zero
        elif j in sublist_col_index and abs(aij) < self.tol:
            self.matrix[i, j] = 0
            self.number_of_nonzero -= 1

            # inserts the new index in the right order in the sublist
            index = np.searchsorted(sublist_col_index, j)
            sublist_col_index = np.delete(sublist_col_index, index)

            row_values = np.delete(row_values, index)

            # Delete old values and insert new ones at right indices
            self.values = np.delete(self.values, slice(row_start, row_end))
            self.values = np.insert(self.values, row_start, row_values)

            # Delete old column indices and insert new ones at right indices
            self.col_index = np.delete(self.col_index, slice(row_start, row_end))
            self.col_index = np.insert(self.col_index, row_start, sublist_col_index)

            # Decrease all the elements by one because a value has been deleted
            self.row_index[i + 1:] -= 1

        # If current element != 0 and aij != 0
        elif j in sublist_col_index and abs(aij) >= self.tol:
            self.matrix[i, j] = aij
            row_values[j] = aij
            self.values[row_start:row_end] = row_values

    # Task 4 converting csr to csc
    def csr_to_csc(self):
        """
        Converts matrix to CSC-form
        :return:
        """
        if self.intern_represent == "CSC":
            return

        self.values = []
        self.col_index = []
        self.row_index = []

        for i in range(len(self.matrix[0])):
            for j in range(len(self.matrix)):
                if self.matrix[j][i] != 0:
                    self.values.append(self.matrix[j][i])
                    self.row_index.append(j)
                    self.col_index.append(i)

        self.values = np.array(self.values)
        self.col_index = np.array(self.col_index)
        self.row_index = np.array(self.row_index)

        self.intern_represent = "CSC"

    # Task 5, checking if two csc matrices is exactly equal
    def is_same(self, other_matrix):
        # Converting both matrices to csc in case one already is csc()
        self.csr_to_csc()
        other_matrix.csr_to_csc()

        if np.array_equal(self.values, other_matrix.values, equal_nan=False):
            pass
        else:
            return False
        if np.array_equal(self.col_index, other_matrix.col_index, equal_nan=False):
            pass
        else:
            return False
        if np.array_equal(self.row_index, other_matrix.row_index, equal_nan=False):
            pass
        else:
            return False
        return True

    # Task 7
    def elementwise_add(self, other_matrix):
        if not isinstance(other_matrix, SparseMatrix):  # checks that other matrix is a sparsematrix object
            raise ValueError('Input has to be a SparseMatrix object')

        if self.matrix.shape == other_matrix.matrix.shape:  # checks that both matrices have the same shape

            sum_matrix = self.matrix + other_matrix.matrix
        else:
            raise ValueError('Matrices must be same shape')

        return SparseMatrix(sum_matrix)

    # Task 8
    def vector_multiplication(self, vector):

        if vector.ndim != 1:
            raise ValueError('Dimension of vector must be one')

        if not isinstance(vector, np.ndarray):
            raise ValueError('Vector musy be numpy array')

        if vector.shape[0] != self.matrix.shape[1]:
            raise ValueError('Vector length and number of matrix columns must match')

        result = np.zeros(self.matrix.shape[0])

        for i in range(self.matrix.shape[0]):  # iterate through rows
            start_index = self.row_index[i]  # index of first nonzero element in row i
            end_index = self.row_index[
                i + 1]  # starting index of nonzero element in next row, correpsonds to ending index of nonzero element in row i
            nonzero_col_indices = self.col_index[
                                  start_index:end_index]  # extracts column indeces in col_index corresponding to nonzero elements in row i
            values = self.values[start_index:end_index]  #
            result[i] = np.sum(values * vector[nonzero_col_indices])

        return result


# Example matrix from wikipedia
example_matrix = np.array([
    [10, 20, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 30, 0, 40, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 50, 60, 70, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 80, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 90, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 100, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 110, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 120, 0, 0, 0, 0, 0],
    [0, 130, 0, 0, 0, 0, 0, 0, 0, 0, 140, 0, 0, 0, 0],
    [150, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 160, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 170, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 180, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 190],
    [200, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 210, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
])

# Task 9
zeros = np.array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
for i in range(10000):
    array_before = example_matrix[:2]
    array_after = example_matrix[2:]
    result_array = np.concatenate((array_before, [zeros], array_after))
    example_matrix = result_array

example = SparseMatrix(example_matrix)

# example.set_element(0,2,25)

print("example.matrix:")
print(example.matrix)
print("values = ", example.values)
print("col_index = ", example.col_index)
print("row_index = ", example.row_index)
print("intern_represent = ", example.intern_represent)
print("number_of_nonzero = ", example.number_of_nonzero)

print("\n" + "CSC-array:")
example.csr_to_csc()

print("values = ", example.values)
print("col_index = ", example.col_index)
print("row_index = ", example.row_index)
print("intern_represent = ", example.intern_represent)
print("number_of_nonzero = ", example.number_of_nonzero)

example_matrix1 = np.array([
    [10, 20, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 30, 0, 40, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 50, 60, 70, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 80, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 90, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 100, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 110, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 120, 0, 0, 0, 0, 0],
    [0, 130, 0, 0, 0, 0, 0, 0, 0, 0, 140, 0, 0, 0, 0],
    [150, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 160, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 170, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 180, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 190],
    [200, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 210, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
])

example_matrix2 = np.array([
    [10, 20, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 30, 0, 40, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 50, 60, 70, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 80, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 90, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 100, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 110, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 120, 0, 0, 0, 0, 0],
    [0, 130, 0, 0, 0, 0, 0, 0, 0, 0, 140, 0, 0, 0, 0],
    [150, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 160, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 170, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 180, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 190],
    [200, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 210, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
])

example1 = SparseMatrix(example_matrix1)
example2 = SparseMatrix(example_matrix2)

if example1.is_same(example2) == True:
    print("\n" + 'Example 1 is the same as example 2')
else:
    print("\n" + 'Example 1 is not the same as example 2')
print('\n')
addedexample = example1.elementwise_add(example2)
print("Addition of example 1 and example 2 =\n", addedexample.matrix)
print('\n')

example_matrix3 = np.array([
    [10, 20, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 30, 0, 40, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 50, 60, 70, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 80, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 90, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 100, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 110, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 120, 0, 0, 0, 0, 0],
    [0, 130, 0, 0, 0, 0, 0, 0, 0, 0, 140, 0, 0, 0, 0],
    [150, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 160, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 170, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 180, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 190],
    [200, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 210, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
])

example3 = SparseMatrix(example_matrix3)

example_matrix4 = np.array([
    [10, 20, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 30, 0, 40, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 50, 60, 70, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 80, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 90, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 100, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 110, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 120, 0, 0, 0, 0, 0],
    [0, 130, 0, 0, 0, 0, 0, 0, 0, 0, 140, 0, 0, 0, 0],
    [150, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 160, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 170, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 180, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 190],
    [200, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 210, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
])

example4 = SparseMatrix(example_matrix4)

vector = np.array([10, 20, 9, 8, 7, 8, 0, 0, 0, 0, 0, 0, 0, 0, 0])

multexample = example1.vector_multiplication(vector)
print("Multiplication of matrix and vector =", multexample)
if example3.is_same(example4) == True:
    print("\n" + 'Example 3 is the same as example 4')
else:
    print("\n" + 'Example 3 is not the same as example 4')
print('\n')

# Task 10
# Given array
data = np.array([
    [10, 20, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 30, 0, 40, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 50, 60, 70, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 80, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 90, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 100, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 110, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 120, 0, 0, 0, 0, 0],
    [0, 130, 0, 0, 0, 0, 0, 0, 0, 0, 140, 0, 0, 0, 0],
    [150, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 160, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 170, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 180, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 190],
    [200, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 210, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
])

# Create instances of your custom sparse matrix class and scipy.sparse.csr_matrix
my_sparse_matrix = SparseMatrix(data)
scipy_sparse_matrix = lil_matrix(data)

# Benchmarking
num_iterations = 1000

# Benchmark insertion
start_time = time.time()
for _ in range(num_iterations):
    my_sparse_matrix.set_element(0, 2, 25)
    end_time = time.time()
print("Custom Insertion Time:", end_time - start_time)

start_time = time.time()
for _ in range(num_iterations):
    scipy_sparse_matrix[0, 2] = 25
    end_time = time.time()
print("SciPy Insertion Time:", end_time - start_time)

# Benchmark matrix summation
start_time = time.time()
for _ in range(num_iterations):
    my_sparse_matrix.elementwise_add(example2)
    end_time = time.time()
print("Custom Summation Time:", end_time - start_time)

start_time = time.time()
for _ in range(num_iterations):
    scipy_sparse_matrix.__add__(example2)
    end_time = time.time()
print("SciPy Summation Time:", end_time - start_time)

# Benchmark matrix-vector multiplication
vector = np.random.rand(data.shape[1])
start_time = time.time()
for _ in range(num_iterations):
    my_sparse_matrix.vector_multiplication(vector)
    end_time = time.time()
print("Custom Multiplication Time:", end_time - start_time)
# print(vector)
# print(my_sparse_matrix.vector_multiplication(vector))
start_time = time.time()
for _ in range(num_iterations):
    scipy_sparse_matrix._mul_vector(vector)
    end_time = time.time()
print("SciPy Multiplication Time:", end_time - start_time)
