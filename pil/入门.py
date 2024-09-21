import matplotlib.pyplot as plt
import pandas as pd

# 绘制简单图表
# plt.plot([1, 2, 3, 4, 5])
# plt.show()

# 绘制散点图  第一个列表为x轴 第二个列表为y轴  第三个参数为控制曲线的关键字

# plt.plot([1, 2, 3, 4, 5], [3, 1, 5, 3, 2],'ro')
# plt.show()


# 读取excel中的数据，并绘制折线图
# exc = pd.read_excel('../resource/未来15天天天气报.xlsx')
# print(exc)
# date_ = exc['日期']
# wend = exc['温度']
# plt.plot(date_, wend)
# plt.show()


# 设置折线的样式  color指定颜色  linestyle指定线样式

plt.plot([1, 2, 3, 4, 5], [3, 1, 5, 3, 2], color='r', linestyle='-.') # 点线
plt.plot([1, 2, 3, 4, 5], [1, 2, 3, 4, 5], color='g', linestyle='--') # 双划线
plt.plot([1, 2, 3, 4, 5], [5, 4, 3, 2, 1], color='b', linestyle=':')  # 虚线
plt.show()


# 设置标记的样式 marker   markerfacecolor:设置marker内部的颜色

exc = pd.read_excel('../resource/未来15天天天气报.xlsx')
print(exc)
date_ = exc['日期']
wend = exc['温度']
plt.plot(date_, wend,marker='o',color='pink',markerfacecolor='white')
plt.show()