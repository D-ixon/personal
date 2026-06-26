import pandas as pds
import numpy as np

train_ds = pds.read_csv('data/training_dataset.csv')
test_ds = pds.read_csv('data/test_dataset.csv')

X = train_ds.drop(columns=['ID', 'Y1'])
y = train_ds[['Y1']]

X_array = X.to_numpy()
y_array = y.to_numpy()

bias_column = np.ones((X_array.shape[0], 1))
X_with_bias = np.c_[bias_column, X_array]

def normal_equation(X_with_bias, y_array):

    theta_best = np.linalg.pinv(X_with_bias.T@(X_with_bias))@(X_with_bias.T)@(y_array)

    return theta_best

theta_best = normal_equation(X_with_bias, y_array)
print("First 10 weights (theta) from normal equation:")
print(theta_best[:10])

X_test = test_ds.drop(columns=['ID'])
X_test_with_bias = np.c_[np.ones((X_test.shape[0], 1)), X_test.to_numpy()]

predictions = X_test_with_bias @ theta_best

print("Predictions for test dataset (first 10):")
print(predictions[:10])

def evaluate(X_with_bias, y_array, theta_best):
    predictions = X_with_bias @ theta_best
    error = predictions - y_array
    rmse = np.sqrt(np.mean(error**2))
    return rmse

rmse = evaluate(X_with_bias, y_array, theta_best)
print("Root Mean Square Error on training dataset:")
print(rmse)