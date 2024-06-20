from numpy.random import *
import matplotlib.pyplot as plt

print(randn())
print(randn(5))
print(randn(5, 5))

R = randn(10000)
plt.hist(R, bins = 100)
plt.show()











