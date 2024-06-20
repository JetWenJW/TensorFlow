import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("./president_heights.csv")

heights = np.array(data['height(cm)'])
print(heights)
print(heights.mean())
print(heights.min())
print(heights.max())
print(heights.std())

print(np.percentile(heights, 25))   # 25% 分位數
print(np.median(heights))           # 中位數
print(np.percentile(heights, 75))   # 75% 分位數

plt.hist(heights)
plt.title("Height of US Presidents")
plt.xlabel("height(cm)")
plt.ylabel("number")
plt.show()














