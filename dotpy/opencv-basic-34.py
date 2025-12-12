'''
케니 엣지 : 단계적인 알고리즘
1. 가우시안 필터를 이용한 노이즈 제거 
2. 소벨 필터를 이용한 엣지 검출 
3. 불필요한 픽셀 제거하는 임계 처리 
4. 실제 결과 도출 (두 개의 임계값을 통한)
'''
import cv2

src = cv2.imread('dotpy/data/lena.jpg', cv2.IMREAD_GRAYSCALE)
# 하단 임계값, 상단 임계값 
edges1 = cv2.Canny(src, 50, 100)
edges2 = cv2.Canny(src, 50, 200)
 
cv2.imshow('edges1',  edges1)
cv2.imshow('edges2',  edges2)
cv2.waitKey()
cv2.destroyAllWindows()