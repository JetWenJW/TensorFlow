import numpy as np

X = np.array([1, 2, 3, 5, 8, 13, 21])
print(np.sum(X))
print(np.max(X))
print(np.argmax(X))     # index

print(X < 10)
print(np.any(X < 10))   #只要存在 < 10的數就返回True
print(np.all(X < 10))   #所有數都要 < 10才返回True





