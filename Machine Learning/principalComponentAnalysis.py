```
Write a Python function that performs Principal Component Analysis (PCA) from scratch. The function should take a 2D NumPy array as input, where each row represents a data sample and each column represents a feature. The function should standardize the dataset, compute the covariance matrix, find the eigenvalues and eigenvectors, and return the principal components (the eigenvectors corresponding to the largest eigenvalues). The function should also take an integer k as input, representing the number of principal components to return.

Example
Example:
        input: data = np.array([[1, 2], [3, 4], [5, 6]]), k = 1
        output:  [[0.7071], [0.7071]]
        reasoning: After standardizing the data and computing the covariance matrix, the eigenvalues and eigenvectors are calculated. The largest eigenvalue's corresponding eigenvector is returned as the principal component, rounded to four decimal places.
```


import numpy as np

'''
https://towardsdatascience.com/a-step-by-step-implementation-of-principal-component-analysis-5520cc6cd598

literally just followed this
'''

def pca(data: np.ndarray, k: int):

    mean = np.mean(data, axis=0)
    std_dev = np.std(data, axis=0)
    standardized_data = (data - mean) / std_dev

    covariance_matrix = np.cov(standardized_data, rowvar=False)

    eigenvalues, eigenvectors = np.linalg.eigh(covariance_matrix)

    sorted_index = np.argsort(eigenvalues)[::-1]
    sorted_eigenvalues = eigenvalues[sorted_index]
    sorted_eigenvectors = eigenvectors[:, sorted_index]

    principal_components = sorted_eigenvectors[:, :k]

    for i in range(principal_components.shape[1]):
        if principal_components[0, i] < 0:
            principal_components[:, i] = -principal_components[:, i]

    principal_components_list = np.round(principal_components, 4).tolist()
  
    return principal_components_list
