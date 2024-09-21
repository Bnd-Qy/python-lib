import numpy as np
import cv2

arr = np.asarray([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
arr1 = np.asarray([[10], [11], [12]])
print(arr)

# 垂直方向增加数据
# new_arr=np.vstack((arr,arr1))
# print(new_arr)

# 水平方向新增数据
new_arr2 = np.hstack((arr, arr1))
print(new_arr2)

# 删除操作

# 删除第2行
# arr=np.delete(arr, 1, axis=0)
# print(arr)

# 删除第二列
#
# arr=np.delete(arr,1,axis=1)
# print(arr)

# 删除第二行和第三行

arr = np.delete(arr, (1, 2), axis=0)
print(arr)

# 数组的修改

img = np.zeros([100, 100, 3], dtype=np.uint8)

img[30:40, 30:60] = (155, 155, 255)

# 数组的查询 where  参数1：条件  参数2 当条件成立时赋值  当条件不成立时赋值
arr=np.arange(0,10)
# 返回的是符合的索引集合
w=np.where(arr>6)
val=arr[w]
print(val) # [7 8 9]


