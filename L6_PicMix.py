#图像混合
import cv2 as cv

src1 = cv.imread("./pic/psb.jpg")
src2 = cv.imread("./pic/psb1.jpg")

# resize image
scale_percent = 60       # percent of original size
width = int(src1.shape[1] * scale_percent / 300)
height = int(src1.shape[0] * scale_percent / 300)
dim = (width, height)
resizedImg1 = cv.resize(src1, dim)
resizedImg2 = cv.resize(src2, dim)
# cv.namedWindow("Resize img1",cv.WINDOW_AUTOSIZE)
# cv.imshow("Resize img1",resizedImg1)
# cv.namedWindow("Resize img2",cv.WINDOW_AUTOSIZE)
# cv.imshow("Resize img2",resizedImg2)


# Mix pic
mixPic = cv.addWeighted(resizedImg1,0.3,resizedImg2,0.7,0.3)
cv.namedWindow("Resize img2",cv.WINDOW_AUTOSIZE)
cv.imshow("Resize img2",mixPic)
cv.waitKey(0)
