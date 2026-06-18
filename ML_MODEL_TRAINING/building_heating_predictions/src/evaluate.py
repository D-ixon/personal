import numpy as np

def evaluate(X, y, theta):
    
    predictions = X.dot(theta)
    
    error = predictions - y

    rmse = np.sqrt(np.mean(error**2))
    
    return rmse, predictions

if __name__ == "__main__":
    print("Evaluate module loaded. Ready to judge performance.")