# 소벨 필터 : 중심화소 기준으로 앞뒤 변화량 비교하는 알고리즘
import numpy as np
import cv2

img = cv2.imread("dotpy/data/church.jpg", cv2.IMREAD_GRAYSCALE)

# 1, 0 은 x축 필터
x_edge = cv2.Sobel(img, -1, 1, 0, ksize=3)
# 0, 1 은 y축 필터
y_edge = cv2.Sobel(img, -1, 0, 1, ksize=3)

cv2.imshow("Origin", img)
cv2.imshow("Sobel Filter X Y", np.c_[x_edge, y_edge])
cv2.imshow("Sobel Filter", x_edge+y_edge)
cv2.waitKey()
cv2.destroyAllWindows()