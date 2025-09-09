# Matrix Solver - Gaussian Elimination with Back Substitution
# Solves nxn systems of linear equations

from utils import input_matrix, make_upper_tree, back_substitute


def main():
    # main function that reads matrix, converts to upper triangular, and solves
    matrix = []
    
    try:
        with open("matrix.txt", 'r', encoding="utf-8") as file:
            # Load matrix from file
            input_matrix(file, matrix)
            
            print("Original matrix:")
            print_matrix(matrix)
            
            # Convert to upper triangular form using Gaussian elimination
            make_upper_tree(matrix)
            
            print("\nUpper triangular matrix:")
            print_matrix(matrix)
            
            # Solve the system using back substitution
            solution = back_substitute(matrix)
            
            if solution:
                print("\nSolution:")
                for i in range(len(solution)):
                    print(f"x{i+1} = {solution[i]:.4f}")
            else:
                print("\nNo unique solution exists")
            
    except FileNotFoundError:
        print("ERROR: matrix.txt file not found")
        print("Please ensure the file exists and contains valid matrix data.")
    except ValueError as e:
        print(f"ERROR: Invalid data in file - {e}")
        print("Please check that all values are numeric.")
    except Exception as e:
        print(f"ERROR: {e}")

def print_matrix(matrix):
    # prints the matrix in a nice format
    for row in matrix:
        print([f"{x:8.2f}" for x in row])

if __name__ == "__main__":
    main()