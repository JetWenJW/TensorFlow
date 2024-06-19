import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
os.system("clear")

import tensorflow as tf
import numpy as np


def log(prefix = "", val = ""):
    print(prefix, val, "\n")

a = tf.random.shuffle(tf.range(10))
log("a: ", a)

#升冪排序(return Value)
b = tf.sort(a, direction = "ASCENDING")
log("b: ", b)

#降冪排列(return Value)
b = tf.sort(a, direction = "DESCENDING")
log("b: ", b)

#升冪排序(return index)
b = tf.argsort(a, direction = "ASCENDING")
log("b: ", b)

#降冪排列(return index)
b = tf.argsort(a, direction = "DESCENDING")
log("b: ", b)

#
c = tf.gather(a, b)
log("c: ", c)