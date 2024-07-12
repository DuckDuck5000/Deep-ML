```
Write a Python function that approximates the Singular Value Decomposition on a 2x2 matrix by using the jacobian method and without using numpy svd function, i mean you could but you wouldn't learn anything. return the result in this format.

Example
Example:
        input: a = [[2, 1], [1, 2]]
        output: (array([[-0.70710678, -0.70710678],
                        [-0.70710678,  0.70710678]]),
        array([3., 1.]),
        array([[-0.70710678, -0.70710678],
               [-0.70710678,  0.70710678]]))
        reasoning: U is the first matrix sigma is the second vector and V is the third matrix
```

import numpy as np

def eig_2x2_jacobi(matrix):
    tol = 1e-10
    max_iterations = 100
    V = np.eye(2)
    
    for _ in range(max_iterations):
        if abs(matrix[0, 1]) < tol:
            break
        theta = 0.5 * np.arctan2(2 * matrix[0, 1], matrix[0, 0] - matrix[1, 1])
        c = np.cos(theta)
        s = np.sin(theta)
        
        J = np.array([[c, -s], [s, c]])
        matrix = J.T @ matrix @ J
        V = V @ J
    
    eigenvalues = np.diag(matrix)
    return eigenvalues, V

def svd_2x2_singular_values(A: np.ndarray) -> tuple:
    A = np.array(A)
    
    AtA = A.T @ A
    AAt = A @ A.T
    

    sigma_squared, V = eig_2x2_jacobi(AtA)
    sigma = np.sqrt(sigma_squared)
    
    _, U = eig_2x2_jacobi(AAt)
    
    sorted_indices = np.argsort(-sigma)
    sigma = sigma[sorted_indices]
    U = U[:, sorted_indices]
    V = V[:, sorted_indices]
    
    return U, sigma, V.T


