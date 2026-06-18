import numpy as np
from load_data import train_df, test_df
from preprocess import preprocess_data
from train_model import train_model as train_model 

X_train, X_test, y_train = preprocess_data(train_df, test_df)

m_test = X_test.shape[0]
X_test_biased = np.c_[np.ones(m_test), X_test]

m = X_train.shape[0]
X_train_biased = np.c_[np.ones(m), X_train]

alpha = 0.01 
iterations = 1000
theta, loss_history = train_model(X_train_biased, y_train, alpha, iterations)

print("Training complete!")
print("Final Weights (Theta):", theta)
