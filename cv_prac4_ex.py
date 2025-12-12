import cv2
import numpy as np

img = cv2.imread('rail.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
blur = cv2.GaussianBlur(gray, (5, 5), 0)
edges = cv2.Canny(blur, 200, 230)
rows, cols = edges.shape
edges = edges[rows//2:, :]

lines = cv2.HoughLinesP(edges, 1, np.pi/180, 50, minLineLength=200, maxLineGap=100)
print(lines.shape)

if lines is not None:
    for line in lines:
        x1, y1, x2, y2 = line[0]
        cv2.line(img, (x1, y1 + rows//2), (x2, y2 + rows//2), (0, 0, 255), 2)

cv2.imshow('line_img', img)
cv2.waitKey(0)
cv2.destroyAllWindows()