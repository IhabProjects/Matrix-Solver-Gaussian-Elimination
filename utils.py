def input_matrix(fh, matrix):
    # reads the matrix from file
    # first line is the size n, then n lines of matrix data
    line_number = 0
    for line in fh:
        if line_number == 0:
            # First line contains the matrix size
            n = int(line.strip())
            rows = cols = n
        else:
            # Parse each row: split by whitespace and convert to floats
            matrix.append(list(map(float, line.strip().split())))
        line_number += 1

def find_first_non0(matrix, row, col):
    # looks for a non-zero element in the column to use as pivot
    # returns 1 if we swapped rows, 0 if no swap needed
    n = len(matrix)
    
    # If current pivot is already non-zero, no swap needed
    if matrix[row][col] != 0:
        return 0
    
    # Look for a non-zero element in the column below current row
    for i in range(row + 1, n):
        if matrix[i][col] != 0:
            swap(matrix, row, i)
            return 1  # Swap was made
    
    return 0  # No non-zero element found

def make_first_0(matrix, row, col):
    # makes all elements below the pivot zero using row operations
    # this is the main elimination step in gaussian elimination
    n = len(matrix)
    
    # Ensure we have a non-zero pivot element
    if matrix[row][col] == 0:
        return  # Cannot proceed with zero pivot
    
    # For each row below the pivot row
    for i in range(row + 1, n):
        if matrix[i][col] != 0:  # Only process non-zero elements
            # Calculate the elimination multiplier
            c = matrix[i][col] / matrix[row][col]
            
            # Perform row operation: row_i = row_i - c * pivot_row
            # Include the constant term (rightmost column) in elimination
            for j in range(col, n + 1):
                matrix[i][j] = matrix[i][j] - c * matrix[row][j]


def swap(matrix, not0, is0):
    # swaps two rows in the matrix
    matrix[not0], matrix[is0] = matrix[is0], matrix[not0]
   
   
def make_upper_tree(matrix):
    # converts the matrix to upper triangular form
    # goes through each column and eliminates elements below the diagonal
    n = len(matrix)
    
    # Process each column (except the last one)
    for j in range(n - 1):
        # Ensure we have a non-zero pivot at position [j][j]
        if find_first_non0(matrix, j, j) == 0 and matrix[j][j] == 0:
            # If no non-zero element found, matrix may be singular
            continue  # Skip this column
        
        # Eliminate all elements below the pivot
        make_first_0(matrix, j, j)
        
        
def back_substitute(matrix):
    # solves the upper triangular system using back substitution
    # starts from the bottom and works its way up
    n = len(matrix)
    
    # Initialize solution vector
    x = [0.0] * n
    
    # Solve from bottom row to top row
    for i in range(n - 1, -1, -1):
        # Check for zero diagonal element (singular matrix)
        if matrix[i][i] == 0:
            print("Error: Cannot solve - diagonal element is zero")
            return None
        
        # Start with the constant term (rightmost column)
        x[i] = matrix[i][n]
        
        # Subtract contributions from already-solved variables
        for j in range(i + 1, n):
            x[i] = x[i] - matrix[i][j] * x[j]
        
        # Divide by the coefficient of the current variable
        x[i] = x[i] / matrix[i][i]
    
    return x