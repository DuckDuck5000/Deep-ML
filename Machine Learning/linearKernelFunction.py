'''
Write a Python function `kernel_function` that computes the linear kernel between two input vectors `x1` and `x2`. 
The linear kernel is defined as the dot product (inner product) of two vectors.

'''

import numpy as np

def kernel_function(x1, x2):
	# Your code here
	kernel = 0
	for x, y in zip(x1, x2): kernel += x*y
	return kernel
