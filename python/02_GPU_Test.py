import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
import tensorflow as tf
os.system("clear")
print("GPU List:", tf.config.list_physical_devices())
