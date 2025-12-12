# 라플라시안 필터 : 현재 화소 기준으로 테두리를 더 부각시키는 방식 
import cv2

img = cv2.imread("dotpy/data/church.jpg", cv2.IMREAD_GRAYSCALE)
cv2.imshow("Origin", img)
cv2.imshow("cv2.Laplacian", cv2.Laplacian(img, -1))
cv2.waitKey()
cv2.destroyAllWindows()