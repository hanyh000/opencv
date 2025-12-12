"""
import cv2
img = cv2.imread('dotpy/data/lena.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 찾고 싶은 부분 (눈) 잘라내기 (템플릿 준비)
template = gray[150:290, 200:400] 

# 매칭 수행
res = cv2.matchTemplate(gray, template, cv2.TM_CCOEFF_NORMED)
min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)

# max_loc이 매칭된 위치의 좌상단 좌표
top_left = max_loc

# 이후 자유롭게 후처리 가능!
print(top_left)

cv2.circle(gray,top_left,5,(0,0,0),-1)

cv2.imshow("gray", gray)
cv2.imshow("dilation", template)
cv2.waitKey()
cv2.destroyAllWindows()
"""
"""
import cv2

img = cv2.imread('p.jpg')

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# 분류기 로드
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# 검출 (입력 이미지는 그레이스케일 권장)
# scaleFactor: 이미지 피라미드 스케일 (보통 1.1)
# minNeighbors: 검출된 영역이 얼마나 중복되어야 얼굴로 인정할지 (보통 3~5)
faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=4)

for (x, y, w, h) in faces:

    template = gray[y:y+h, x:x+w]
    res = cv2.matchTemplate(gray, template, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
    top_left = max_loc

    cv2.rectangle(img, top_left, (x+w, y+h), (255, 0, 0), 2)

    text = "matching"
    cv2.putText(img, text, top_left, cv2.FONT_HERSHEY_SIMPLEX, 1, (120, 60, 180), 2)

    cv2.imshow("tem", template)

cv2.imshow("gray", gray)
cv2.imshow("dilation", img)
cv2.waitKey()
cv2.destroyAllWindows()
"""
"""
import cv2
import sys

fourcc = cv2.VideoWriter_fourcc(*"DIVX")
output = cv2.VideoWriter("output.avi",fourcc, 30.0,(640,480))

cap = cv2.VideoCapture(0) # 0번 카메라 (기본 웹캠)

if not cap.isOpened():
    print("Camera open failed!")
    sys.exit(-1)

while True:
    ret, frame = cap.read() # 한 프레임 읽기
    if ret:
        output.write(frame)
        cv2.imshow('Camera', frame)

        if cv2.waitKey(1) == 27 or cv2.waitKey(1) == 113 : # ESC 키
            break
    
cap.release()
output.release()
cv2.destroyAllWindows()
"""
"""
import cv2

cap = cv2.VideoCapture(0)
# prev_frame 최초로 얻은 프레임을 백업
ret, prev_frame = cap.read()

if not ret:
    print("웹캠에서 영상을 가져올 수 없습니다.")
    cap.release()
    exit()

# 첫 프레임을 그레이스케일로 변환
prev_gray = cv2.cvtColor(prev_frame, cv2.COLOR_BGR2GRAY)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # 이번 프레임을 그레이스케일로 변환
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # 두 프레임 간 차이 계산
    diff = cv2.absdiff(prev_gray, gray)

    # 차이를 보기 좋게 이진화(Threshold)
    _, diff_thresh = cv2.threshold(diff, 30, 255, cv2.THRESH_BINARY)

    # 화면에 표시
    cv2.imshow("Current Frame", frame)
    cv2.imshow("Frame Difference", diff)
    cv2.imshow("Threshold Movement", diff_thresh)

    # 이번 프레임을 다음 반복문의 prev_frame으로 사용
    prev_gray = gray.copy()
    
    if cv2.waitKey(10) == 27: # ESC 키
        break

cap.release()
cv2.destroyAllWindows()
"""
"""
import cv2
import numpy as np

cap = cv2.VideoCapture(0) # 0번 카메라 (기본 웹캠)

if not cap.isOpened():
    print("Camera open failed!")
    exit()

while True:
    ret, frame = cap.read() # 한 프레임 읽기
    if not ret: break

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    hsv2 = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    hsv3 = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    lower_red = np.array([70, 70, 10])
    upper_red = np.array([255, 130, 255])

    lower_blue = np.array([10, 70, 70])
    upper_blue = np.array([255, 130, 130])

    lower_green = np.array([70, 10, 70])
    upper_green = np.array([130, 255, 130])

    mask = cv2.inRange(hsv, lower_red, upper_red)
    mask2 = cv2.inRange(hsv2, lower_blue, upper_blue)
    mask3 = cv2.inRange(hsv3, lower_green, upper_green)

    cv2.imshow('Red Mask', mask)
    cv2.imshow('blue Mask', mask2)
    cv2.imshow('green Mask', mask3)
    
    if cv2.waitKey(10) == 27: # ESC 키
        break

cap.release()
cv2.destroyAllWindows()
"""