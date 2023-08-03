"""
NUMA01: Computational Programming with Python
Final Project: Sparse Matrices (2nd Draft)
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
        # Check if the current element is zero and aij is not zero
        if self.matrix[i, j] == 0 and aij != 0:
            self.number_of_nonzero += 1

        # Check if the current element is not zero and aij is zero
        elif self.matrix[i, j] != 0 and aij == 0:
            self.number_of_nonzero -= 1

        # Set the new value
        self.matrix[i, j] = aij

    def csr_to_csc(self):
        """
        Converts matrix to CSC-form
        :return:
        """
        # self.transposed_matrix = self.matrix.T  # transposes the matrix
        # self.values = []
        # self.col_index = []
        # self.row_index = [0]
        self.intern_represent = "CSC"


# Example matrix from wikipedia
example_matrix = np.array([
    [10, 20, 0, 0, 0, 0],
    [0, 30, 0, 40, 0, 0],
    [0, 0, 50, 60, 70, 0],
    [0, 0, 0, 0, 0, 80]
])

example = SparseMatrix(example_matrix)

print("example.matrix:")
print(example.matrix)
print("values = ", example.values)
print("col_index = ", example.col_index)
print("row_index = ", example.row_index)
print("intern_represent = ", example.intern_represent)
print("number_of_nonzero = ", example.number_of_nonzero)

print("\n" + "CSC-array:")
