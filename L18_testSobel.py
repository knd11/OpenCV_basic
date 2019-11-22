import cv2 as cv 

src = cv.imread("./pic/gyz.jpg")
# cv.imshow("src",src)

blurSrc = cv.GaussianBlur(src,(3,3),0,0)
cv.imshow("blur",blurSrc)
 
gray = cv.cvtColor(blurSrc,cv.COLOR_BGR2GRAY)
cv.imshow("gray",gray)
#dy dx表示求导的阶数
ksize = 3

xgrad = cv.Sobel(gray,cv.CV_16S,1,0,ksize)
ygrad = cv.Sobel(gray,cv.CV_16S,0,1,ksize)

absX = cv.convertScaleAbs(xgrad)
absY = cv.convertScaleAbs(ygrad)

cv.imshow("xgrad",absX)
cv.imshow("ygrad",absY)

xygrad = cv.addWeighted(absX,0.5,absY,0.5,0)
cv.imshow("xygrad",xygrad)

cv.waitKey(0)