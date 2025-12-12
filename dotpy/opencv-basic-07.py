# 원 그리기 
import cv2
import numpy as np
img = np.zeros(shape=(512,512,3), dtype=np.uint8) + 255

# 중심점 구하기 
y = img.shape[0] // 2
x = img.shape[1] // 2

# 중심점과 반지름을 정해서 그리기 
cv2.circle(img, (x, y), 50, (0, 0, 255), 2)

# 두께를 -1로 하면, 채우기가 된다! 
cv2.circle(img, (x, y), 30, (0, 255, 0), -1)

cv2.imshow('img', img)
cv2.waitKey()
cv2.destroyAllWindows()

