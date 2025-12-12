# 차분 필터 
# 오른쪽 방향 화소와 아래 방향 화소의 차이를 합성해서 필터링하기
import numpy as np
import cv2

img = cv2.imread("dotpy/data/church.jpg", cv2.IMREAD_GRAYSCALE)
x_kernel = np.array([[-1, 1]])
y_kernel = np.array([[-1],[1]])

x_edge = cv2.filter2D(img, -1, x_kernel)
y_edge = cv2.filter2D(img, -1, y_kernel)

cv2.imshow("Origin", img)

# 배열 양 옆으로 붙이기 
cv2.imshow("Diff Filter X Y", np.c_[x_edge, y_edge])
cv2.imshow("Diff Filter", x_edge+y_edge)
cv2.waitKey()
cv2.destroyAllWindows()