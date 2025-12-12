# 수축과 팽창 : 모폴로지 연산 
import cv2
import numpy as np

img = cv2.imread("dotpy/data/morphology.jpg", cv2.IMREAD_GRAYSCALE)
kernel = np.ones((5,5),np.uint8)
erosion = cv2.erode(img,kernel,iterations = 1)
dilation = cv2.dilate(img,kernel,iterations = 1)

cv2.imshow("erosion", erosion)
cv2.imshow("dilation", dilation)
cv2.waitKey()
cv2.destroyAllWindows()