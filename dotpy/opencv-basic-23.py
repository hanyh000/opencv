# 블러 필터
import cv2

lena_gray = cv2.imread("dotpy/data/lena.jpg", cv2.IMREAD_GRAYSCALE)
cv2.imshow("Lena", lena_gray)

# (3, 3)은 주변 픽셀 사이즈 
cv2.imshow("Mean Blur", cv2.blur(lena_gray, (9,9)))
cv2.waitKey()
cv2.destroyAllWindows()