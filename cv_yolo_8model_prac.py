"""
#사진
from ultralytics import YOLO
import matplotlib.pyplot as plt
import cv2

model = YOLO("yolov8n.pt") # 사용할 모델 다운로드하여 인스턴스 생성 
image = cv2.imread("office.jpg")

# 이미지 추론
results = model(image, conf=0.3) # conf로 점수 낮은것 출력 X

for result in results : 
    print(result.boxes) # 감지한 박스 정보 출력 
    boxes = result.boxes
    for box in boxes :
        c = box.cls[0] # 클래스 번호 
        conf = box.conf[0] # 점수
        x1, y1, x2, y2 = box.xyxy[0] # 박스의 좌표  
        
        # 클래스 이름 알아내기 (names 딕셔너리 활용)
        class_name = model.names[int(c)]
        
        print(f"물체: {class_name}, 확신도: {conf:.2f}")
        print(f"좌표: ({x1:.1f}, {y1:.1f}) ~ ({x2:.1f}, {y2:.1f})")
        print("-" * 30)

# 시각화 된 이미지 보기
annotated_frame = results[0].plot()
plt.imshow(cv2.cvtColor(annotated_frame, cv2.COLOR_BGR2RGB))
plt.show()
"""
""""""
#영상
from ultralytics import YOLO
import matplotlib.pyplot as plt
import cv2
import numpy as np

cap = cv2.VideoCapture(0)

model = YOLO("yolov8n.pt") # 사용할 모델 다운로드하여 인스턴스 생성 
# 이미지 추론
if cap.isOpened() :
    while True:
        delay = int(cap.get(cv2.CAP_PROP_FPS))
        
        ret, img = cap.read()

        results = model(img, conf=0.3) # conf로 점수 낮은것 출력 X

        for result in results : 
            print(result.boxes) # 감지한 박스 정보 출력 
            boxes = result.boxes
            for box in boxes :
                c = box.cls[0] # 클래스 번호 
                conf = box.conf[0] # 점수
                x1, y1, x2, y2 = box.xyxy[0] # 박스의 좌표  
                
                # 클래스 이름 알아내기 (names 딕셔너리 활용)
                class_name = model.names[int(c)]

                print(f"물체: {class_name}, 확신도: {conf:.2f}")
                print(f"좌표: ({x1:.1f}, {y1:.1f}) ~ ({x2:.1f}, {y2:.1f})")
                print("-" * 30) 

                font = cv2.FONT_HERSHEY_PLAIN
                cv2.rectangle(img, (int(x1), int(y1)), (int(x2), int(y2)), (0, 0, 0), 2)
                cv2.putText(img, class_name, (int(x1), int(y1 + 30)), font, 3, (0, 0, 0), 3)
                if class_name == 'cell phone':
                    cv2.putText(img, "warnning", (25, 220), font, 8, (0, 0, 255), 3)

        cv2.imshow("stream", img)
        key = cv2.waitKey(delay)
        if key == 27:
            # if you push the ESC key, 
            break

cv2.destroyAllWindows()