""""""
#사진
import cv2
import numpy as np 
from ultralytics import YOLO

# 사전 학습된 YOLO 모델 읽어오기 
model = YOLO('C:/Users/202-15/Desktop/fruit.v1i.yolov8/runs/detect/fruit_set/weights/best.pt')

img = cv2.imread('apple.jpg')
# 클래스명 리스트 생성 및 채우기 
results = model(img)

# 결과 이미지 시각화 (OpenCV 창에 표시)
for result in results:
    im_bgr = result.plot() # 탐지된 객체가 표시된 BGR 이미지 반환
    cv2.imshow("YOLO Detection", im_bgr)
    cv2.waitKey(0)

cv2.destroyAllWindows()
