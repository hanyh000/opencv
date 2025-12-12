# 콘스라스트(대비) 강조 : 정규화를 통한 대비 
import numpy as np
import cv2

img = cv2.imread("dotpy/data/lena.jpg", cv2.IMREAD_GRAYSCALE)

height, width = img.shape

# 값을 비교적 오밀조밀하게 만드는 작업 
for y in range(height) :
    for x in range(width) :
        if img[y, x] > 160 :
            img[y, x] = 160

# 정규화를 이용해 값의 분포를 변형하기 
# 대상이미지, 출력이미지, 분포의 범위1, 2, 정규화타입
dst = cv2.normalize(img, None, 0, 255, cv2.NORM_MINMAX)

cv2.imshow("img", img)
cv2.imshow("dst", dst)
cv2.waitKey()
cv2.destroyAllWindows()
