import numpy as np

a = np.array([1, 2, 3, 5, 8 ,13, 21])
print(a)
print(a[0])
print(a[1])
print(a[-1])
print(a[-2])
print(len(a))
a[0] = 100
print("-" * 40)
print(a)
print(a.dtype)
print(a.itemsize)
print(a.nbytes)

print("#" * 40)
b = np.arange(24).reshape(4, 6)
print(b[0])
print(b[1])
print(len(b))
print(b[0, 0])
print(b[0, 2])
print(b[1, 0])
print(b[1, 2])
print("-" * 40)
b[0, 0] = 100
print(b)
print(b.dtype)
print(b.itemsize)
print(b.nbytes)



