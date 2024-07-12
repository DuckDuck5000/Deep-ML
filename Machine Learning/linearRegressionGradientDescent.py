```
Write a Python function that performs linear regression using gradient descent. The function should take NumPy arrays X (features with a column of ones for the intercept) and y (target) as input, along with learning rate alpha and the number of iterations, and return the coefficients of the linear regression model as a NumPy array. Round your answer to four decimal places. -0.0 is a valid result for rounding a very small number.

Example
Example:
        input: X = np.array([[1, 1], [1, 2], [1, 3]]), y = np.array([1, 2, 3]), alpha = 0.01, iterations = 1000
        output: np.array([0.1107, 0.9513])
        reasoning: The linear model is y = 0.0 + 1.0*x, which fits the input data after gradient descent optimization
```


import numpy as np

def compute_cost(X, y, theta):
    m = len(y)
    predictions = X.dot(theta)
    cost = (1 / (2 * m)) * np.sum((predictions - y) ** 2)
    return cost

def linear_regression_gradient_descent(X, y, alpha, iterations):
    m, n = X.shape
    theta = np.zeros(n)
    cost_history = np.zeros(iterations)
    
    for i in range(iterations):
        predictions = X.dot(theta)
        errors = np.dot(X.T, (predictions - y))
        theta -= (alpha / m) * errors
        cost_history[i] = compute_cost(X, y, theta)
    
    return np.round(theta, 4)
