```
multiply two matrices together (return -1 if shapes of matrix dont aline), i.e. C = A dot product B

Example
 
Example:
        input: A = [[1,2],
                    [2,4]], 
               B = [[2,1],
                    [3,4]]
        output:[[ 8,  9],
                [16, 18]]
        reasoning: 1*2 + 2*3 = 8;
                   2*2 + 3*4 = 16;
                   1*1 + 2*4 = 9;
                   2*1 + 4*4 = 18
                    
Example 2:
        input: A = [[1,2],
                    [2,4]], 
               B = [[2,1],
                    [3,4],
                    [4,5]]
        output: -1
        reasoning: the length of the rows of A does not equal
          the column length of B
```

def matrixmul(a:list[list[int|float]],
              b:list[list[int|float]])-> list[list[int|float]]: 
    if len(a[0]) != len(b):
        return -1
    
    output = [
        [0 for _ in range(len(b[0]))] for _ in range(len(a))
    ]
    
    for i in range(len(a)):
        for j in range(len(b[0])):
            for k in range(len(a[0])):
                output[i][j] += a[i][k] * b[k][j]
                
    return output
