# 이미지 저장하기 
import cv2

imageFile = "dotpy/data/lena.jpg"

img = cv2.imread(imageFile) 

# 첫번째 인자는 저장할 이름, 두번째 인자가 2차원 배열  
cv2.imwrite("dotpy/data/lena2.jpg", img, [cv2.IMWRITE_JPEG_QUALITY, 90])
cv2.imwrite("dotpy/data/lena2.png", img, [cv2.IMWRITE_PNG_COMPRESSION, 9])