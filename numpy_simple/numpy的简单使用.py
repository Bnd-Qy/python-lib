import numpy as np

# 创建一维数组

array1 = np.array([1, 2, 3])
print(array1)

# 创建类型为浮点类型的数组


array2 = np.array([1.1, 1.2, 1.3])
print(array2)

# 设置数组的类型
array3 = np.array([1, 2, 3], dtype=float)
print(array3)  # [1. 2. 3.]

# 查看数组的数据类型
print(array3.dtype)  # float64

# 查看数组的类型
print(type(array3))  # <class 'numpy.ndarray'>

# 创建参数介绍 object:数据对象  dtype:数据类型 copy:对数组修改时是否进行复制一份，从而不影响原数组 ndmin:数组的最小维度


src_arr = [10, 11, 12]

# 测试复制
"""
[100 200  12]
[10, 11, 12]
"""
new_arr = np.array(src_arr, copy=True)

new_arr[0] = 100
new_arr[1] = 200

print(new_arr)
print(src_arr)

three_arr = np.array([1, 2, 3], ndmin=3)  # [[[1 2 3]]]
print(three_arr)

# 测试维度
