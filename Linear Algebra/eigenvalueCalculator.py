```
Write a Python function that calculates the eigenvalues of a 2x2 matrix. The function should return a list containing the eigenvalues, sort values from highest to lowest.

Example
Example:
        input: matrix = [[2, 1], [1, 2]]
        output: [3.0, 1.0]
        reasoning: The eigenvalues of the matrix are calculated using the characteristic equation of the matrix, which for a 2x2 matrix is $\lambda^2 - 	ext{trace}(A)\lambda + 	ext{det}(A) = 0$, where $\lambda$ are the eigenvalues.
```


import math

def calculate_eigenvalues(matrix: list[list[float|int]]) -> list[float]:
    a = matrix[0][0]
    b = matrix[0][1]
    c = matrix[1][0]
    d = matrix[1][1]
    A = 1
    B = -(a+d)
    C = a * d - b * c

    discriminant = B**2 - 4 * A * C

    lambda1 = (-B + math.sqrt(discriminant)) / (2 * A)
    lambda2 = (-B - math.sqrt(discriminant)) / (2 * A)

    return [lambda1, lambda2]
