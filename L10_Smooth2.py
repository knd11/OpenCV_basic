import cv2 as cv

#src pic
src = cv.imread("./pic/lena_noise.bmp")
src1 = cv.imread("./pic/psb0.jpg")
cv.imshow("src",src)
cv.imshow("src1",src1)

kernelsize = 3

#中值滤波去除椒盐噪声
Median = cv.medianBlur(src,kernelsize)
cv.imshow("Median",Median)

#双边滤波(人像处理)
BilaterFilt = cv.bilateralFilter(src1,15,150,5)
cv.imshow("BilaterFilt",BilaterFilt)
cv.waitKey(0)