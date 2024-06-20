import numpy as np
import timeit

a = np.random.rand(1000)

def f1():
    b = np.empty(len(a))
    for i in range(len(a)):
        b[i] = 1 / a[i]
    return b

def f2():
    b = 1 / a
    return b

print(timeit.timeit(stmt = f1, number = 1000))
print(timeit.timeit(stmt = f2, number = 1000))
