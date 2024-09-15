'''
Write a Python function to calculate the accuracy score of a model's predictions. The function should take in two 1D numpy arrays: y_true, which contains the true labels, 
and y_pred, which contains the predicted labels. It should return the accuracy score as a float.

'''

import numpy as np

def accuracy_score(y_true, y_pred):
	correct = 0
	for act, pred in zip(y_true, y_pred):
		if act == pred: correct += 1
	return correct/len(y_true)