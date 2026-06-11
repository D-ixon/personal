import pandas as pd
import numpy as np
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.compose import ColumnTransformer

# Setup data (same as previous)
df = pd.read_csv('customer__data.csv')
X = df.drop(columns=['Buy Product (Target)'])
y = df['Buy Product (Target)'].apply(lambda x: 1 if x == 'Yes' else 0).values
preprocessor = ColumnTransformer([('num', StandardScaler(), ['Age', 'Income ($1000s)', 'Previous Purchases']),
                                 ('cat', OneHotEncoder(drop='first'), ['Education Level', 'Marital Status'])])
X_preprocessed = preprocessor.fit_transform(X)
X_b = np.c_[np.ones((X_preprocessed.shape[0], 1)), X_preprocessed]

def sigmoid(z): return 1 / (1 + np.exp(-np.clip(z, -500, 500)))

# Trace Function
def trace_optimization(method_name, iterations=5):
    theta = np.zeros(X_b.shape[1])
    print(f"\n--- {method_name} Trace (First {iterations} iterations) ---")
    print(f"{'Iter':<5} | {'Weight[0]':<10} | {'Weight[1]':<10}")
    
    for i in range(iterations):
        if method_name == "BGD":
            grad = (1/len(y)) * X_b.T.dot(sigmoid(X_b.dot(theta)) - y)
            theta -= 0.5 * grad
        elif method_name == "Newton":
            h = sigmoid(X_b.dot(theta))
            grad = (1/len(y)) * X_b.T.dot(h - y)
            S = np.diag(h * (1 - h))
            H = (1/len(y)) * X_b.T.dot(S).dot(X_b)
            theta -= np.linalg.inv(H + 1e-5 * np.eye(X_b.shape[1])).dot(grad)
            
        print(f"{i+1:<5} | {theta[0]:<10.4f} | {theta[1]:<10.4f}")

trace_optimization("BGD", 5)
trace_optimization("Newton", 5)