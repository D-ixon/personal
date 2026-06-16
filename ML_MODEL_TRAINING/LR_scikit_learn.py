import numpy as np
from sklearn.linear_model import LinearRegression

np.random.seed(42) 
X = 2 * np.random.rand(100, 1)
y = 4 + 3 * X + np.random.randn(100, 1)

# 2. Scikit-Learn implementation
lin_reg = LinearRegression()
lin_reg.fit(X, y)


print("--- MODEL OUTPUT ---")
print(f"Intercept (theta0): {lin_reg.intercept_[0]}")
print(f"Coefficient (theta1): {lin_reg.coef_[0][0]}")


X_new = np.array([[0], [2]])
y_predict = lin_reg.predict(X_new)
print(f"Predictions for x=0 and x=2:\n{y_predict}")