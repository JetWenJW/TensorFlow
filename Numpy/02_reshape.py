import numpy as np


my_array = [1, 2, 3, 8, 5, 13]
np_array = np.array(my_array).reshape(2, 3)
print(np_array)

print("Array Dimension: ", np_array.ndim)
print("Array Dimension(Format as Tuple): ", np_array.shape)
print("Array Numerous of Elements: ", np_array.size)
print("Array Data Type: ", np_array.dtype)
print("Array Size of elements: ", np_array.itemsize)

#Much easier to change Array Dimension via Numpy