"""
NUMA01: Computational Programming with Python
Final Project: Sparse Matrices (1st Draft)
Authors:
Date: 2023-07-17
"""
import numpy as np


class SparseMatrix:
    def __init__(self, input_matrix):
        """
        Initializes a CSR matrix
        :param input_matrix:
        """
        if not isinstance(input_matrix, np.ndarray):  # Checks if it is a numpy.array
            raise ValueError("Input must be a numpy array")
        else:
            self.matrix = input_matrix

        # Initialize arrays for storing matrix in CSR form
        self.values = []
        self.col_index = []
        self.row_index = []

        indices = np.nonzero(self.matrix)

        for x, y in zip(*indices):
            self.values.append(self.matrix[x, y])  # get value at the index
            self.col_index.append(y)
            self.row_index.append(x)

        # Convert to numpy arrays (not sure if needed)
        self.values = np.array(self.values)
        self.col_index = np.array(self.col_index)
        self.row_index = np.array(self.row_index)

        self.intern_represent = "CSR"
        self.number_of_nonzero = np.count_nonzero(self.matrix)  # built-in function to count all nonzero elements

    def set_element(self, i, j, aij):
        """
        Sets an element of the matrix
        :param i:
        :param j:
        :param aij:
        :return:
        """
        # Check if the current element is zero and aij is not zero
        if self.matrix[i, j] == 0 and aij != 0:
            self.number_of_nonzero += 1

        # Check if the current element is not zero and aij is zero
        elif self.matrix[i, j] != 0 and aij == 0:
            self.number_of_nonzero -= 1

        # Set the new value
        self.matrix[i, j] = aij


# Example matrix from wikipedia
example_matrix = np.array([
    [5, 0, 0, 0],
    [0, 8, 0, 0],
    [0, 0, 3, 0],
    [0, 6, 0, 0]
])

print(example_matrix)

example = SparseMatrix(example_matrix)

print("values = ", example.values)
print("col_index = ", example.col_index)
print("row_index = ", example.row_index)
print("intern_represent = ", example.intern_represent)
print("number_of_nonzero = ", example.number_of_nonzero)
