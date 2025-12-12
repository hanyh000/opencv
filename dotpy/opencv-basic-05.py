# 직선 및 사각형 그리기 
import cv2
import numpy as np 

img = np.zeros(shape=(512,512,3), dtype=np.uint8) + 255

# 직선 그리기 
cv2.line(img, (0, 0), (500, 0), (166, 97, 243), 5)

# 사각형 그리기 (왼쪽위 + 오른쪽아래)
cv2.rectangle(img, (100, 100), (400, 400), (166, 97, 243), 5)

cv2.imshow('img', img)
cv2.waitKey()
cv2.destroyAllWindows()