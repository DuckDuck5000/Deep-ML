```
Write a Python function to perform one-hot encoding of nominal values. The function should take in a 1D numpy array x of integer values and an optional integer n_col representing the number of columns for the one-hot encoded array. 
If n_col is not provided, it should be automatically determined from the input array.
```

import numpy as np

def to_categorical(x, n_col=None):
	
	## not using numpy here....
	return [[1 if i == val else 0 for i in range(max(x)+1)] for val in x]

    
	