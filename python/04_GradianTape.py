import tensorflow as tf
x = tf.constant(10.)

with tf.GradientTape() as tape:
    tape.watch([x])
    y = x**2

dy_dx = tape.gradient(y, x)
print(dy_dx)

