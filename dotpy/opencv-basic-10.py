# ROI (Region Of Interest) : 관심 영역 추출하기 
import cv2 

img = cv2.imread('dotpy/data/lena.jpg', cv2.IMREAD_GRAYSCALE)
# img[높이, 너비, 채널깊이]
# img[y, x, z]
img[100:400, 200:400] = 0 # 관심영역을 검은색으로!

cv2.imshow('img', img)
cv2.waitKey()
cv2.destroyAllWindows()

img = cv2.imread('dotpy/data/lena.jpg')
img[100:400, 200:400] = [100, 50, 100]
cv2.imshow('img', img)
cv2.waitKey()
cv2.destroyAllWindows()