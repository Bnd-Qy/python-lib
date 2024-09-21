import matplotlib.pyplot as plt
import pandas as pd

plt.plot([1, 2, 3, 4, 5], [1, 2, 3, 2, 1],
         marker='o', color='r', markerfacecolor='white')
plt.plot([1, 2, 3, 4, 5], [4, 3, 2, 1, 3],
         marker='o', color='y', markerfacecolor='white')
plt.rcParams['font.sans-serif'] = ['SimHei']
# 设置注释
plt.annotate('最大值', xy=(3, 3), xytext=(3.4, 3), arrowprops=dict(facecolor='yellow', shrink=0.05))
# 设置图例
plt.legend(['华为', '小米'])

# 设置是否显示刻度线
# plt.tick_params(bottom=False, left=False, top=False, right=False)

# 设置画布和边缘的间距
plt.subplots_adjust(left=0.25, bottom=0.25)


# 设置刻度线显示的方向 in:向里  out:向外
plt.rcParams['xtick.direction'] = 'in'
plt.rcParams['ytick.direction'] = 'out'
plt.show()
