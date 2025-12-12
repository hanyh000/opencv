#import cv2
#import numpy as np

#src = cv2.imread('lena.jpg')
#gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
#hsv = cv2.cvtColor(src, cv2.COLOR_BGR2HSV)
#dst = cv2.equalizeHist(gray)


# 빨간색 추출 예시 (H: 0~10 or 170~180)
# 빨간색은 Hue 값이 0 근처와 180 근처 양쪽에 걸쳐 있습니다.
#lower_red = np.array([0, 100, 100])
#upper_red = np.array([10, 255, 255])

#mask = cv2.inRange(hsv, lower_red, upper_red)
#kernel = np.ones((3, 3), np.uint8)

# 열림 연산으로 자잘한 노이즈 제거
#result = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)

#cv2.imshow('Source', src)
#cv2.imshow('dst', dst)
#cv2.imshow('Equalized', result)
#cv2.waitKey()
#cv2.destroyAllWindows()

import cv2
import numpy as np
img = cv2.imread("dotpy/data/morphology.jpg", cv2.IMREAD_GRAYSCALE)
kernel = np.ones((5,5),np.uint8)
erosion = cv2.erode(img,kernel,iterations = 1)
dilation = cv2.dilate(img,kernel,iterations = 1)

cv2.imshow("img", img)
cv2.imshow("erosion", erosion)
cv2.imshow("dilation", dilation)
cv2.waitKey()
cv2.destroyAllWindows()