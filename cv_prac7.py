import cv2
import numpy as np

cap = cv2.VideoCapture(0)
colors = [(255, 0, 0), (255, 0, 255), (0, 255, 0), (0, 0, 255), (0, 255, 255)]
color = colors[0]

width = int(cap.get(3))
height = int(cap.get(4))

canvas = np.zeros((height, width, 3), np.uint8)

if not cap.isOpened():
    print("Camera open failed!")
    exit()

previous_center_point = (0, 0) #이전 프레임의 추적 좌표를 저장하며, 선을 이어 그리는 데 사용됩니다.
is_drawing = False 

while True:
    ret, frame = cap.read() # 한 프레임 읽기
    frame = cv2.flip(frame,1)

    if not ret: break

    #cv2.rectangle(frame, (20,120), (120,150), (122,122,122), -1)
    #cv2.putText(frame, "CLEAR ALL", (30, 140), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2, cv2.LINE_AA)

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    lower_red = np.array([0, 80, 80])
    upper_red = np.array([10, 255, 255])
    mask = cv2.inRange(hsv, lower_red, upper_red)
    kernel = np.ones((5,5),np.uint8)
    mask = cv2.dilate(mask, kernel, iterations=1) # 마스크의 작은 노이즈를 제거하고 물체 영역을 확장(팽창)하여 추적을 안정화합니다.
    
    # --- 컨투어 감지 및 중심점 계산 ---
    contours, h = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    
    current_center_point = None # 현재 프레임의 중심점
    min_area = 1000

    if len(contours) > 0:
        cmax = max(contours, key = cv2.contourArea)
        area = cv2.contourArea(cmax) #외곽선이 감지되면, 가장 큰 외곽선(cmax)을 선택합니다.
        
        if area > min_area:
            M = cv2.moments(cmax)
            # m00이 0이 아닐 때만 계산
            if M["m00"] > 0:
                cX = int(M["m10"] / M["m00"])
                cY = int(M["m01"] / M["m00"])
                current_center_point = (cX, cY)
                #유효한 물체의 **무게 중심(Moment)**을 계산하여 중심 좌표 (cX, cY)를 구하고 이를 current_center_point에 저장합니다.
                # 프레임에 중심점 표시
               #cv2.circle(frame, current_center_point, 10, (0, 0, 255), 2)
    
    # --- 버튼 클릭 및 그리기 상태 로직 ---
    if current_center_point:
        cX, cY = current_center_point
        """
        if cY < 160 and cY > 110:
            if cX > 20 and cX < 120:
                canvas = np.zeros((height, width, 3), np.uint8) # CLEAR ALL
                """
        is_drawing = True
        if cv2.waitKey(10) == 98:
            color = colors[0]

        if cv2.waitKey(10) == 99:
            canvas = np.zeros((height, width, 3), np.uint8)

        if cv2.waitKey(10) == 112:
            color = colors[1]

        if cv2.waitKey(10) == 103:
            color = colors[2]

        if cv2.waitKey(10) == 114:
            color = colors[3]
        
        if cv2.waitKey(10) == 121:
            color = colors[4]
    else :
        is_drawing = False
    
    # --- 선 그리기 ---
    # is_drawing이 True이고, 이전 점이 (0,0)이 아니며, 현재 점이 감지되었을 때만 선을 긋습니다.
    if is_drawing and previous_center_point != (0, 0) and current_center_point:
        cv2.line(canvas, previous_center_point, current_center_point, color, 2)
        #현재 그리기 상태이고, 이전 점이 유효하며, 현재 점이 감지되었다면, 캔버스에 previous_center_point부터 current_center_point까지 선을 그립니다.
    # --- 중심점 업데이트 ---
    if current_center_point:
        previous_center_point = current_center_point
    else:
        # 물체 감지가 끊기면 다음 프레임에서 선이 이어지지 않도록 (0, 0)으로 설정
        previous_center_point = (0, 0) 
        is_drawing = False

    # --- 캔버스 합치기 ---
    #캔버스 합치기 및 출력
    # 이 부분은 그림이 그려진 캔버스를 웹캠 영상 위에 자연스럽게 합성하여 보여줍니다.그림 영역 마스크 생성: canvas를 회색으로 변환한 뒤 이진화하여, 그림이 그려진 영역만 검은색(0)인 canvas_binary 마스크를 만듭니다.원본 영상 지우기: frame = cv2.bitwise_and(frame, canvas_binary)를 통해 원본 frame에서 그림 영역만큼의 픽셀을 제거 (검은색으로 만듦)합니다. (이 마스크의 흰색 부분만 원본 프레임에서 남깁니다.)그림 합치기: frame = cv2.bitwise_or(frame, canvas)를 통해 제거된 자리에 canvas의 그림을 합성하여 최종 영상을 완성합니다.cv2.imshow('mask', mask) / cv2.imshow('Air Canvas', frame): 추적에 사용된 마스크와 최종 결과 영상을 화면에 표시합니다.if cv2.waitKey(10) == 27: break: ESC 키를 누르면 프로그램을 종료합니다.
    canvas_gray = cv2.cvtColor(canvas, cv2.COLOR_BGR2GRAY)
    _, canvas_binary = cv2.threshold(canvas_gray, 20, 255,cv2.THRESH_BINARY_INV)
    canvas_binary = cv2.cvtColor(canvas_binary, cv2.COLOR_GRAY2BGR)
    frame = cv2.bitwise_and(frame, canvas_binary)
    frame = cv2.bitwise_or(frame, canvas)

    
    cv2.imshow('mask', mask) 
    cv2.imshow('Air Canvas', frame)

    if cv2.waitKey(10) == 27: 
        break

cap.release()
cv2.destroyAllWindows()

