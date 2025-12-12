# 직선의 방정식 + 삼각함수 기반의 허프 변환에 의한 검출 
import cv2
import numpy as np

src1 = cv2.imread('dotpy/data/circles.jpg')
gray1 = cv2.cvtColor(src1, cv2.COLOR_BGR2GRAY)

# 대상이미지, 메소드는사실상고정값, dp는 해상도, minDist는 최소거리, 
# param1 은 내부적으로 사용되는 케니 엣지 임계값
# param2 는 검출 민감도 (작을수록 검출이 잘 안 됨)
circles1 = cv2.HoughCircles(gray1, method = cv2.HOUGH_GRADIENT,
            dp=1, minDist=50, param2=15)

circles1 =  np.int32(circles1)
print('circles1.shape=', circles1.shape)
for circle in circles1[0,:]:    
    cx, cy, r  = circle
    cv2.circle(src1, (cx, cy), r, (0,0,255), 5)
cv2.imshow('src1',  src1)

src2 = cv2.imread('dotpy/data/circles2.jpg')
gray2 = cv2.cvtColor(src2,cv2.COLOR_BGR2GRAY)
circles2 = cv2.HoughCircles(gray2, method = cv2.HOUGH_GRADIENT,
          dp=1, minDist=50, param2=15, minRadius=30, maxRadius=100)

circles2 =  np.int32(circles2)
print('circles2.shape=', circles2.shape)
for circle in circles2[0,:]:    
    cx, cy, r  = circle
    cv2.circle(src2, (cx, cy), r, (0,0,255), 2) 
    
cv2.imshow('src2',  src2)



cv2.waitKey()
cv2.destroyAllWindows()