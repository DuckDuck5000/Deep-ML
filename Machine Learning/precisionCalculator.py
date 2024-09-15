'''
Write a Python function `precision` that calculates the precision metric given two numpy arrays: `y_true` and `y_pred`. The `y_true` array contains the true binary labels, and the `y_pred` array contains the predicted binary labels. Precision is defined as the ratio of true positives to the sum of true positives and false positives.
'''


import numpy as np
def precision(y_true, y_pred):
	# Your code here
	fp = 0
	tp = 0
	
	for act, pred in zip(y_true, y_pred):
		if act == pred and pred == 1: tp += 1
		if (act == 0 and pred == 1): fp += 1
	return tp / (tp + fp)