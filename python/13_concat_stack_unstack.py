import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
os.system("clear")

import tensorflow as tf
import numpy as np

a = tf.zeros([2, 4, 3])
b = tf.ones([2, 4, 3])
print(a)
print(b)


c = tf.concat([a, b], axis = 0)
print(c)

c = tf.concat([a, b], axis = 1)
print(c)


c = tf.concat([a, b], axis = 2)
print(c)

#Expand One Dimension
c = tf.stack([a, b], axis = 0)
print(c)

m, n = tf.unstack(c, axis = 0) 
print(m)
print(n)


# 所有圖片都可以理解為一個array
# 現在所有對array的操作都是，對未來圖片操作的準備