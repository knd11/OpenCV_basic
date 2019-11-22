import cv2 as cv 

src = cv.imread("./pic/lena.jpg")
cv.imshow("src",src)

blurSrc = cv.GaussianBlur(src,(3,3),0,0)
cv.imshow("blur",blurSrc)
 
gray = cv.cvtColor(blurSrc,cv.COLOR_BGR2GRAY)

edge_img = cv.Laplacian(gray,cv.CV_16S,3)
edge_img = cv.convertScaleAbs(edge_img)
cv.imshow("Laplacian result",edge_img)

# edge_img = cv.threshold(edge_img,0.6,255,cv.THRESH_OTSU|cv.THRESH_BINARY)
# cv.imshow("Laplacian result1",edge_img)
cv.waitKey(0)
