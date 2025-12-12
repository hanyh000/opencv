import cv2
import numpy as np

img = cv2.imread('linetest.jpg')
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

edges = cv2.Canny(gray, 130, 390)
lines = cv2.HoughLinesP(edges, 0.85, np.pi/10000, 75, minLineLength=80, maxLineGap=11)
dst = cv2.cvtColor(edges, cv2.COLOR_GRAY2BGR) # 컬러로 변환해 그리기

if lines is not None:
    for line in lines:
        x1, y1, x2, y2 = line[0]
        cv2.line(dst, (x1, y1), (x2, y2), (0, 0, 255), 2)

cv2.imshow('img', img)
cv2.imshow('edges', edges)
cv2.imshow('Canny Edge', dst)
cv2.waitKey(0)
cv2.destroyAllWindows()