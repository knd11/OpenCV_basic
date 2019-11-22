#图像操作--反色
import cv2 as cv
import numpy as np

#RGB pic
src = cv.imread("./pic/lena.jpg")
cv.namedWindow("input image",cv.WINDOW_AUTOSIZE)
cv.imshow("input image",src)

#gray pic inverse
#gray pic
output_image = cv.cvtColor(src,cv.COLOR_RGB2GRAY)
cv.namedWindow("gray image",cv.WINDOW_AUTOSIZE)
cv.imshow("gray image",output_image)

height = output_image.shape[0]
weight = output_image.shape[1]
print("weight : %s, height : %s" %(weight, height))
for row in range(height):
    for col in range(weight):
        gray = output_image[row,col]
        output_image[row,col] = 255 - gray
cv.namedWindow("inverse image",cv.WINDOW_AUTOSIZE)
cv.imshow("inverse image",output_image)
cv.waitKey(0)

# #RGB pic inverse
# height = src.shape[0]
# weight = src.shape[1]
# channels = src.shape[2]
# print("weight : %s, height : %s, channel : %s" %(weight, height,channels))

# for row in range(height):
#     for col in range(weight):
#         for chan in range(channels):
#             gray = src[row,col,chan]
#             src[row,col,chan] = 255 - gray

# cv.namedWindow("inverse image",cv.WINDOW_AUTOSIZE)
# cv.imshow("inverse image",src)
# cv.waitKey(0)