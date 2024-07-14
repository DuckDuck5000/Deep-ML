```
Write a Python function that simulates a single neuron with sigmoid activation, and implements backpropagation to update the neuron's weights and bias. The function should take a list of feature vectors, associated true binary labels, initial weights, initial bias, a learning rate, and the number of epochs. The function should update the weights and bias using gradient descent based on the MSE loss, and return the updated weights, bias, and a list of MSE values for each epoch, each rounded to four decimal places.

Example
Example:
        input: features = [[1.0, 2.0], [2.0, 1.0], [-1.0, -2.0]], labels = [1, 0, 0], initial_weights = [0.1, -0.2], initial_bias = 0.0, learning_rate = 0.1, epochs = 2
        output: updated_weights = [0.0808, -0.1916], updated_bias = -0.0214, mse_values = [0.2386, 0.2348]
        reasoning: The neuron receives feature vectors and computes predictions using the sigmoid activation. Based on the predictions and true labels, the gradients of MSE loss with respect to weights and bias are computed and used to update the model parameters across epochs.
```          


import numpy as np

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def train_neuron(features: np.ndarray, labels: np.ndarray, initial_weights: np.ndarray, initial_bias: float, learning_rate: float, epochs: int) -> (np.ndarray, float, list[float]):
    weights = np.array(initial_weights)
    bias = initial_bias
    mse_values = []

    for epoch in range(epochs):
        total_error = 0
        weight_gradients = np.zeros_like(weights)
        bias_gradient = 0

        for x, y in zip(features, labels):
            linear_output = np.dot(x, weights) + bias
            prediction = sigmoid(linear_output)

            error = prediction - y
            total_error += error ** 2

            d_prediction = error * prediction * (1 - prediction) 
            weight_gradients += d_prediction * x
            bias_gradient += d_prediction

        weights -= learning_rate * weight_gradients / len(labels)
        bias -= learning_rate * bias_gradient / len(labels)

        mse = total_error / len(labels)
        mse_values.append(round(mse, 4))

    updated_weights = np.round(weights, 4)
    updated_bias = round(bias, 4)
    return updated_weights, updated_bias, mse_values
