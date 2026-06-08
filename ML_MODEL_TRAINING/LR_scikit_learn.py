import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# 1. Generate Data
np.random.seed(42)
X = 2 * np.random.rand(100, 1)
y = 4 + 3 * X + np.random.randn(100, 1)

# 2. Fit the model
lin_reg = LinearRegression()
lin_reg.fit(X, y)

# 3. Predict for plotting (creating a line from 0 to 2)
X_new = np.array([[0], [2]])
y_predict = lin_reg.predict(X_new)

# 4. PLOTTING: This is the visual feedback you were missing
plt.plot(X_new, y_predict, "r-", linewidth=2, label="Predictions")
plt.plot(X, y, "b.")
plt.axis([0, 2, 0, 15])
plt.xlabel("$x_1$", fontsize=18)
plt.ylabel("$y$", rotation=0, fontsize=18)
plt.legend(loc="upper left", fontsize=14)
plt.show()