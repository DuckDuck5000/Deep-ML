```
Matrix times Vector (easy)
Write a Python function that takes the dot product of a matrix and a vector. return -1 if the matrix could not be dotted with the vector

Example
Example:
        input: a = [[1,2],[2,4]], b = [1,2]
        output:[5, 10] 
        reasoning: 1*1 + 2*2 = 5;
                   1*2+ 2*4 = 10
```
def matrix_dot_vector(a:list[list[int|float]],b:list[int|float])-> list[int|float]:

  if len(a[0]) != len(b): return -1

  output = [0]*len(a)
  
  for i in range(0, len(a)):
    for j in range(0, len(b)):
      output[i] += a[i][j]*b[j]
  return output
