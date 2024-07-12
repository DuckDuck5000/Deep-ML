```
Write a Python function that performs feature scaling on a dataset using both standardization and min-max normalization. The function should take a 2D NumPy array as input, where each row represents a data sample and each column represents a feature. It should return two 2D NumPy arrays: one scaled by standardization and one by min-max normalization. Make sure all results are rounded to the nearest 4th decimal.

Example
Example:
        input: data = np.array([[1, 2], [3, 4], [5, 6]])
        output: ([[-1.2247, -1.2247], [0.0, 0.0], [1.2247, 1.2247]], [[0.0, 0.0], [0.5, 0.5], [1.0, 1.0]])
        reasoning: Standardization rescales the feature to have a mean of 0 and a standard deviation of 1. Min-max normalization rescales the feature to a range of [0, 1], where the minimum feature value maps to 0 and the maximum to 1.
```

import numpy as np
def feature_scaling(data: np.ndarray) -> (np.ndarray, np.ndarray):
    # Helper functions
    def min_max_normalize(array: np.ndarray):
        min_val = np.min(array, axis=0)
        max_val = np.max(array, axis=0)
        normalized = (array - min_val) / (max_val - min_val)
        return np.round(normalized, 4)
    
    def standard_normalize(array: np.ndarray):
        mean = np.mean(array, axis=0)
        std_dev = np.std(array, axis=0)
        normalized = (array - mean) / std_dev
        return np.round(normalized, 4)
    
    min_max_scaled_data = min_max_normalize(data)
    standardized_data = standard_normalize(data)
    
    return standardized_data, min_max_scaled_data
