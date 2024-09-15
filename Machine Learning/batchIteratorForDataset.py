```
Write a Python function to create a batch iterator for the samples in a numpy array X and an optional numpy array y. The function should yield batches of a specified size. If y is provided, the function should yield batches of (X, y) pairs; otherwise, it should yield batches of X only.

```




import numpy as np

def batch_iterator(X, y=None, batch_size=32):
    n_samples = X.shape[0]

    batches = []
    
    for start_idx in range(0, n_samples, batch_size):
        end_idx = min(start_idx + batch_size, n_samples)
        X_batch = X[start_idx:end_idx]
        
        if y is not None:
            y_batch = y[start_idx:end_idx]
            batches.append([X_batch.tolist(), y_batch.tolist()])
        else:
            batches.append(X_batch.tolist())
    
    return batches