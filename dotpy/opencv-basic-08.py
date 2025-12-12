# 문자열 출력 
import numpy as np
import cv2

img = np.zeros(shape=(512,512,3), dtype=np.uint8) + 255

# 글자 표시하기 기본
text = "Happy Lunch Time"
origin = (100, 100)
font_family = cv2.FONT_HERSHEY_PLAIN
cv2.putText(img, text, origin, font_family, 2, (0, 0, 0), 1)

# 글의 영역 얻기 
size, baseLine = cv2.getTextSize(text, font_family, 2, 1)

cv2.circle(img, (origin[0], origin[1]), 5, (0, 255, 0), -1)

# 글의 영역 표시하기 
cv2.rectangle(img, origin, (origin[0] + size[0], origin[1] - size[1]), (0,0,0))

cv2.imshow('img', img)
cv2.waitKey()
cv2.destroyAllWindows()