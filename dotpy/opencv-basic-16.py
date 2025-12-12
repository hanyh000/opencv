# Affine 변환
# 변환행렬을 구해서 이미지에 적용하는 방식! 
import cv2
src = cv2.imread('dotpy/data/lena.jpg')

rows, cols, channels = src.shape

# 원하는대로 변형하기 위해서 필요한 변환행렬 구하기 
# 중심점, 회전각도, 확대축소비
M1 = cv2.getRotationMatrix2D( (rows/2, cols/2),  45, 0.5 )
M2 = cv2.getRotationMatrix2D( (rows/2, cols/2), -45, 1.0 )

# 변환행렬을 실제 이미지에 적용하기 
# 원본소스, 변환행렬, 원본크기
dst1 = cv2.warpAffine( src, M1, (rows, cols))
dst2 = cv2.warpAffine( src, M2, (rows, cols))

cv2.imshow('dst1',  dst1)
cv2.imshow('dst2',  dst2)
cv2.waitKey()    
cv2.destroyAllWindows()
