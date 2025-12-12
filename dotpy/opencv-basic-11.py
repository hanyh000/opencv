# 마우스로 ROI 영역 지정
import cv2
 
src = cv2.imread('dotpy/data/lena.jpg', cv2.IMREAD_GRAYSCALE)
roi = cv2.selectROI(src)
print('roi =', roi)

# 만약에 ROI를 선택했다면
# ROI 좌표 의미 : (좌상단x, 좌상단y, x거리, y거리)
# (0, 0, 100, 200)
if roi != (0, 0, 0, 0):
    img = src[roi[1]:roi[1]+roi[3],
               roi[0]:roi[0]+roi[2]]

    cv2.imshow('Img', img)
    cv2.waitKey()
    
cv2.destroyAllWindows()
