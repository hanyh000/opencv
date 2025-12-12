# 정지영상 읽어들여 화면에 표시하기 
import cv2

imageFile = 'dotpy/data/lena.jpg'

# 주어진 경로의 이미지를 배열 형태로 읽어들여 반환하기 
img  = cv2.imread(imageFile)

# 첫 번째 값은 창 제목, 두 번째 값이 보여줄 이미지
cv2.imshow('Lena color', img)

# 사용자의 키 입력 기다리기
cv2.waitKey()

# 모든 창 끄기
cv2.destroyAllWindows()