import matplotlib.pyplot as plt
import pandas as pd

# 通过figure设置画布  figsize:画布大小 百像素  facecolor画布颜色
# pl.figure(figsize=(8, 5), facecolor='pink')
# pl.plot([1, 2, 3, 4, 5], [1, 2, 3, 4, 5])
# pl.show()

###########################
# 设置坐标轴标题 xlabel ylabel

exc = pd.read_excel('../resource/未来15天天天气报.xlsx')
print(exc)
date_ = exc['日期']
wend = exc['温度']
plt.figure(figsize=(10, 7))
# 解决中文乱码
# plt.rcParams['font.sans-serif'] = ['SimHei']
# plt.xlabel('日期')
# plt.ylabel('温度')

# 设置刻度 第一个为精度列表  第二个参数为每个精度对应的label，可传可不传，例如 ['19度','20度'...]
plt.yticks(range(0, 33))

# 设置坐标轴的范围xlim  ylim

# 设置网格线  axis:隐藏网格线的轴
# plt.grid(color='lightgray', linestyle='--', linewidth=0.5, axis='y')

# 设置图表的标题
# plt.title('未来15天天气预报', fontsize=30, color='lightblue')

# 设置图例
# plt.legend(['摄氏度'],fontsize='small')

plt.plot(date_, wend, marker='o', color='r', markerfacecolor='white')

plt.show()
