# 원본과 비교 
import cv2
from matplotlib import pyplot as plt

img = cv2.imread('dotpy/data/lena.jpg')
rows, cols, ch = img.shape

M = cv2.getRotationMatrix2D( (rows/2,cols/2), -30, 1.2)
dst = cv2.warpAffine(img, M, (cols,rows))

# 1행 2열 1번째 = 121
plt.subplot(121)
plt.imshow(img) 
plt.title("origin")

# 1행 2열 2번째 = 122
plt.subplot(122)
plt.imshow(dst) 
plt.title("affine")

plt.show()