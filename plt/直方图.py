import pandas as pd
import matplotlib.pyplot as plt

# 读取数据

score = pd.read_excel('../resource/成绩表2.xlsx')
print(score)

name = score['姓名']
curr_score = score['考试成绩']
plt.title('2024秋季月考成绩分布图')
plt.rcParams['font.sans-serif'] = ['SimHei']

# 参数1：数据集  参数2：数据分布区间
plt.hist(curr_score, [40, 50, 60, 70, 80, 90, 100],color='skyblue',alpha=0.5)
plt.show()
