import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utils import input_matrix, make_upper_tree

def test_matrix_operations():
    #Test the matrix upper triangular conversion
    
    # Test with the test file
    matrix = []
    
    try:
        with open("test.txt", 'r', encoding="utf-8") as file:
            input_matrix(file, matrix)
            
            print("Test Matrix - Original:")
            print_matrix(matrix)
            
            # Convert to upper triangular
            make_upper_tree(matrix)
            
            print("\nTest Matrix - Upper Triangular:")
            print_matrix(matrix)
            
            # Verify it's upper triangular
            if is_upper_triangular(matrix):
                print("\nTEST PASSED: Matrix is upper triangular")
            else:
                print("\nTEST FAILED: Matrix is not upper triangular")
                
    except Exception as e:
        print(f"TEST FAILED: {e}")

def print_matrix(matrix):
    """Pretty print the matrix"""
    for row in matrix:
        print([f"{x:6.2f}" for x in row])

def is_upper_triangular(matrix):
    """Check if matrix is upper triangular"""
    n = len(matrix)
    for i in range(n):
        for j in range(i):
            if abs(matrix[i][j]) > 1e-10:  # Account for floating point errors
                return False
    return True

if __name__ == "__main__":
    test_matrix_operations()