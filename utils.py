def input_matrix(fh, matrix):
   line_number = 0
   for line in fh:
       if line_number == 0:
           # since our target 
           n = int(line.strip())
           rows = cols = n
       else:
           # take the  line make sure there is no whitespace then split the line into a list of integers which is the row
           matrix.append(list(map(float, line.strip().split())))
       line_number += 1

def find_first_non0(matrix, row, col):
   n = len(matrix)
   # Look for a non-zero element in the column starting from current row
   for i in range(row + 1, n): 
       if matrix[row][col] != 0:  # if current element is already non-zero, no need to swap
           return 0  # No swap needed
       elif matrix[i][col] != 0:  #looking for non-zero element to swap with
           swap(matrix, row, i)
           return 1 #means that we found a row that has the 0 in the col and that we swapped them
   return 0

def make_first_0(matrix, row, col): # the row and col is given cux matrix[row][col] is going to be mutliplied by something and added to the matrix[i][col], i have to multiply it by c = matrix[i][col] / matrix[row][col] 
    # i have to make all the matrix[i][col] = 0 but not just like that it has to be by mathematical equation
    n = len(matrix)
    
    # Make sure we have a non-zero pivot element
    if matrix[row][col] == 0:
        return  # Can't proceed if pivot is zero
    
    # For each row below the current row
    for i in range(row + 1, n):
        if matrix[i][col] != 0:  # Only process if element is non-zero
            # Calculate the multiplier: c = matrix[i][col] / matrix[row][col]
            c = matrix[i][col] / matrix[row][col]
            
            # For each column in the row, subtract c * pivot_row element
            for j in range(col, n + 1):  # Start from col since previous elements should already be 0, include constant term
                matrix[i][j] = matrix[i][j] - c * matrix[row][j]


def swap(matrix, not0, is0):
   matrix[not0], matrix[is0] = matrix[is0], matrix[not0]
   
   
def make_upper_tree(matrix): # it will call the make_first_0 as many times till we have our upper tree
    n = len(matrix)
    
    # For each column (and corresponding diagonal element)
    for j in range(n - 1):  # Don't need to process last column
        # Try to get a non-zero pivot at matrix[j][j]
        if find_first_non0(matrix, j, j) == 0 and matrix[j][j] == 0:
            # If we can't find a non-zero element to swap, matrix might be singular
            continue  # or handle this case as needed
        
        # Make all elements below the pivot zero
        make_first_0(matrix, j, j)
        
        
def back_substitute(matrix): # takes the upper triangular matrix and solves for x values using back substitution
    # get the size of the matrix (n x n system)
    n = len(matrix)
    
    # create a list to store our solutions
    x = [0.0] * n
    
    # start from the bottom row and work our way up
    for i in range(n - 1, -1, -1):
        # check if the diagonal element is zero (can't divide by zero)
        if matrix[i][i] == 0:
            print("Error: Can't solve - diagonal element is zero")
            return None
        
        # start with the constant term (the rightmost column)
        x[i] = matrix[i][n]
        
        # subtract all the known variables (the ones we already solved for)
        for j in range(i + 1, n):
            x[i] = x[i] - matrix[i][j] * x[j]
        
        # divide by the coefficient of the current variable
        x[i] = x[i] / matrix[i][i]
    
    return x