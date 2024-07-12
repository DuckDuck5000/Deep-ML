```
Write a Python function that transforms a given matrix A using the operation 
, where T and S are invertible matrices. The function should first validate if the matrices T and S are invertible, and then perform the transformation.

Example
Example:
        input: A = [[1, 2], [3, 4]], T = [[2, 0], [0, 2]], S = [[1, 1], [0, 1]]
        output: [[0.5, 1.0], [1.5, 2.0]]
        reasoning: The matrices T and S are used to transform matrix A by computing $T^{-1}AS$.
```

import numpy as np

def transform_matrix(A: list[list[int | float]], T: list[list[int | float]], S: list[list[int | float]]) -> list[list[int | float]]:
    A = np.array(A)
    T = np.array(T)
    S = np.array(S)
    
    T_inv = np.linalg.inv(T)
    
    result = T_inv @ A @ S
    
    return result.tolist()
