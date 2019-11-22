# 开操作:先膨胀后腐蚀，可以去除较小对象(对象为前景，黑色为背景)
# 闭操作:先腐蚀后膨胀，可以填充小洞(对象为前景，黑色为背景)

import cv2 as cv
import numpy as np

#src pic
src = cv.imread("./pic/ED.bmp")
src1 = cv.imread("./pic/lena.jpg")
cv.imshow("src",src)


kernelsize = (21,21)
StructElemt = cv.getStructuringElement(cv.MORPH_RECT,kernelsize)
#开操作，小对象被去掉
Open = cv.morphologyEx(src,cv.MORPH_OPEN,StructElemt)
cv.imshow("Open",Open)

#闭操作，黑孔被填充
Close = cv.morphologyEx(src,cv.MORPH_CLOSE,StructElemt)
cv.imshow("Close",Close)

#形态学梯度，膨胀-腐蚀
Gradient = cv.morphologyEx(src1,cv.MORPH_GRADIENT,(3,3))
cv.imshow("Gradient",Gradient)

#顶帽，原图-开操作
Tophat = cv.morphologyEx(src,cv.MORPH_TOPHAT,StructElemt)
cv.imshow("Top hat",Tophat)


#黑帽,闭操作-原图，查看孔洞
BlackHat = cv.morphologyEx(src,cv.MORPH_BLACKHAT,StructElemt)
cv.imshow("Black Hat",BlackHat)
cv.waitKey(0)