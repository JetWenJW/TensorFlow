import numpy as np

a = np.arange(5)
b = np.empty(5)

np.multiply(a, 10, out = b)
print(a)
print(b)

b = np.zeros(10)
np.add(a, 100, out = b[::2])
print(np.add(a, 100))
print(b)







