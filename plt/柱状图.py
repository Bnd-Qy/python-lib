import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

produce = pd.read_excel('../resource/产品销售统计.xlsx')
produce_name = produce['产品名称']
counter = produce['总量']
plt.rcParams['font.sans-serif'] = ['SimHei']
# 绘制基本柱状图
# plt.bar(produce_name, counter)
# plt.grid(axis='y', linestyle='--')
# plt.show()


# 绘制多柱状图

print(produce)

c1 = produce['1月'] + produce['2月'] + produce['3月']
c2 = produce['4月'] + produce['5月'] + produce['6月']
c3 = produce['7月'] + produce['8月'] + produce['9月']
c4 = produce['10月'] + produce['11月'] + produce['12月']

x = np.asarray([1, 2, 3, 4, 5, 6, 7, 8])

plt.bar(x, c1, width=0.2, alpha=0.5)
plt.bar(x + 0.2 * x, c2, width=0.2, alpha=0.5)
plt.bar(x + 0.4 * x, c3, width=0.2, alpha=0.5)
plt.bar(x + 0.6 * x, c4, width=0.2, alpha=0.5)
plt.show()
