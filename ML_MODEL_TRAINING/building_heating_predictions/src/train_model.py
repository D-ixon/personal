import numpy as np

def train_model(X, y, alpha, iterations):
    m, n = X.shape
    theta = np.zeros(n)
    loss_history = []
    
    for i in range(iterations):
        predictions = X.dot(theta)
        error = predictions - y
        loss = np.sqrt(np.mean(error**2))
        
        if np.isnan(loss):
            print("Alert: Loss diverged!")
            break
            
        loss_history.append(loss)
        gradient = (1 / m) * X.T.dot(error)
        theta -= alpha * gradient
        
    return theta, loss_history

print("\n DEBUG: train_model.py was loaded successfully ")