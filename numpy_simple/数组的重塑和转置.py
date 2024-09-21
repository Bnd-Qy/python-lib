import numpy as np

arr = np.arange(0, 10)
print(arr)

# 重塑:reshape
new_arr = arr.reshape([2, 5])  # 转为两行5列
print(new_arr)

# 转置(类似于反转90度)

arr_2=np.array([['Python', 89], ['Java', 86], ['C++', 67], ['Golang', 94]])
print(arr_2)

arr_3=arr_2.T
print(arr_3)
# T属性与transpose方法都可以进行转置
arr_4=arr_2.transpose()
print(arr_4)