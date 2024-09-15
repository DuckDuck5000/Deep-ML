'''
Write a Python function `ridge_loss` that implements the Ridge Regression loss function. The function should take a 2D numpy array `X` representing the feature matrix, a 1D numpy array `w` representing the coefficients, a 1D numpy array `y_true` representing the true labels, and a float `alpha` representing the regularization parameter. 
The function should return the Ridge loss, which combines the Mean Squared Error (MSE) and a regularization term.

'''


import numpy as np

def ridge_loss(X: np.ndarray, w: np.ndarray, y_true: np.ndarray, alpha: float) -> float:
	
	'''
	predict y
	compute mse
	compute l2 reg
	compute total loss
	'''
	y_pred = X @ w
	mse = np.mean((y_true-y_pred)**2)
	l2_reg = alpha*np.sum(w**2)
	return mse + l2_reg
