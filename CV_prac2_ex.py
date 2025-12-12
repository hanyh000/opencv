import cv2
import numpy as np

# 사이즈가 다르면 연산 시 오류가 발생할 수 있다. 
src = cv2.imread('chroma.jpg')
src = cv2.resize(src, (512, 512))
lena = cv2.imread('lena.jpg')
lena = cv2.resize(lena, (512,512))
# 초록 배경에 해당하는 영역만 따로 누끼따기
green_mask = cv2.inRange(src, (0, 120, 0), (100, 255, 100))
mask_fg = green_mask # 초록색 부분만 하얗게 강조
mask_bg = cv2.bitwise_not(mask_fg) # 초록색 부분 외의 영역을 하얗게 강조 

src_fg = cv2.bitwise_and(src, src, mask=mask_bg) # 초록색 외 부분과 아저씨가 겹치는 부분 AND
lena_bg = cv2.bitwise_and(lena, lena, mask=mask_fg) # 초록색 부분과 레나가 겹치는 부분 AND

result = src_fg + lena_bg

cv2.imshow("src_fg", src_fg)
cv2.imshow("lena_bg", lena_bg)
cv2.imshow("result", result)
cv2.waitKey()
cv2.destroyAllWindows()