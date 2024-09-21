

import matplotlib.pyplot as plt
import pandas as pd

score = pd.read_excel('../resource/成绩表.xlsx')

plt.rcParams['font.sans-serif'] = ['SimHei']

name = score['姓名']

math = score['数学']
chinese = score['语文']
english = score['英语']

plt.plot(name, math, linestyle='-', color='red', marker='o', markerfacecolor='w', label='数学')
plt.plot(name, english, linestyle='--', color='y', marker='o', markerfacecolor='w', label='英语')
plt.plot(name, chinese, linestyle='-.', color='g', marker='o', markerfacecolor='w', label='语文')

plt.legend(['数学', '英语', '语文'])

plt.ylabel('分数')
plt.title('2024年秋季月考分数汇总', fontsize=20, color='purple')

# 添加网格线
plt.grid(axis='y', linestyle='--')  # 隐藏y轴

# 设置y轴
plt.yticks(range(60, 150, 10))
plt.show()
