import cv2

lena_gray = cv2.imread("dotpy/data/lena.jpg", cv2.IMREAD_GRAYSCALE)

# 이미지, 주변사이즈, 표준편차 
cv2.imshow("Gaussian1", cv2.GaussianBlur(lena_gray, (5, 5), 10))
cv2.imshow("Gaussian2", cv2.GaussianBlur(lena_gray, (5, 5), 200))
cv2.waitKey()
cv2.destroyAllWindows()