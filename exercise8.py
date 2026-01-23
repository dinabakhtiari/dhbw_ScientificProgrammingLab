from sklearn.datasets import load_iris
import numpy as np

X, y = load_iris(return_X_y=True)

result = np.mean(X, axis=0)

print(result)