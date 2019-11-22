import cv2 as cv

#src pic
src = cv.imread("./pic/psb0.jpg")
cv.imshow("src",src)

kernel_size = (3,3)
#均值模糊
Blur = cv.blur(src,kernel_size)
cv.imshow("Blur",Blur)
#高斯模糊
GaussianB = cv.GaussianBlur(src,kernel_size,11,11)
cv.imshow("GaussianBlur",GaussianB)
cv.waitKey(0)