"""
import cv2
import numpy as np

cap = cv2.VideoCapture(0) # 0번 카메라 (기본 웹캠)

colors = [(255, 0, 0), (255, 0, 255), (0, 255, 0), (0, 0, 255), (0, 255, 255)]
color = colors[0]
width = int(cap.get(3))
height = int(cap.get(4))
# Create a blank canvas 
canvas = np.zeros((height, width, 3), np.uint8)

if not cap.isOpened():
    print("Camera open failed!")
    exit()

# 이 변수들을 루프 이전에 정의해야 합니다.
previous_center_point = (0, 0)
is_drawing = False 

while True:
    ret, frame = cap.read() # 한 프레임 읽기
    if not ret: break

    # 🎨 버튼 영역 그리기
    cv2.rectangle(frame, (20,1), (120,65), (122,122,122), -1)
    cv2.rectangle(frame, (140,1), (220,65), colors[0], -1) # Blue
    cv2.rectangle(frame, (240,1), (320,65), colors[1], -1) # Violet
    cv2.rectangle(frame, (340,1), (420,65), colors[2], -1) # Green
    cv2.rectangle(frame, (440,1), (520,65), colors[3], -1) # Red (주의: colors[3]은 (0,0,255)로 Red입니다.)
    cv2.rectangle(frame, (540,1), (620,65), colors[4], -1) # Yellow

    # 📝 버튼 텍스트 넣기
    cv2.putText(frame, "CLEAR ALL", (30, 33), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2, cv2.LINE_AA)
    cv2.putText(frame, "BLUE", (155, 33), cv2.FONT_HERSHEY_SIMPLEX, 0.5,(255, 255, 255), 2, cv2.LINE_AA)
    cv2.putText(frame, "VIOLET", (255, 33), cv2.FONT_HERSHEY_SIMPLEX, 0.5,(255,255, 255), 2, cv2.LINE_AA)
    cv2.putText(frame, "GREEN", (355, 33), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2, cv2.LINE_AA)
    cv2.putText(frame, "RED", (465, 33), cv2.FONT_HERSHEY_SIMPLEX, 0.5,(255, 255, 255), 2, cv2.LINE_AA)
    cv2.putText(frame, "YELLOW", (555, 33), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255,255,255), 2, cv2.LINE_AA)

    # 🔴 [NameError: name 'mask' is not defined] 해결 부분: 마스크 생성 로직 복구
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    lower_red = np.array([0, 100, 100])
    upper_red = np.array([10, 255, 255])
    mask = cv2.inRange(hsv, lower_red, upper_red)
    kernel = np.ones((5,5),np.uint8)
    mask = cv2.dilate(mask, kernel, iterations=1)
    
    # --- 컨투어 감지 및 중심점 계산 ---
    contours, h = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    
    current_center_point = None # 현재 프레임의 중심점
    min_area = 1000

    if len(contours) > 0:
        cmax = max(contours, key = cv2.contourArea)
        area = cv2.contourArea(cmax)
        
        if area > min_area:
            M = cv2.moments(cmax)
            # m00이 0이 아닐 때만 계산
            if M["m00"] > 0:
                cX = int(M["m10"] / M["m00"])
                cY = int(M["m01"] / M["m00"])
                current_center_point = (cX, cY)
                
                # 프레임에 중심점 표시
                cv2.circle(frame, current_center_point, 10, (0, 0, 255), 2)
    
    # --- 버튼 클릭 및 그리기 상태 로직 ---
    if current_center_point:
        cX, cY = current_center_point
        
        # 버튼 영역 (Y < 65) 클릭 감지
        if cY < 65:
            is_drawing = False # 버튼 영역 클릭 시 그리기 중지
            
            if cX > 20 and cX < 120:
                canvas = np.zeros((height, width, 3), np.uint8) # CLEAR ALL
            elif cX > 140 and cX < 220:
                color = colors[0] # Blue
            elif cX > 240 and cX < 320:
                color = colors[1] # Violet
            elif cX > 340 and cX < 420:
                color = colors[2] # Green
            elif cX > 440 and cX < 520:
                color = colors[3] # Red
            elif cX > 540 and cX < 620:
                color = colors[4] # Yellow
        else:
            # 버튼 영역 밖 (그리기 영역)
            is_drawing = True

    # --- 선 그리기 ---
    # is_drawing이 True이고, 이전 점이 (0,0)이 아니며, 현재 점이 감지되었을 때만 선을 긋습니다.
    if is_drawing and previous_center_point != (0, 0) and current_center_point:
        cv2.line(canvas, previous_center_point, current_center_point, color, 2)
        
    # --- 중심점 업데이트 ---
    if current_center_point:
        previous_center_point = current_center_point
    else:
        # 물체 감지가 끊기면 다음 프레임에서 선이 이어지지 않도록 (0, 0)으로 설정
        previous_center_point = (0, 0) 
        is_drawing = False

    # ❌ 이전 답변에서 불필요하게 추가된 중복 로직 (NameError 방지) 제거
    # previous_center_point= (cX, cY) 이 코드는 위의 if/else 블록에서 처리되므로 제거했습니다.

    # --- 캔버스 합치기 ---
    canvas_gray = cv2.cvtColor(canvas, cv2.COLOR_BGR2GRAY)
    _, canvas_binary = cv2.threshold(canvas_gray, 20, 255,cv2.THRESH_BINARY_INV)
    canvas_binary = cv2.cvtColor(canvas_binary, cv2.COLOR_GRAY2BGR)
    frame = cv2.bitwise_and(frame, canvas_binary)
    frame = cv2.bitwise_or(frame, canvas)
    
    cv2.imshow('Air Canvas', frame) # 창 표시
    
    if cv2.waitKey(10) == 27: # ESC 키
        break

cap.release()
cv2.destroyAllWindows()
"""