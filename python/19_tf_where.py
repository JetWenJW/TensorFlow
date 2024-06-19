import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
os.system("clear")

import tensorflow as tf
import numpy as np

def log(prefix = "", val = ""):
    print(prefix, val, "\n")

a = tf.random.uniform((1, 10), minval = 0, maxval = 10, dtype = tf.int32)
b = tf.random.uniform((1, 10), minval = 0, maxval = 10, dtype = tf.int32)
log("a: ", a)
log("b: ", b)

# a compare with b
log("a == b", a == b)
log(a[a == b])
log(tf.where(a == b))






