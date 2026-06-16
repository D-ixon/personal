import numpy as np

# training data with our inputs x and outputs y
X = np.array([1, 2, 3])
y = np.array([3, 5, 7])

# this is our initial guesses for as parameters, theta 0 is the intercept or the bias term.
theta0 = 0
theta1 = 0

learning_rate = 0.1
epochs = 100

m = len(X)

for epoch in range(epochs):

    # this is called, forward pass
    y_pred = theta0 + theta1 * X

    # Error
    error = y_pred - y

    # Gradients
    d_theta0 = (1/m) * np.sum(error)

    d_theta1 = (1/m) * np.sum(error * X)

    # Update
    theta0 -= learning_rate * d_theta0
    theta1 -= learning_rate * d_theta1

print(theta0, theta1)