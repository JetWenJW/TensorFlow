import numpy as np

a1 = np.array([10, 20, 30, 40, 50])
print(a1)
print(a1.sum())
print(a1.min())
print(a1.max())

a2 = np.arange(5)
print(a2)
print("/" * 40)

a3 = a1 + a2
print(a3)
print("/" * 40)

a4 = a1 - a2
print(a4)
print(a4 < 30)
print("/" * 40)

a5 = a1 * a2
print(a5)
print("/" * 40)

#Multi-domension array Compute
b = np.arange(12).reshape(3, 4)
print(b)
print(b.shape)

print("/" * 40)
print(b.sum(axis = 0)) #Vertical coloum
print(b.sum(axis = 1)) #Horizontal Row

print("/" * 40)
print(b.max(axis = 0)) #Vertical coloum
print(b.max(axis = 1)) #Horizontal Row

print("/" * 40)
print(b.min(axis = 0)) #Vertical coloum
print(b.min(axis = 1)) #Horizontal Row

print("*" * 40)

#Array and Array Multiplier
X = np.array([
    [1, 1, 0],
    [0, 1, 1]
])

W = np.array([
    [2, 0],
    [3, 4],
    [1, 2]
])

Y = np.dot(X, W)
print(Y)





