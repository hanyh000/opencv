# 넘파이 배열로써의 정지영상 
import cv2
import numpy as np

img = cv2.imread('dotpy/data/lena.jpg') 

print('img.ndim=', img.ndim) # 3
print('img.shape=', img.shape) # (512, 512, 3)
print('img.dtype=', img.dtype) # 8비트 정수 uint8

# 타입 바꾸기 
img = img.astype(np.int32)
print('img.dtype=',img.dtype)

# 타입 되돌리기
img= np.uint8(img)
print('img.dtype=',img.dtype)

# 1차원으로 펼치기 
img = img.flatten()
print('img.shape=', img.shape)

# 이미지로 되돌리기 
img = img.reshape(512, 512, 3)

cv2.imshow("img_blue", img[:, :, 0])
cv2.imshow("img_green", img[:, :, 1])
cv2.imshow("img_red", img[:, :, 2])
cv2.waitKey()
cv2.destroyAllWindows()