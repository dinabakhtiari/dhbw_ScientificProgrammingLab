import numpy as np
import matplotlib.pyplot as plt

def relu(x):
    return np.maximum(0, x)

def softplus(x):
    return np.log(1 + np.exp(x))

x = np.linspace(-5, 5, 200)


plt.plot(x, relu(x), label="ReLU", linestyle="--", color="red", lw=2)
plt.plot(x, softplus(x), label="Softplus", color="blue", lw=2)

plt.title("Comparison: ReLU vs Softplus")
plt.xlabel("Input (x)")
plt.ylabel("Output (y)")
plt.grid(True, linestyle=':', alpha=0.6)
plt.axhline(0, color='black', linewidth=1)
plt.axvline(0, color='black', linewidth=1)
plt.legend()

plt.show()