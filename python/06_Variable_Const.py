import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
os.system("clear")

import tensorflow as tf

#define Variable
a = tf.Variable(1)
b = tf.Variable(1.)
c = tf.Variable([1.0])
d = tf.Variable(1., dtype = tf.float32)

print("-" * 40)
print(a)
print(b)
print(c)
print(d)

print(b + c)        #Tensor Data Type
print(b + c[0])     #Tensor Data Type

#define Tensor Constant
x1 = tf.constant(1)
x2 = tf.constant(1.)
x3 = tf.constant([1.])
x4 = tf.constant(1, dtype = tf.float32)

print("-" * 40)
print(x1)
print(x2)
print(x3)
print(x4)

print(x2 + x3[0])