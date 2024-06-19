import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
os.system("clear")

import tensorflow as tf
import numpy as np


def log(prefix = "",val = ""):
    print(prefix, val, "\n")

a = tf.fill([1, 2], value = 2.)
log("a: ", a)
b = tf.norm(a)  #a的范數
log("a的2范數b: ", b)

#計算驗證
a = tf.square(a)
log("a的平方: ", a)

a = tf.reduce_sum(a)
log("a的平方和: ", a)

b = tf.sqrt(a)
log("a的平方合開根號: ", b)



