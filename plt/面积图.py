import matplotlib.pyplot as plt
import pandas as pd
import random

x = [i for i in range(1, 6)]

y1 = [random.randint(1, 10) for i in range(5)]
y2 = [random.randint(1, 10) for i in range(5)]
y3 = [random.randint(1, 10) for i in range(5)]
y4 = [random.randint(1, 10) for i in range(5)]

# 绘制面积图
plt.stackplot(x, y1, y2, y3, y4)
plt.show()