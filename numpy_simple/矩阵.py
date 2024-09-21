import numpy as np

# 创建矩阵
m = np.mat('1 2; 3 4; 5 6')
print(m)
print(type(m))
'''
[[1 2]
 [3 4]
 [5 6]]
<class 'numpy.matrix'>
'''

m2 = np.mat([[11, 12], [13, 14]])
print(m2)
print(type(m2))
'''
[[11 12]
 [13 14]]
<class 'numpy.matrix'>
'''

# 对角矩阵与对角线矩阵
# 对角
m3 = np.mat(np.eye(5, 5, dtype=np.uint8))
print(m3)
'''
[[1 0 0 0 0]
 [0 1 0 0 0]
 [0 0 1 0 0]
 [0 0 0 1 0]
 [0 0 0 0 1]]
'''

# 对角线

nums = [1, 2, 3, 4]
m4=np.mat(np.diag(nums))
print(m4)
'''
[[1 0 0 0]
 [0 2 0 0]
 [0 0 3 0]
 [0 0 0 4]]
'''

# 矩阵的转置和求逆
m5=np.mat('1 2; 3 4; 5 6')
print(m5)
print(m5.T)
print(m5.I)
'''
[[1 2]
 [3 4]
 [5 6]]
 
[[1 3 5]
 [2 4 6]]

[[-1.33333333 -0.33333333  0.66666667]
 [ 1.08333333  0.33333333 -0.41666667]]
'''