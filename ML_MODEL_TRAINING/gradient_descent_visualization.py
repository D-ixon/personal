import numpy as np
import matplotlib.pyplot as plt

# Function
def f(x):
    return x**2

# Derivative
def grad(x):
    return 2*x

# Starting point
x = 8

# Learning rate
alpha = 1 # changed from 0.1 to 1 for faster convergence

# Store history
x_history = [x]

# Gradient descent
for _ in range(20):
    x = x - alpha * grad(x)
    x_history.append(x)

# Plot function
x_vals = np.linspace(-10, 10, 400)
y_vals = f(x_vals)

plt.figure(figsize=(8,5))
plt.plot(x_vals, y_vals, label='f(x) = x²')

# Plot descent path
for x_i in x_history:
    plt.scatter(x_i, f(x_i), s=50)

plt.plot(
    x_history,
    [f(x) for x in x_history],
    '--o',
    label='Gradient Descent Path'
)

plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Gradient Descent on f(x)=x²')
plt.legend()
plt.grid(True)
plt.show()