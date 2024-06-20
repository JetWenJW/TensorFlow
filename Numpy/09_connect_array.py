import numpy as np

a = np.arange(5)
b = np.arange(10, 15)
print(a)
print(b)

#connect a & b
print(np.concatenate([a, b]))

c = np.arange(20, 25)
print(np.concatenate([a, b, c]))
print("-" * 40)

a1 = np.array([
    [1, 2, 3],
    [7, 8, 9]
])
print("-" * 40)
a2 = np.array([
    [10, 20, 30],
    [70, 80, 90]
])
print(a1)
print(a2)
print("-" * 40)

#array stack(vertical & Horizontal)
print(np.concatenate([a1, a2]))
print(np.concatenate([a1, a2], axis = 1))
print("-" * 40)

#vstack &hstack
print(np.vstack([a1, a2]))
print(np.hstack([a1, a2]))