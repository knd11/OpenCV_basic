import cv2 as cv
import numpy as np

# def Threshold_Demo():
#     cv.threshold(src,threshold_value,threshold_max,cv.THRESH_BINARY,src)
#     cv.imshow("binnery image",src)


src = cv.imread("./pic/lancat.jpg",cv.IMREAD_GRAYSCALE)
cv.imshow("input_window",src)

threshold_value = 120
threshold_max = 255
ThType1 = cv.THRESH_BINARY
ThType2 = cv.THRESH_BINARY_INV
ThType3 = cv.THRESH_MASK
ThType4 = cv.THRESH_OTSU
ThType5 = cv.THRESH_TOZERO
ThType6 = cv.THRESH_TOZERO_INV
ThType7 = cv.THRESH_TRIANGLE
ThType8 = cv.THRESH_TRUNC

b1,b2,b3,b4,b5,b6,b7,b8 = src,src,src,src,src,src,src,src
cv.namedWindow("binnery image1",cv.WINDOW_AUTOSIZE)
cv.threshold(src,threshold_value,threshold_max,ThType2,b2)
cv.imshow("binnery image1",b2)


# cv.createTrackbar("Threshold value:","binnery image",threshold_value,threshold_max,Threshold_Demo)

cv.waitKey(0)

