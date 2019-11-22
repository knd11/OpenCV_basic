#图像金字塔，上采样(放大zoom in)与下采样(缩小zoom out)
import cv2 as cv
import numpy as np

src = cv.imread("./pic/gyz.jpg",cv.IMREAD_GRAYSCALE)
# dim = np.shape(src)[:2]
# lwrate = dim[0]/dim[1]
# dim = ((int)(dim[0]/3.5),(int)(dim[1]/2.3))
# src = cv.resize(src,dim)
# cv.imwrite("gyz.jpg",src)
# cv.imshow("src",src)

# #上采样
# dim = np.shape(src)[:2]
# UPsampling = cv.pyrUp(src,(dim[0]*2,dim[1]*2))
# cv.imshow("UPsampling",UPsampling)

# #下采样
# DownSampling = cv.pyrDown(src,(dim[0]/2,dim[1]/2))
# cv.imshow("DownSampling",DownSampling)

#高斯金字塔
gray_src = src
sigma = 2
K = 2.2
kernelsize = (5,5)
g1 = cv.GaussianBlur(gray_src,kernelsize,sigma,sigma)
g2 = cv.GaussianBlur(g1,kernelsize,sigma*K,sigma*K)
DoGimg = cv.subtract(g1,g2)
cv.normalize(DoGimg,DoGimg,255,0,cv.NORM_MINMAX)#放大到0：255，放大差异
DoGimg = DoGimg.astype(np.uint8)
cv.imshow("DoGimg",DoGimg)

cv.waitKey(0)