import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
os.system("clear")

import tensorflow as tf
import numpy as np

a = tf.random.normal([10, 28, 28, 3])
print(a)
print(a.shape)      # Shape
print(a.ndim)       # Dimension

b = tf.reshape(a, [10, 784, 3])  
print(b)
print(b.shape)      # Shape
print(b.ndim)       # Dimension

# "-1" will auto reshape
c = tf.reshape(a, [10, -1, 3])  
print(c)
print(c.shape)      # Shape
print(c.ndim)       # Dimension

d = tf.reshape(a, [10, 784 * 3])  
print(d)
print(d.shape)      # Shape
print(d.ndim)       # Dimension

# "-1" will auto reshape
e = tf.reshape(a, [10, -1])  
print(e)
print(e.shape)      # Shape
print(e.ndim)       # Dimension







