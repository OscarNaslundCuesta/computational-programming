"""
NUMA01: Computational Programming with Python
Final Project: Sparse Matrices (Draft)
Authors:
Date: 2023-07-17
"""
import numpy as np


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
            raise ValueError(f"i (row index) is out of range. Expected between 0 and {max_row_index}, got {i}.")
        if not 0 <= j <= max_col_index:
            raise ValueError(f"j (column index) is out of range. Expected between 0 and {max_col_index}, got {j}.")

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
example.csr_to_csc()

print("values = ", example.values)
print("col_index = ", example.col_index)
print("row_index = ", example.row_index)
print("intern_represent = ", example.intern_represent)
print("number_of_nonzero = ", example.number_of_nonzero)

example_matrix1 = np.array([
    [10, 20, 0, 0, 0, 0],
    [0, 30, 0, 40, 0, 0],
    [0, 0, 50, 60, 70, 0],
    [0, 0, 0, 0, 0, 80]
])
example_matrix2 = np.array([
    [10, 20, 0, 0, 0, 0],
    [0, 30, 0, 40, 0, 0],
    [0, 0, 50, 60, 70, 0],
    [0, 0, 0, 0, 0, 80]
])

example1 = SparseMatrix(example_matrix1)
example2 = SparseMatrix(example_matrix2)

print(example1.is_same(example2))
