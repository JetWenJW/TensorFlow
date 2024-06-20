import numpy as np

a = np.arange(1, 6)
print(a)

b = np.add.reduce(a)
print(b)

c = np.multiply.reduce(a)
print(c)

#累加
b = np.add.accumulate(a)
print(b)

#累乘
c = np.multiply.accumulate(a)
print(c)










