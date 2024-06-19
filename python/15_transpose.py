import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
os.system("clear")

import tensorflow as tf
import numpy as np

a = tf.range([12])
a = tf.reshape(a, [4, 3])
print(a)

b = tf.transpose(a)
print(b)


# A Colourful Picture 4x4  
a = tf.random.uniform([4, 4, 3],   minval = 0, maxval = 10, dtype = tf.int32)
print(a)

b = tf.transpose(a, perm = [0, 2, 1])
print(b)

c = tf.transpose(b, perm = [0, 2, 1])
print(c)










