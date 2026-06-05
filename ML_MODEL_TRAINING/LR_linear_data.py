import numpy as np
import matplotlib.pyplot as plt


X = 2 * np.random.rand(100, 1)
y = 4 + 3 * X + np.random.randn(100, 1)


plt.scatter(X, y)
plt.xlabel("X")
plt.ylabel("y")
plt.title("Linear Relationship with Noise")
plt.show()