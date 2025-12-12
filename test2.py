import cv2
import numpy as np

src = cv2.imread('lena.jpg')
gray = cv2.cvtColor(src,cv2.COLOR_BGR2GRAY)

__,binary = cv2.threshold(gray,127,255,cv2.THRESH_BINARY)

_and = cv2.bitwise_and(gray,binary)
_or = cv2.bitwise_or(gray,binary)

cv2.imshow('src', src)
cv2.imshow('and', _and)
cv2.imshow('or', _or)
cv2.waitKey()
cv2.destroyAllWindows()