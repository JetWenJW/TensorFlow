import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
os.system("clear")

import tensorflow as tf
import numpy as np

def log(prefix = "", val = ""):
    print(prefix, val, "\n")

a = tf.range(12, dtype = tf.float32)
a = tf.reshape(a, (4, 3))
log("a Array: ", a)

b = tf.reduce_min(a)
log("Minimun of Array: ", b)

b = tf.reduce_max(a)
log("Maxima of Array: ", b)

b = tf.reduce_mean(a)
log("Mean of Array: ", b)


#軸(行)運算(axis = 0)
b = tf.reduce_min(a, axis = 0)
log("Minimun of axis = 0 Array: ", b)

b = tf.reduce_max(a, axis = 0)
log("Maxima of axis = 0 Array: ", b)

b = tf.reduce_mean(a, axis = 0)
log("Mean of axis = 0 Array: ", b)


#軸(行)運算(axis = 1)
b = tf.reduce_min(a, axis = 1)
log("Minimun of axis = 1 Array: ", b)

b = tf.reduce_max(a, axis = 1)
log("Maxima of axis = 1 Array: ", b)

b = tf.reduce_mean(a, axis = 1)
log("Mean of axis = 1 Array: ", b)










