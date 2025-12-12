# 로버츠 필터 : 대각선 방향의 화소 차이로 엣지 검출
import numpy as np
import cv2

img = cv2.imread("dotpy/data/church.jpg", cv2.IMREAD_GRAYSCALE)
x_kernel = np.array([[1,0],[0, -1]])
y_kernel = np.array([[0,1],[-1,0]])

x_edge = cv2.filter2D(img, -1, x_kernel)
y_edge = cv2.filter2D(img, -1, y_kernel)

cv2.imshow("Origin", img)
cv2.imshow("Roverts Filter X Y", np.c_[x_edge, y_edge])
cv2.imshow("Roverts Filter", x_edge+y_edge)
cv2.waitKey()
cv2.destroyAllWindows()