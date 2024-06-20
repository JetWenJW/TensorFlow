import numpy as np

a = np.arange(8)
print(a)
print(np.split(a, [3]))
print(np.split(a, [3, 6]))

print("-" * 40)
b = np.arange(16).reshape(4, 4)
print(b)
upper, lower = np.vsplit(b, [2])
print(upper)
print()
print(lower)

left, right = np.hsplit(b, [2])
print(left)
print(right)

























