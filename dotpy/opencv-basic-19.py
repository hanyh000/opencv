# 이진화 : 흑과 백으로 나누기
# 흑백 영상 : 회색조 영상 (0~255) vs 이진 영상 (0, 255)
import cv2
import matplotlib.pyplot as plt
img = cv2.imread("dotpy/data/lena.jpg", cv2.IMREAD_GRAYSCALE)

# 임계값을 이용한 이진화 처리
# 대상이미지, 임계값, 임계값이상일때목표 
thresh_value = 127

# 임계값보다 크면 최대치, 작으면 0
ret, thresh1 = cv2.threshold(img, thresh_value, 255, cv2.THRESH_BINARY)
# 임계값보다 크면 0, 작으면 최대치 
ret, thresh2 = cv2.threshold(img, thresh_value, 255, cv2.THRESH_BINARY_INV)
# 임계값보다 크면 임계값, 작으면 원래대로 
ret, thresh3 = cv2.threshold(img, thresh_value, 255, cv2.THRESH_TRUNC)
# 임계값보다 크면 원래대로, 작으면 0
ret, thresh4 = cv2.threshold(img, thresh_value, 255, cv2.THRESH_TOZERO)
# 임계값보다 크면 0, 작으면 원래대로 
ret, thresh5 = cv2.threshold(img, thresh_value, 255, cv2.THRESH_TOZERO_INV)

titles = ['ORIGIN','BINARY','BINARY_INV','TRUNC','TOZERO','TOZERO_INV']
images = [img,thresh1,thresh2,thresh3,thresh4,thresh5]

for i in range(6):
    plt.subplot(2, 3, i + 1)
    plt.imshow(images[i], cmap="gray")
    plt.title(titles[i])
    plt.axis("off")
    
plt.show()