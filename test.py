import cv2
import numpy as np

cv2.namedWindow("img")

img = cv2.imread("lena.jpg")

def mouse_callback(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        print("왼쪽 버튼 클릭:", x, y)
        
cv2.setMouseCallback('img', mouse_callback)

cv2.imshow('img', img)
cv2.waitKey(0)
cv2.destroyAllWindows()