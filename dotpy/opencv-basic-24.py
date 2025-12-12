# 메디안 필터
import numpy as np
import cv2

lena_gray = cv2.imread("dotpy/data/lena.jpg", cv2.IMREAD_GRAYSCALE)
result = cv2.medianBlur(lena_gray, 3)
cv2.imshow("Lena", lena_gray)
cv2.imshow("Median filter", result)
cv2.waitKey()
cv2.destroyAllWindows()