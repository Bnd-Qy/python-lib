import matplotlib.pyplot as plt
import pandas as pd

# 将区域拆成两行两列，当前区域占用第一个位置 第一种方式
# plt.subplot(2, 2, 1)
# plt.plot([1, 2, 3, 4, 5], [5, 4, 3, 2, 1])
#
# plt.subplot(2, 2, 2)
# plt.plot([1, 2, 3, 4, 5], [1, 2, 3, 2, 1], color='green')
#
# # 将区域分为两行一列，当前区域为第二行
# plt.subplot(2, 1, 2)
# plt.plot([1, 2, 3, 4, 5], [1, 2, 3, 4, 5], color='r')
#
# plt.show()

###################### 第二种方式subplots
# figure, axes = plt.subplots(2, 2)  # 返回画布对象 和坐标轴对象
#
# # 在第0行0列进行绘图
# axes[0, 0].plot([1, 2, 3, 4, 5], [5, 4, 3, 2, 1])
# # 在第一行第一列的区域进行绘图
# axes[1, 1].scatter([1, 2, 3, 4, 5], [1, 3, 3, 2, 1])
# plt.show()


##################### 第三种方式  add_subplot 声明画布后，在画布的指定区域进行绘图
fig=plt.figure()
ax1=fig.add_subplot(2,2,1)
ax1.plot([1, 2, 3, 4, 5], [5, 4, 3, 2, 1])

ax2=fig.add_subplot(2,2,4)
ax2.plot([1, 2, 3, 4, 5], [3, 1, 2, 2, 1])
plt.show()
