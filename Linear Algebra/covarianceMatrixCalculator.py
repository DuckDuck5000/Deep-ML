```
Calculate Covariance Matrix (medium)
✔
Write a Python function that calculates the covariance matrix from a list of vectors. Assume that the input list represents a dataset where each vector is a feature, and vectors are of equal length.

Example
Example:
        input: vectors = [[1, 2, 3], [4, 5, 6]]
        output: [[1.0, 1.0], [1.0, 1.0]]
        reasoning: The dataset has two features with three observations each. The covariance between each pair of features (including covariance with itself) is calculated and returned as a 2x2 matrix.
```



import numpy as np

def calculate_covariance_matrix(vectors: list[list[float]]) -> list[list[float]]:
    
    data = np.array(vectors)
    
    n = data.shape[1]
    means = np.mean(data, axis=1)
    covariance_matrix = np.zeros((data.shape[0], data.shape[0]))
   
    for i in range(data.shape[0]):
        for j in range(data.shape[0]):
            covariance_matrix[i, j] = np.sum((data[i] - means[i]) * (data[j] - means[j])) / (n - 1)
    
    return covariance_matrix.tolist()
