#图像的对比度和亮度的增强
import cv2 as cv
import numpy as np

def Contrast_Brightness_Enhance(alpha, beta, img):
    blank = 255*np.ones(img.shape,img.dtype)#也可以用zeros
    # dst = alpha * img + beta * blank
    dst = cv.addWeighted(img,alpha,blank,1-alpha,beta)
    return dst


alpha = 0.8
beta = 30
src = cv.imread("./pic/r.png")
EnPic = Contrast_Brightness_Enhance(alpha, beta, src)

cv.imshow("src pic",src)
cv.imshow("enhanced pic",EnPic)
cv.waitKey(0)