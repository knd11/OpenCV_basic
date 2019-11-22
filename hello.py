import cv2 as cv;

src = cv.imread("./pic/r.png")

cv.imread("input image",cv.WINDOW_AUTOSIZE)
cv.imshow("input image",src)
cv.waitKey(0)
print("hello world")