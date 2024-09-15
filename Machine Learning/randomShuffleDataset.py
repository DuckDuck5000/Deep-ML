'''
Write a Python function to perform a random shuffle of the samples in two numpy arrays, X and y, while maintaining the corresponding order between them. The function should have an optional seed parameter for reproducibility.
'''



import numpy as np

def shuffle_data(X, y, seed=None):
    '''
    1. combine arrays
    2. shuffle
    3. split
    '''
    if seed is not None:
        np.random.seed(seed)

    combined = np.c_[X.reshape(len(X), -1), y.reshape(len(y), -1)]
    
    np.random.shuffle(combined)
    
    X_shuffled = combined[:, :X.shape[1]].reshape(X.shape)
    y_shuffled = combined[:, X.shape[1]:].reshape(y.shape)
    
    return X_shuffled, y_shuffled
