import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
os.system("clear")

import tensorflow as tf
import numpy as np

def log(prefix = "", val = ""):
    print(prefix, val, "\n")

a = tf.random.uniform([3, 5], maxval = 10, dtype = tf.int32)
log("a: ", a)

#升冪排序(return Value)
b = tf.sort(a, axis = 1, direction = "ASCENDING")
log("b: ", b)

#降冪排列(return Value)
b = tf.sort(a, axis = 1, direction = "DESCENDING")
log("b: ", b)

#升冪排序(return index)
b = tf.argsort(a, axis = 1, direction = "ASCENDING")
log("b: ", b)

#降冪排列(return index)
b = tf.argsort(a, axis = 1, direction = "DESCENDING")
log("b: ", b)





