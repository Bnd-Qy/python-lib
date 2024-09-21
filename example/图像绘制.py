import cv2, numpy

# 生成一个512*512 size的图像
img = numpy.zeros((512, 512, 3), numpy.uint8)

# 画直线  图片对象  起始坐标 结束坐标  颜色(B,R,G) 线条宽度
cv2.line(img, (0, 0), (511, 511), (0, 0, 255), 2)

# 画圆 图片对象 中心点坐标  半径  颜色  线宽

cv2.circle(img, (256, 256), 30, (0, 228, 0), -1)

# 绘制方形 图片对象 起始坐标 结束坐标  颜色  线宽

cv2.rectangle(img, (100, 100), (400, 400), (155, 155, 55),2)


# 写文字 图片大小 内容 起始坐标 字体  文字大小  颜色  线宽
cv2.putText(img,'OpenCV2',(50,450),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),2)
cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
