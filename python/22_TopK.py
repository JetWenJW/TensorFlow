import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
os.system("clear")

import tensorflow as tf
import numpy as np

def log(prefix = "", val = ""):
    print(prefix, val, "\n")

a = tf.random.uniform([3, 5], maxval = 10, minval = 0, dtype = tf.int32)
log("a: ", a)

#取array前3位
b = tf.math.top_k(a, k = 3, sorted = True)
#取數值(前3位)
log("b: ", b.values)
#取index(前3位)
log("b: ", b.indices)







