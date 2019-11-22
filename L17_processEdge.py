import cv2 as cv
import numpy as np 


src = cv.imread("./pic/gyz.jpg")
# cv.imshow("src",src)

k = 0.05
top = (int)(k*np.shape(src)[0])
bottom = (int)(k*np.shape(src)[0])
left = (int)(k*np.shape(src)[1])
right = (int)(k*np.shape(src)[1])

#填充效果，展示边缘处理
dst1 = cv.copyMakeBorder(src,top,bottom,left,right,cv.BORDER_DEFAULT)
cv.imshow("BORDER_DEFAULT",dst1)

dst2 = cv.copyMakeBorder(src,top,bottom,left,right,cv.BORDER_CONSTANT)
cv.imshow("BORDER_CONSTANT",dst2)

dst3 = cv.copyMakeBorder(src,top,bottom,left,right,cv.BORDER_WRAP)
cv.imshow("BORDER_WRAP",dst3)

dst4 = cv.copyMakeBorder(src,top,bottom,left,right,cv.BORDER_REPLICATE)
cv.imshow("BORDER_REPLICATE",dst4)

dst = cv.GaussianBlur(src,(3,3),0,0,cv.BORDER_CONSTANT)
cv.imshow("blur",dst)
cv.waitKey(0)