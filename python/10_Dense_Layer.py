import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
os.system("clear")

import tensorflow as tf

# Dense Layer (Hidden Layer): y = wx + b
rows = 1
net = tf.keras.layers.Dense(1)  # A Neutral Unit per Dense Layer
net.build((rows, 1))            # Each Trainning model has 1 feature
print("net.w: ", net.kernel)    # Numbers of Parameter
print("net.b: ", net.bias)      # Same as Numbers of Dense Layer




