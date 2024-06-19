import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
os.system("clear")

import tensorflow as tf

rows = 1
out = tf.random.uniform([rows, 10])
print("out: ", out)
print("預測值: ", tf.math.argmax(out, axis = 1), "\n")

y = tf.range(rows)
print("y: ", y, "\n")


y = tf.one_hot(y, depth = 10)
print("y_one_hot: ", y, "\n")

loss = tf.keras.losses.mse(y, out)
print("row loss", loss, "\n")

loss = tf.reduce_mean(loss)
print("Total Loss: ", loss, "\n")

# Conclusion:
#  =>主要是用來調整參數用來減少誤差植
#       1. 先算出MSE誤差值
#       2. 再依此數據去調整參數
#       3. 最後不斷Repeat這兩步驟
#       4. 訓練出預測精準的AI Model













