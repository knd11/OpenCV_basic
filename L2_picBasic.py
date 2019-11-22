#图片的读写
import cv2 as cv
import numpy as np

#RGB pic
src = cv.imread("./pic/lena.jpg")
cv.imshow("input image",src)


#gray pic
cv.namedWindow("gray image",cv.WINDOW_AUTOSIZE)
output_image = cv.cvtColor(src,cv.COLOR_RGB2GRAY)
cv.imshow("gray image",output_image)
cv.waitKey(0)

cv.imwrite('gray.jpg',output_image)
