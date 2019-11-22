import cv2 as cv
import numpy as np

src = cv.imread("./pic/gyz.jpg",cv.IMREAD_GRAYSCALE)
# cv.imshow("src img",src)

# # Robert算子 X方向
# kernel = (1,0,0,-1)
# RobertX = cv.filter2D(src,-1,kernel,(-1,-1))
# cv.imshow("Robert X ",RobertX )

# # Robert算子 Y方向
# kernel = (0,1,-1,0)
# RobertY = cv.filter2D(src,-1,kernel,(-1,-1))
# cv.imshow("Robert Y ",RobertY )

# #Sobel 算子 X方向
# kernel = (-1,0,1,-2,0,2,-1,0,1)
# SobelX = cv.filter2D(src,-1,kernel,(-1,-1))
# cv.imshow("Sobel X ",SobelX )

# #Sobel 算子 Y方向
# kernel = (-1,-2,-1,0,0,0,1,2,1)
# SobelY = cv.filter2D(src,-1,kernel,(-1,-1))
# cv.imshow("Sobel Y ",SobelY )

# # Laplace算子
# kernel = (0,-1,0,-1,4,-1,0,-1,0)
# Laplace = cv.filter2D(src,-1,kernel,(-1,-1))
# cv.imshow("Laplace ",Laplace )


index = 0
a = 1
while(a == 1)
{
    c = cv.waitKey(500)
    if((char)c ==27)
        break

    ksize = 4 + (index%8)*2 + 1
    kernel = np.ones((ksize,ksize),cv.CV_32F)/(float)(ksize*ksize)
    dst = cv.filter2D(src,-1,kernel,(-1,-1))
    index = index + 1
    cv.namedWindow("Custom blur filter result",cv.WINDOW_AUTOSIZE)
    imshow("Custom blur filter result",dst)
}

cv.waitKey(0)
