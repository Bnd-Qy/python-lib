import cv2

# img = cv2.imread('../resource/1.jpg')
# cv2.imshow('image',img)
# cv2.waitKey(0)

# 图像的读取 cv2.imread(path,method) 图像加载方式包含彩色、灰度、带有透明度的彩色三种方式  ,读取失败则返回None
# IMREAD_UNCHANGED: int 带有透明度
# IMREAD_GRAYSCALE: int 灰度
# IMREAD_COLOR: int 彩色
img = cv2.imread('../resource/1.jpg', cv2.IMREAD_GRAYSCALE)

# cv2.imshow('img', img)
# cv2.waitKey(0)

# 显示图像 cv2.imshow(窗口名词，要加载的图像)


# 保存图像 cv2.imwrite('文件路径',要保存的图像)
cv2.imwrite('../resource/1-process.jpg', img)