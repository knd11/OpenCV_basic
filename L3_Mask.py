#掩膜操作
import cv2 as cv
import numpy as np

src = cv.imread("./pic/r.png")
cv.imshow("src image",src)


kernel = np.array([[0,-1,0],[-1,5,-1],[0,-1,0]])
dst = cv.filter2D(src,-1,kernel)
cv.namedWindow("filtered image",cv.WINDOW_AUTOSIZE)
cv.imshow("filtered image",dst)
cv.waitKey(0)
