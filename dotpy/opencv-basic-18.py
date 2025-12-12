# 다수의 기준점을 이용한 아핀변환 
import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('dotpy/data/lena.jpg')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

rows, cols, ch = img.shape

pts1 = np.float32([[200,100],[400,100],[200,200]]) # 여기에서
pts2 = np.float32([[200,300],[400,200],[200,400]]) # 여기로 이동

# 원래 위치를 원으로 표시
cv2.circle(img, (200,100), 10, (255,0,0),-1)
cv2.circle(img, (400,100), 10, (0,255,0),-1)
cv2.circle(img, (200,200), 10, (0,0,255),-1)

# 아핀변환을 이용해서 각 점을 이동시켜 왜곡!
M = cv2.getAffineTransform(pts1, pts2)
dst = cv2.warpAffine(img, M, (cols,rows))

# 여기부터 : 원본과 왜곡결과물을 함께 표시해보세요! 
plt.subplot(121)
plt.imshow(img) 
plt.title("origin")
plt.axis("off")
plt.subplot(122)
plt.imshow(dst) 
plt.title("affine")
plt.axis("off")
plt.show()