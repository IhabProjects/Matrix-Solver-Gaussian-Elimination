# Matrix Solver - Gaussian Elimination

This program solves systems of linear equations using Gaussian elimination and back substitution. It reads a matrix from a file, converts it to upper triangular form, and finds the solution.

## How it works

1. Reads matrix from `matrix.txt`
2. Converts to upper triangular form using row operations
3. Solves using back substitution

## Files

- `matrix_solver.py` - main program
- `utils.py` - the math functions
- `matrix.txt` - input file
- `tests/` - test files

## Usage

1. Put your matrix in `matrix.txt` like this:

```
3
2 4 10 36
2 3 8 31
3 5 7 33
```

First line is the size, then each row has coefficients + constant term.

2. Run it:

```bash
python3 matrix_solver.py
```

## Example

Input matrix:

```
2x + 4y + 10z = 36
2x + 3y + 8z = 31
3x + 5y + 7z = 33
```

Output:

```
Original matrix:
['    2.00', '    4.00', '   10.00', '   36.00']
['    2.00', '    3.00', '    8.00', '   31.00']
['    3.00', '    5.00', '    7.00', '   33.00']

Upper triangular matrix:
['    2.00', '    4.00', '   10.00', '   36.00']
['    0.00', '   -1.00', '   -2.00', '   -5.00']
['    0.00', '    0.00', '   -6.00', '  -16.00']

Solution:
x1 = 5.3333
x2 = -0.3333
x3 = 2.6667
```

## Testing

Run the tests:

```bash
cd tests
python3 test.py
```

## The Algorithm

**Gaussian Elimination:**

- For each column, find a non-zero pivot
- Swap rows if needed to get a good pivot
- Eliminate all elements below the pivot using row operations

**Back Substitution:**

- Start from the last equation
- Solve for each variable by substituting known values

## Error Handling

The program handles:

- Missing files
- Invalid data
- Zero pivots (tries to swap rows)
- Singular matrices

## Requirements

- Python 3.6+

_This project was created as part of MTH-2303-02 coursework to demonstrate practical implementation of numerical linear algebra algorithms._
