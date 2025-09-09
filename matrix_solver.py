from utils import input_matrix, make_upper_tree, back_substitute

def main():
    matrix = []
    
    try: 
        with open("matrix.txt", 'r', encoding="utf-8") as file:
            # creating the matrix
            input_matrix(file, matrix)
            
            print("Original matrix:")
            print_matrix(matrix)
            
            # convert to upper triangular form
            make_upper_tree(matrix)
            
            print("\nUpper triangular matrix:")
            print_matrix(matrix)
            
            # solve the system using back substitution
            solution = back_substitute(matrix)
            
            if solution:
                print("\nSolution:")
                for i in range(len(solution)):
                    print(f"x{i+1} = {solution[i]:.4f}")
            else:
                print("\nNo unique solution exists")
            
    except FileNotFoundError:
        print("ERROR: matrix.txt file not found")
    except ValueError as e:
        print(f"ERROR: Invalid data in file - {e}")
    except Exception as e:
        print(f"ERROR: {e}")

def print_matrix(matrix):
    # pretty print the matrix
    for row in matrix:
        print([f"{x:8.2f}" for x in row])

if __name__ == "__main__":
    main()