import cv2
import numpy as np 
from matplotlib import pyplot as plt

src = cv2.imread("book.png") 
rows, cols, ch = src.shape

# x, y 순서로 좌표 쓰면 됨 
pts1 = np.float32([
    [100,280],
    [660,100],
    [280,1250], 
    [1150, 870]]) 
pts2 = np.float32([
    [0,0],
    [cols,0],
    [0,rows], 
    [cols, rows]]) 

M = cv2.getPerspectiveTransform(pts1, pts2)
dst = cv2.warpPerspective(src, M, (cols,rows))

dst = cv2.resize(dst, None, fx=0.3, fy=0.3)

cv2.imshow("dst", dst)
cv2.waitKey(0)
cv2.destroyAllWindows()