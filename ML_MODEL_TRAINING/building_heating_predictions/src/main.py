import numpy as np
from load_data import train_df, test_df
from preprocess import preprocess_data
from train_model import train_model
from evaluate import evaluate
from predict import predict
import pandas as pds


X_train, X_test, y_train, scaler = preprocess_data(train_df, test_df)
X_train_biased = np.c_[np.ones(X_train.shape[0]), X_train]
X_test_biased = np.c_[np.ones(X_test.shape[0]), X_test]

alpha = 0.01
iterations = 10000

theta, loss_history = train_model(X_train_biased, y_train, alpha, iterations)

Y1_predict = predict(X_test_biased, theta)

test_ids = test_df['ID']

results_df = pds.DataFrame({
    'ID': test_ids,
    'Heating_Load': Y1_predict
})

results_df.to_csv('final_predictions.csv', index=False)
print("\n Final predictions saved to final_predictions.csv")

print("\n Training complete!")
print("\n Final Weights (Theta):", theta)

rmse, _ = evaluate(X_train_biased, y_train, theta)
print("\n Training RMSE:", rmse)

test_predictions = predict(X_test_biased, theta)
print("\n Test predictions (first 10):")

print("\n", test_predictions[:10], "\n\n")
