import numpy as np

def predict(X, theta):
    predictions = X.dot(theta)
    
    return predictions

if __name__ == "__main__":
    print("Predict module loaded. Ready to generate results.")