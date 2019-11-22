#膨胀 腐蚀来消除小对象
import cv2 as cv
import numpy as np
#src pic
# src = cv.imread("./pic/lena.jpg")
# cv.imshow("src",src)

src = np.zeros([400,400])
for i in range(10):
    for j in range(20):
        src[i,j] = 255
        src[300-i,300-j] = 255
        src[200-i,200-j] = 255
        src[100-i,100-j] = 255
        src[50-i,50-j] = 255

for i in range(100):
    for j in range(150):
        src[350-i,350-j] = 255

cv.imshow("src",src)
cv.imwrite("ED.bmp",src)
element_size = 15
s = element_size*2 + 1

StructElement = cv.getStructuringElement(cv.MORPH_RECT,(s,s))
Dilate = cv.dilate(src,StructElement)

Erode = cv.erode(src,StructElement)

cv.imshow("Dilate",Dilate)
cv.imshow("Erode",Erode)
cv.waitKey(0)