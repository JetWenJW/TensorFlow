import numpy as np

my_array = [1, 2, 3, 8, 5, 13]
np_array = np.array(my_array)
print(np_array)
print(np_array.dtype)

#change Dimension vis Numpy
new_array = [1, 2, 3, 8, 5, 13]
np1_array = np.array(new_array).reshape(2, 3)
print(np1_array)
print(np1_array.dtype)

#Create all 0 Array
np_0_array = np.zeros((5))
print(np_0_array)
print("-" * 40)
np_0_array = np.zeros((4, 6))
print(np_0_array)

print("-" * 40)

#Create all 1 Array
np_1_array = np.ones((5))
print(np_1_array)
print("-" * 40)
np_1_array = np.ones((4, 6))
print(np_1_array)

print("-" * 40)

#Assign elemrnt Value of Array
nparray = np.full((3, 5), 3.14)
print(nparray)
print("-" * 40)

#Order array
nparray = np.arange(10)
print(nparray)
print("#" * 40)

nparray = np.arange(5, 10)
print(nparray)
print("#" * 40)

nparray = np.arange(1, 10, 2)
print(nparray)
print("#" * 40)

nparray = np.arange(0, 10, 2)
print(nparray)
print("#" * 40)


nparray = np.linspace(0, 24, 5)
print(nparray)



