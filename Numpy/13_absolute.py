import numpy as np

a = np.arange(10) - 5
print(a)

def f1():
    return abs(a)

def f2():
    return np.abs(a)

#Pythton API
print(f1())

#Numpy API
print(f2())
