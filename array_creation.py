import numpy as np
my_array = np.array([10, 9, 8])
#print(my_array)

my_2d_array = np.array([[1, 3, 5, 7],[2, 4, 6, 8]], dtype=np.float32)
print(my_2d_array[1, 1])
print("---------------")
print(my_2d_array[1])
print("---------------")
print(my_2d_array[:, 2])
print("---------------")
print(my_array.shape)
print(my_2d_array.shape)
print("---------------")
print(my_2d_array.dtype)
print("---------------")

ones_array = np.ones((3, 5))
print(ones_array)
print("---------------")

print(np.arange(2, 4))
print("---------------")

print(np.linspace(2, 3, 18))
print("---------------")


print(my_2d_array.reshape(4, 2))
print("---------------")

#addition of arrays 1st method
array_1 = np.array([1, 2, 3, 4])
array_2 = np.array([5, 6, 7, 8])
print(array_1 + array_2)
print("---------------")

#addition of arrays 2nd method
array_out = np.zeros_like(array_1)
for i in range(len(array_1)):
    array_out[i] = array_1[i] + array_2[i]

print(array_out)
print("---------------")

print(np.sin(array_out))
print("---------------")

print(np.dot(array_1, array_2))
print("---------------")

array_a = np.random.rand(4, 3)
array_b = np.random.rand(3, 5)
print(np.dot(array_a, array_b))
print("---------------")

print(my_2d_array.T)
print("---------------")

print(np.arange(7)[3:])
print("---------------")


