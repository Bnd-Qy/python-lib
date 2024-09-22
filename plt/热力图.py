import matplotlib.pyplot as plt
import pandas as pd

plt.rcParams['font.sans-serif'] = ['SimHei']

score = pd.read_excel('../resource/成绩表.xlsx')

name = score['姓名']

x = score.loc[:, '数学':'英语'].values

plt.xticks(range(3), ['数学', '语文', '英语'])

plt.yticks(range(10), name)

# 显示热力图  数据为矩阵[[xxx,xxx],[xxx,xxx]]
plt.imshow(x)

# 显示颜色条
plt.colorbar()

plt.show()
