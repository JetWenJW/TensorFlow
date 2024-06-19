import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
os.system("clear")

import tensorflow as tf

#define Variable
a = tf.Variable(1)
b = tf.Variable(10.)

print("-" * 40)
print("a.device: ", a.device, a)    #CPU
print("b.device: ", b.device, b)    #GPU

#define Tensor
x1 = tf.constant(100)
x2 = tf.constant(1000.)

print("-" * 40)
print("x1.device: ", x1.device, x1)     #CPU
print("x2.device: ", x2.device, x2)     #CPU

#CPU + CPU
ax1 = a + x1
print("ax1.device: ", ax1.device, ax1)  #GPU

#CPU + GPU
bx2 = b + x2
print("bx2.device: ", bx2.device, bx2)  #GPU

# Conclusion:
#   1. Only define variable as int Data Type, it runs in CPU
#   2. No matter "+", "-", "*", "/"; It Will Run in GPU