# 영상 복사 (== 배열 복사)
import cv2
import numpy as np
 
src = cv2.imread('dotpy/data/lena.jpg', cv2.IMREAD_GRAYSCALE) # (512, 512)
shape = src.shape[0], src.shape[1], 3 # (512, 512, 3)
dst = np.zeros(shape, dtype=np.uint8) # 3차원 검은 화면 

# dst = (512, 512, 3) 인데, 전체가 0으로 채워짐

# 블루 채널에 회색조의 값들을 그대로 대입
dst[:, :, 0] = src  
dst[100:400, 200:300, :] = [255, 255, 255]

cv2.imshow('src', src)
cv2.imshow('dst', dst)
cv2.waitKey()    
cv2.destroyAllWindows()