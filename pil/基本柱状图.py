import matplotlib.pyplot as plt
import pandas as pd

produce = pd.read_excel('../resource/产品销售统计.xlsx')
produce_name = produce['产品名称']
counter = produce['总量']
plt.rcParams['font.sans-serif'] = ['SimHei']
# 绘制基本柱状图
plt.bar(produce_name, counter)
plt.grid(axis='y', linestyle='--')
plt.show()
