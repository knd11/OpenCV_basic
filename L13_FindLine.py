#找水平和垂直直线

import cv2 as cv
import numpy as np

import pytesseract
from PIL import Image
# src Img
# src = cv.imread("./pic/LineBW.jpg")
src = cv.imread("./pic/verifiedCode1.png")


# gray Img
grayImg = cv.cvtColor(src,cv.COLOR_BGR2GRAY)
cv.imshow("grayImg",grayImg)

# binnery Img
binImg = cv.adaptiveThreshold(grayImg,255,cv.ADAPTIVE_THRESH_GAUSSIAN_C,cv.THRESH_BINARY,15,-2)
cv.imshow("binImg",binImg)

ksize1 = ((int)(np.shape(src)[0]/16),1)
ksize2 = (1,(int)(np.shape(src)[1]/16))
hline = cv.getStructuringElement(cv.MORPH_RECT,ksize1,(-1,-1))
vline = cv.getStructuringElement(cv.MORPH_RECT,ksize2,(-1,-1))

# # 提取水平线
# Erode = cv.erode(binImg,hline)
# ErodeDilate_h = cv.dilate(Erode,hline)#open openeration
# cv.imshow("Find hline",ErodeDilate_h)
# ErodeDilate_h = cv.bitwise_not(ErodeDilate_h)#将背景变为白色
# cv.imshow("Find hline with white background",ErodeDilate_h)

# #提取竖直的线
# ErodeDilate_v = cv.morphologyEx(binImg,cv.MORPH_OPEN,vline)
# ErodeDilate_v = cv.bitwise_not(ErodeDilate_v)
# cv.imshow("Find vline with white background",ErodeDilate_v)

# 识别验证码
kernel = cv.getStructuringElement(cv.MORPH_RECT,(3,3))
ErodeDilate_vercode = cv.morphologyEx(binImg,cv.MORPH_OPEN,kernel)
cv.bitwise_not(ErodeDilate_vercode,ErodeDilate_vercode)

cv.imshow("verified code recognize",ErodeDilate_vercode)


cv.waitKey(0)