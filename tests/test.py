# Test file for the matrix solver
# Tests if the upper triangular conversion works correctly

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utils import input_matrix, make_upper_tree


def test_matrix_operations():
    # tests the matrix conversion to upper triangular form
    matrix = []
    
    try:
        with open("test.txt", 'r', encoding="utf-8") as file:
            input_matrix(file, matrix)
            
            print("Test Matrix - Original:")
            print_matrix(matrix)
            
            # Convert to upper triangular form
            make_upper_tree(matrix)
            
            print("\nTest Matrix - Upper Triangular:")
            print_matrix(matrix)
            
            # Verify the result is upper triangular
            if is_upper_triangular(matrix):
                print("\nTEST PASSED: Matrix is upper triangular")
            else:
                print("\nTEST FAILED: Matrix is not upper triangular")
                
    except Exception as e:
        print(f"TEST FAILED: {e}")

def print_matrix(matrix):
    # prints the matrix nicely
    for row in matrix:
        print([f"{x:6.2f}" for x in row])

def is_upper_triangular(matrix):
    # checks if the matrix is upper triangular (zeros below diagonal)
    n = len(matrix)
    tolerance = 1e-10  # Account for floating point errors
    
    for i in range(n):
        for j in range(i):  # Check elements below diagonal
            if abs(matrix[i][j]) > tolerance:
                return False
    return True

if __name__ == "__main__":
    test_matrix_operations()