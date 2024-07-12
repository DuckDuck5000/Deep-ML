```
Solve Linear Equations using Jacobi Method (medium)
✔
Write a Python function that uses the Jacobi method to solve a system of linear equations given by Ax = b. The function should iterate 10 times, rounding each intermediate solution to four decimal places, and return the approximate solution x.

Example
Example:
        input: A = [[5, -2, 3], [-3, 9, 1], [2, -1, -7]], b = [-1, 2, 3], n=2
        output: [0.146, 0.2032, -0.5175]
        reasoning: The Jacobi method iteratively solves each equation for x[i] using the formula x[i] = (1/a_ii) * (b[i] - sum(a_ij * x[j] for j != i)), where a_ii is the diagonal element of A and a_ij are the off-diagonal elements.
```


import numpy as np

def solve_jacobi(A: np.ndarray, b: np.ndarray, n: int) -> list:
    num_equations = len(A)
    
    x = np.zeros(num_equations)
    
    for _ in range(n):
        x_new = np.copy(x)
        
        for i in range(num_equations):
            sum_off_diagonal = sum(A[i][j] * x[j] for j in range(num_equations) if j != i)
            
            x_new[i] = (b[i] - sum_off_diagonal) / A[i][i]
        
        x = np.round(x_new, 4)
    
    return x.tolist()
