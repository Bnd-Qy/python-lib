import numpy as np

# 创建指定维度数据未初始化的数组，需要一个必填参数shape [行，列，高]
arr = np.empty([4, 3])
print(arr)

# 创建指定维度以0填充的数组

arr1 = np.zeros(3)
print(arr1)  # [0. 0. 0.]  默认dtype=float

# 创建指定维度以1填充的数组
arr2 = np.ones(4)
print(arr2)  # [1. 1. 1. 1.]

# 创建指定维度和类型的数组并以指定值进行填充
arr3 = np.full([4, 3], 255, dtype=float)
'''
[[255. 255. 255.]
 [255. 255. 255.]
 [255. 255. 255.]
 [255. 255. 255.]]
'''
print(arr3)

##################################
# 通过数值范围创建数组  和range函数一致
arr_range = np.arange(0, 100, 5)
print(arr_range)

# 生成等差数列  开始值  结束值  生成的数列中包含样本数量  endpoint:包含尾部  retstep:是否返回样本步长
arr_lin_space = np.linspace(0, 100, num=7, dtype=int, endpoint=False, retstep=True)
print(arr_lin_space)

# 生成等比数列

# 生成 10^0 ~ 10^2  包含10个数，默认底数为10  base:指定底数  endpoint:是否包含尾部数字
arr_log_space = np.logspace(0, 2, 10)
print(arr_log_space)

arr_log_space_2 = np.logspace(0, 3, 4, base=2, endpoint=True)
print(arr_log_space_2)  # [1. 2. 4. 8.]

# 生成随机数组 参数为样本数量
arr_rand = np.random.rand(5)  # [0.54151958 0.99098579 0.35358069 0.15013746 0.47883647]
print(arr_rand)

# 随机生成满足正态分布的数组     正态分布:中间高两边低 对称
arr_randn = np.random.randn(5)
print(arr_randn)

# 生成一定范围内的随机数组 size:样本数  low:最小值  high:最大值(不包括)
arr_rand_int=np.random.randint(low=0, high=10, size=5)
print(arr_rand_int)

arr_rand_int2=np.random.randint(low=0, high=10, size=(3,4)) # 生成二维矩阵
print(arr_rand_int2)


# 生成正态分布的随机数组  loc:正态分布的中心值  scale:宽度  size:样本数量

arr_normal=np.random.normal(loc=10,scale=0.5,size=5)   # 可以自定义标准差和中心值
print(arr_normal)


#######################################################
# asarray  # 根据指定的python数据类型创建数组
arr5=np.asarray([[1,2,3],[4,5,6]])
print(arr5)

# 动态数组  S1表示以单个字符作为数据类型
from_buffer=np.frombuffer(b'abcdefg',dtype='S1')
print(from_buffer)


it=(i for i in range(10))
print(it)
# 从迭代对象中创建数组对象
iter_array=np.fromiter(it,dtype=int)
print(iter_array)

# empty_like
'''
[
[0 0 0]
[0 0 0]
 ]
'''
empty_like_array=np.empty_like([[1,2,3],[4,5,6]])
print(empty_like_array)

# zero_like
'''
[[0 0 0]
 [0 0 0]]
'''
zeros_like_array=np.zeros_like([[1,2,3],[4,5,6]])
print(zeros_like_array)

# ones_like
'''
[[1 1 1]
 [1 1 1]]
'''
ones_like_array=np.ones_like([[1,2,3],[4,5,6]])
print(ones_like_array)

# full_like
'''
[
[8 8 8]
[8 8 8]
]
'''
full_like_array=np.full_like([[1,2,3],[4,5,6]],8)
print(full_like_array)