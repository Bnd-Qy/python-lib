# 数组的乘积与点积

import numpy as np

arr = np.asarray([[1, 2, 3], [4, 5, 6]])

arr2 = np.asarray([[1, 2, 3]])

arr3=np.asarray([1,2,3])

print(arr * arr2)
# 乘积是arr1每行的数据和arr2的每行的数据相乘
'''
[[ 1  4  9]
 [ 4 10 18]]
'''


'''
点积在数学中，又称数量积（dot product; scalar product），是指接受在实数R上的两个向量并返回一个实数值标量的二元运算。它是欧几里得空间的标准内积
两个向量a = [a1, a2,…, an]和b = [b1, b2,…, bn]的点积定义为：
a·b=a1b1+a2b2+……+anbn
'''
# 点积相当于求完和后对每行数据进行求和
# print(np.dot(arr, arr3))

# 矩阵的乘法实际就是在求点积


##############################
m1=np.mat('1 2;3 4;5 6')
m2=np.mat('1;2')
print(m1*m2)  # 点积运算
'''
[[ 5]
 [11]
 [17]]
'''
# 乘积运算

m3=np.mat('1 2')
temp_m=np.multiply(m1,m3)
print(temp_m)
'''
[[ 1  4]
 [ 3  8]
 [ 5 12]]
'''