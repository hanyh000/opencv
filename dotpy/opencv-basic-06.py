# 직선 및 사각형의 교차점 찾기 
import cv2
import numpy as np

img = np.zeros(shape=(512,512,3), dtype=np.uint8) + 255
x1, x2 = 100, 400
y1, y2 = 100, 400
cv2.rectangle(img, (x1, y1), (x2, y2), (0, 0, 255))

pt1 = 120, 50
pt2 = 300, 500
cv2.line(img, pt1, pt2, (255,0,0), 2)

imgRect = (x1, y1, x2-x1, y2-y1)
ret, rpt1, rpt2  = cv2.clipLine(imgRect, pt1, pt2) # 교차점 찾기 함수 

if ret :
    print(rpt1, rpt2)

cv2.imshow('img', img)
cv2.waitKey()
cv2.destroyAllWindows()