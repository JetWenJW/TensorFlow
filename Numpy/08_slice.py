import numpy as np

a = np.arange(12)
print(a)
print(a[:5])
print(a[5:])
print(a[4:7])
print(a[::2])       #index
print(a[1::2])
print(a[::-1])
print(a[::-2])

print("-" * 40)

b = np.arange(24).reshape(4, 6)
print(b)
print(b[:2])
print(b[:2, :3])
print(b[:2, ::2])
print(b[:2, ::-1])
print(b[::-1, ::-1])
print(b[:, 0])
print(b[0, :])
print(b[0, ::-1])




