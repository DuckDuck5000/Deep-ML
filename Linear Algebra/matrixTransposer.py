```
Transpose of a Matrix (easy)
✔
Write a Python function that computes the transpose of a given matrix.

Example
Example:
        input: a = [[1,2,3],[4,5,6]]
        output: [[1,4],[2,5],[3,6]]
        reasoning: The transpose of a matrix is obtained by flipping rows and columns.
```

from collections import defaultdict

def transpose_matrix(a: list[list[int|float]]) -> list[list[int|float]]:
    cols = defaultdict(list)
    
    for i in range(0, len(a)):
      for j in range(0, len(a[0])):
        cols[j].append(a[i][j])
    output = []
    for key in sorted(cols.keys()):
      output.append(cols[key])
    return output
    
