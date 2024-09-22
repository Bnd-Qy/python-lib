import matplotlib.pyplot as plt
import pandas as pd

datas = pd.read_excel('../resource/JD手机销售数据.xlsx')

beijing = datas['北京出库销量']
shanghai = datas['上海出库销量']
names = datas['商品名称']
plt.rcParams['font.sans-serif'] = ['SimHei']

plt.figure(figsize=(10, 10))
# 数据 labels:对应的标签  autopct:数据占比格式  startangle:从多少度开始绘图(逆时针)
# labels=names,
# plt.pie(beijing, autopct='%1.1f%%', startangle=90)


############################
# 分裂饼图 通过explode设置需要分裂那一块

# plt.pie(beijing,autopct='%1.1f%%',shadow=True,startangle=90,explode=[
#     0.1,0,0,0,0,0.1,0,0,0,0
# ])
# plt.title('北京4月份手机出库数量',fontsize=20,color='skyblue')
# plt.legend(names)
# plt.show()


############################


# 环形饼图  ,pctdistance:设置数据占比显示的位置  radius设置半径大小
plt.pie(
    beijing, autopct='%1.1f%%', textprops={'fontsize': 12},
    startangle=90, wedgeprops={'edgecolor': 'white', 'width': 0.4}, radius=1, pctdistance=0.85
)
plt.pie(
    shanghai, autopct='%1.1f%%', textprops={'fontsize': 12},
    startangle=90, wedgeprops={'edgecolor': 'white', 'width': 0.4}, radius=0.7, pctdistance=0.85
)
plt.legend(names)
plt.title('2024秋季北京上海手机出库占比')
plt.show()
