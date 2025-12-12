import cv2
import numpy as np

img = cv2.imread('coin.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(gray, (11, 11), 0)

_, thresh = cv2.threshold(blurred, 220, 255, cv2.THRESH_BINARY_INV)

kernel = np.ones((3, 3), np.uint8)
closing = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel, iterations=2)

contours, _ = cv2.findContours(closing, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

result = img.copy()
cv2.drawContours(result, contours, -1, (0, 255, 0), 3)

text = f"found {len(contours)} coins"
cv2.putText(result, text, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)

cv2.imshow('Coin Counter', result)
cv2.waitKey(0)
cv2.destroyAllWindows()