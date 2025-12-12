import cv2
from ultralytics import YOLO
import math

model = YOLO('yolov8n.pt')
cap = cv2.VideoCapture(0)

while cap.isOpened():
    delay = int(cap.get(cv2.CAP_PROP_FPS))
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.flip(frame, 1)
    results = model(frame, stream=True, conf=0.7)
    person_detected = False

    for result in results:
        boxes = result.boxes
        for box in boxes:
            # map: 주어진 콜렉터에 같은 함수를 동일하게 적용
            x1, y1, x2, y2 = map(int, box.xyxy[0])
            conf = box.conf[0]
            cls = int(box.cls[0])
            name = model.names[cls]

            if name == "person":
                person_detected = True

            color = (127, 0, 127) # 원하는 색상 아무거나 하세요
            cv2.rectangle(frame, (x1, y1), (x2, y2), color, 2)
            cv2.putText(frame, f"{name} {conf:.2f}", (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)

    height, width, channels = frame.shape
    if person_detected:
        font = cv2.FONT_HERSHEY_PLAIN
        cv2.putText(frame, "WARNING: Person Detected!", (50, height//2), font, 3, (0, 0, 255), 3)

    cv2.imshow('frame', frame)

    if cv2.waitKey(delay) == 27:
        break

cap.release()
cv2.destroyAllWindows()
