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

def eig_2x2(matrix):
    """ Compute the eigenvalues and eigenvectors of a 2x2 matrix. """
    a, b = matrix[0, 0], matrix[0, 1]
    c, d = matrix[1, 0], matrix[1, 1]
    trace = a + d
    determinant = a * d - b * c
    eigenvalue1 = trace / 2 + np.sqrt((trace / 2) ** 2 - determinant)
    eigenvalue2 = trace / 2 - np.sqrt((trace / 2) ** 2 - determinant)
    eigenvector1 = np.array([b, eigenvalue1 - a]) if b != 0 else np.array([eigenvalue1 - d, c])
    eigenvector2 = np.array([b, eigenvalue2 - a]) if b != 0 else np.array([eigenvalue2 - d, c])
    eigenvector1 /= np.linalg.norm(eigenvector1)
    eigenvector2 /= np.linalg.norm(eigenvector2)
    return np.array([eigenvalue1, eigenvalue2]), np.array([eigenvector1, eigenvector2]).T

def svd_2x2_singular_values(A):
    AtA = A.T @ A
    AAt = A @ A.T

    eigvals_V, V = eig_2x2(AtA)
    eigvals_U, U = eig_2x2(AAt)

    sigma = np.sqrt(eigvals_V)

    sorted_indices = np.argsort(-sigma)
    sigma = sigma[sorted_indices]
    U = U[:, sorted_indices]
    V = V[:, sorted_indices]

    if np.linalg.det(V) < 0:
        V[:, -1] *= -1

    return U, sigma, V
