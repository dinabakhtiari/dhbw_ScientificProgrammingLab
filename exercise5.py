import numpy as np

def relu(x):

#   return np.maximum(0, x)
  return np.maximum(0, x)  

#print(relu(10))
print(relu(5))

arr = np.array([1, -2, 3, -4])
print("Array result:", relu(arr))
