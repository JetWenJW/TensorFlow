import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
os.system("clear")

import tensorflow as tf
import numpy as np

def log(prefix = "", val = ""):
    print(prefix, val, "\n")

#define a random Array
a = tf.random.uniform((3, 10), minval = 0, maxval = 10, dtype = tf.int32)
log("a: ", a)

#取位置(用在ML中預測某個位置的最大機率)
b = tf.argmax(a, axis = 1)
log("maximun index of an array_a : ", b)

#取位置(用在ML中預測某個位置的最大機率)
b = tf.argmin(a, axis = 1)
log("minimun index of an array_a : ", b)








