#绘制形状与文字
import cv2 as cv
import numpy as np

src = cv.imread("./pic/psb0.jpg")

#Line
pt1 = (100,100)
pt2 = (300,300)
color = (255,0,255)
srcLine = cv.line(src,pt1,pt2,color,1,cv.LINE_8)
# cv.imshow("Line",src)

#Rectangle
pt3 = (200,100)#2点为对角坐标
pt4 = (300,300)
color = (255,0,0)
LineRect = cv.rectangle(srcLine,pt3,pt4,color,2,cv.LINE_8)
# cv.namedWindow("LineRect",cv.WINDOW_AUTOSIZE)
# cv.imshow("LineRect",LineRect)

#Ellipse
pt5 = (160, 160)
axeSize = (100, 45)
color = (0,255,0)
LineRectElli = cv.ellipse(LineRect,pt5,axeSize,60,0,360,color)
# cv.imshow("LineRectElli",LineRectElli)

#Circle
color = (0,255,0)
LineRectElliCir = cv.circle(LineRectElli,pt5,100,color)
# cv.imshow("LineRectElliCir",LineRectElliCir)

#Polygon
b = np.array([[[100,100], [200,230], [150,200], [100,220]]], dtype = np.int32)
LineRectElliCirPoly = cv.fillPoly(LineRectElliCir,b,255)
# cv.imshow("LineRectElliCirPoly",LineRectElliCirPoly)

#Text
pt6 = (100,100)
LineRectElliCirPolyT =  cv.putText(LineRectElliCirPoly,"Hi CV",pt6,cv.FONT_HERSHEY_COMPLEX,2.0,color,2)
cv.imshow("LineRectElliCirPolyT",LineRectElliCirPolyT)
cv.waitKey(0)