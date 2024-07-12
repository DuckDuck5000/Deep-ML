```
Write a Python function that reshapes a given matrix into a specified shape.

Example
Example:
        input: a = [[1,2,3,4],[5,6,7,8]], new_shape = (4, 2)
        output: [[1, 2], [3, 4], [5, 6], [7, 8]]
        reasoning: The given matrix is reshaped from 2x4 to 4x2.


```

def reshape_matrix(a: list[list[int|float]], new_shape: tuple[int, int]) -> list[list[int|float]]:

    flat_matrix = [item for row in a for item in row]
    
    reshaped_matrix = [
        flat_matrix[i * new_shape[1]:(i + 1) * new_shape[1]] 
        for i in range(new_shape[0])
    ]
    
    return reshaped_matrix
