# matplotlib 에서 opencv 영상 표시하기 
import cv2
import matplotlib.pyplot as plt 

imageFile = 'dotpy/data/lena.jpg'

# cv2 의 imread는 이미지 채널을 BGR 로 읽어들인다
imgBGR = cv2.imread(imageFile)

# 이미지의 색상 채널을 변경하고 싶다!
imgRGB = cv2.cvtColor(imgBGR, cv2.COLOR_BGR2RGB) # RGB 색상으로 변환
imgGRAY = cv2.imread(imageFile, cv2.IMREAD_GRAYSCALE) # 회색조 색상으로 읽기

# 하나의 그림판에 두 개의 그래프를 그리는 함수를 이용해서 이미지 그리기
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6))
ax1.imshow(imgRGB)
ax1.axis("off")
ax2.imshow(imgGRAY, cmap="gray")
ax2.axis("off")
plt.show()