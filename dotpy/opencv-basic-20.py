# 적응형 임계처리 
import cv2
import numpy as np

src = cv2.imread('dotpy/data/lena.jpg', cv2.IMREAD_GRAYSCALE)

# 대상이미지, 최대치, 임계적용타입, 임계처리타입, 임계적용영역크기, 차감할값
dst1 = cv2.adaptiveThreshold(src, 
                             255, 
                             cv2.ADAPTIVE_THRESH_GAUSSIAN_C, 
                             cv2.THRESH_BINARY,
                             51,
                             7
                             )

dst2 = cv2.adaptiveThreshold(src, 
                             255, 
                             cv2.ADAPTIVE_THRESH_MEAN_C, 
                             cv2.THRESH_BINARY,
                             51,
                             7
                             )

cv2.imshow('src',  src)
cv2.imshow('dst1',  dst1)
cv2.imshow('dst2',  dst2)
cv2.waitKey()    
cv2.destroyAllWindows()