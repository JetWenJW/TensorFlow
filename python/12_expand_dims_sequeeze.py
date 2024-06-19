import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
os.system("clear")

import tensorflow as tf
import numpy as np

a = tf.range([24])
print(a)
print(a.shape)
print(a.ndim)

# Expand Dimension
b = tf.expand_dims(a, axis = 0)
print(b)
print(b.shape)
print(b.ndim)

# Sequeeze Dimension
c = tf.squeeze(b, axis = 0)
print(c)
print(c.shape)
print(c.ndim)


















