"""
#사진
import cv2
import numpy as np 
from ultralytics import YOLO

# 사전 학습된 YOLO 모델 읽어오기 
model = YOLO('C:/Users/202-15/Desktop/fruit.v1i.yolov8/runs/detect/my_first_yolo/weights/best.pt')

img = cv2.imread('bottle.jpg')
# 클래스명 리스트 생성 및 채우기 
results = model(img)

# 결과 이미지 시각화 (OpenCV 창에 표시)
for result in results:
    im_bgr = result.plot() # 탐지된 객체가 표시된 BGR 이미지 반환
    cv2.imshow("YOLO Detection", im_bgr)
    cv2.waitKey(0)

cv2.destroyAllWindows()
"""
#영상
import cv2
import numpy as np 
from ultralytics import YOLO

# 사전 학습된 YOLO 모델 읽어오기 
model = YOLO('C:/Users/202-15/Desktop/fruit.v1i.yolov8/runs/detect/my_first_yolo/weights/best.pt')
cap = cv2.VideoCapture(0)


while cap.isOpened():
    delay = int(cap.get(cv2.CAP_PROP_FPS))
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.flip(frame, 1)
# 클래스명 리스트 생성 및 채우기 
    results = model(frame, stream=True, conf=0.7)

    for result in results:
        boxes = result.boxes
        for box in boxes:
            # map: 주어진 콜렉터에 같은 함수를 동일하게 적용
            x1, y1, x2, y2 = map(int, box.xyxy[0])
            conf = box.conf[0]
            cls = int(box.cls[0])
            name = model.names[cls]

            color = (127, 0, 127) # 원하는 색상 아무거나 하세요
            cv2.rectangle(frame, (x1, y1), (x2, y2), color, 2)
            cv2.putText(frame, f"{name} {conf:.2f}", (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)

        height, width, channels = frame.shape

        cv2.imshow('frame', frame)
        if cv2.waitKey(delay) == 27:
            break
cap.release()
cv2.destroyAllWindows()
