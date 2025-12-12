# 엣지 검출 == 커널을 이용한 특성 검출
import cv2
import numpy as np
img = cv2.imread("dotpy/data/church.jpg", cv2.IMREAD_GRAYSCALE)

# 커널값은 원하는대로 해도 됨!
kernel = np.array([[0,0,0],[0,1,-1],[0,0,-1]])

# 합성곱 수행 함수 
# 대상이미지, 출력영상의타입(-1 : 타입변화없음), 커널, 경계선처리방식
output = cv2.filter2D(img, -1, kernel, borderType=cv2.BORDER_REFLECT)

cv2.imshow("House", img)
cv2.imshow("filter2D", output)
cv2.waitKey()
cv2.destroyAllWindows()