# 정지영상 생성 및 그림 그리기 
import cv2
import numpy as np

# 도화지 만들기 
img1 = np.full((512, 512, 3), (255, 255, 255), dtype=np.uint8)
img2 = np.ones((512, 512, 3), dtype=np.uint8) * 255
img3 = np.zeros((512, 512, 3), dtype=np.uint8) + 255
img4 = np.zeros((512, 512, 3), dtype=np.uint8) # 검은 도화지 

cv2.imshow('img1', img1)
cv2.imshow('img2', img2)
cv2.imshow('img3', img3)
cv2.imshow('img4', img4)
cv2.waitKey()
cv2.destroyAllWindows()