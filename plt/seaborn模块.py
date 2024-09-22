import seaborn as sns
from matplotlib import pyplot as plt

# seaborn是一个基于matplotlib的高级库，使用起来更加简单

sns.set_style('darkgrid')# 灰色网格式
# sns.set(style="whitegrid") 白色网格线
# sns.set_style('dark') 灰色
# sns.set_style('white') 白色
# sns.set_style('ticks') 四周带刻度线白色背景
x = [1, 2, 3, 4, 5]
y = [82, 75, 81, 72, 64]

sns.barplot(x=x,y=y)

plt.show()