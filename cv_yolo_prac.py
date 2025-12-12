"""
#사진
import cv2
import numpy as np 

# 사전 학습된 YOLO 모델 읽어오기 
net = cv2.dnn.readNet("yolov3.weights", "yolov3.cfg")

# 클래스명 리스트 생성 및 채우기 
classes = []
with open("sample.names", "r") as f :
    classes = [line.strip() for line in f.readlines()]

# 출력층 따로 구분해서 리스트화
layer_names = net.getLayerNames()
output_layers = [layer_names[i - 1] for i in net.getUnconnectedOutLayers()]

# 객체 표시할 색상 랜덤하게 생성하기
colors = np.random.uniform(0, 255, size=(len(classes), 3))

# 이미지 가져오기 
img = cv2.imread("office.jpg")
height, width, channels = img.shape

# 이제 검출해보자~
# 원본 이미지, 스케일팩터(학습률), 예측용 입력 이미지, 평균치, RB 교환 여부, 이미지 자르기 여부
blob = cv2.dnn.blobFromImage(img, 0.00392, (416, 416), (0, 0, 0), True, False)
net.setInput(blob)
outs = net.forward(output_layers)

# 정보를 화면에 표시
class_ids = []
confidences = []
boxes = []
for out in outs:
    for detection in out:
        scores = detection[5:]
        class_id = np.argmax(scores)
        confidence = scores[class_id] # 최종 점수
        if confidence > 0.5:
            # Object detected
            center_x = int(detection[0] * width)
            center_y = int(detection[1] * height)
            w = int(detection[2] * width)
            h = int(detection[3] * height)
            # 어디가 좌상단인지 좌표
            x = int(center_x - w / 2)
            y = int(center_y - h / 2)
            boxes.append([x, y, w, h])
            confidences.append(float(confidence))
            class_ids.append(class_id)

# 중복되는 내용을 억제하는 함수 
# 0.5 의 의미 : 이 점수보다 낮은 건 제거하는!
# 0.4 의 의미 : 박스 간에 겹치는 비율이 0.4 이상이면 제거하는! 
indexes = cv2.dnn.NMSBoxes(boxes, confidences, 0.5, 0.4)

font = cv2.FONT_HERSHEY_PLAIN
for i in range(len(boxes)):
    if i in indexes:
        x, y, w, h = boxes[i]
        label = str(classes[class_ids[i]])
        color = colors[i]
        cv2.rectangle(img, (x, y), (x + w, y + h), color, 2)
        cv2.putText(img, label, (x, y + 30), font, 3, color, 3)
        
cv2.imshow("img", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
"""
""""""
#영상
import cv2
import numpy as np 

# 사전 학습된 YOLO 모델 읽어오기 
net = cv2.dnn.readNet("yolov3.weights", "yolov3.cfg")

# 클래스명 리스트 생성 및 채우기 
classes = []
with open("sample.names", "r") as f :
    classes = [line.strip() for line in f.readlines()]

camera = cv2.VideoCapture(0)

while True:
    # Grab the webcamera's image.
    ret, image = camera.read()

    # 출력층 따로 구분해서 리스트화
    layer_names = net.getLayerNames()
    output_layers = [layer_names[i - 1] for i in net.getUnconnectedOutLayers()]

    # 객체 표시할 색상 랜덤하게 생성하기
    colors = np.random.uniform(0, 255, size=(len(classes), 3))

    # 이미지 가져오기 
    height, width, channels = image.shape

    # 이제 검출해보자~
    # 원본 이미지, 스케일팩터(학습률), 예측용 입력 이미지, 평균치, RB 교환 여부, 이미지 자르기 여부
    blob = cv2.dnn.blobFromImage(image, 0.00392, (416, 416), (0, 0, 0), True, False)
    net.setInput(blob)
    outs = net.forward(output_layers)

    # 정보를 화면에 표시
    class_ids = []
    confidences = []
    boxes = []
    for out in outs:
        for detection in out:
            scores = detection[5:]
            class_id = np.argmax(scores)
            confidence = scores[class_id] # 최종 점수
            if confidence > 0.5:
                # Object detected
                center_x = int(detection[0] * width)
                center_y = int(detection[1] * height)
                w = int(detection[2] * width)
                h = int(detection[3] * height)
                # 어디가 좌상단인지 좌표
                x = int(center_x - w / 2)
                y = int(center_y - h / 2)
                boxes.append([x, y, w, h])
                confidences.append(float(confidence))
                class_ids.append(class_id)

    # 중복되는 내용을 억제하는 함수 
    # 0.5 의 의미 : 이 점수보다 낮은 건 제거하는!
    # 0.4 의 의미 : 박스 간에 겹치는 비율이 0.4 이상이면 제거하는! 
    indexes = cv2.dnn.NMSBoxes(boxes, confidences, 0.5, 0.4)

    font = cv2.FONT_HERSHEY_PLAIN
    for i in range(len(boxes)):
        if i in indexes:
            x, y, w, h = boxes[i]
            label = str(classes[class_ids[i]])
            color = colors[i]
            cv2.rectangle(image, (x, y), (x + w, y + h), color, 2)
            cv2.putText(image, label, (x, y + 30), font, 3, color, 3)

    cv2.imshow("Webcam Image", image)
    keyboard_input = cv2.waitKey(1)

    # 27 is the ASCII for the esc key on your keyboard.
    if keyboard_input == 27:
        break
            
camera.release()
cv2.destroyAllWindows()