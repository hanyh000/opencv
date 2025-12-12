import cv2

cap = cv2.VideoCapture(0)

ret, prev_frame = cap.read()

if not ret:
    print("웹캠에서 영상을 가져올 수 없습니다.")
    cap.release()
    exit()

ft = cv2.imread('filter.png', cv2.IMREAD_UNCHANGED)
if ft is None:
    print("필터 이미지(filter.png)를 로드할 수 없습니다.")
    cap.release()
    exit()

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
# 첫 프레임을 그레이스케일로 변환
prev_gray = cv2.cvtColor(prev_frame, cv2.COLOR_BGR2GRAY)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # 이번 프레임을 그레이스케일로 변환
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=4)

    for (x, y, w, h) in faces:
        ft_resized = cv2.resize(ft, (w, h), interpolation=cv2.INTER_AREA)

        # 2. 리사이즈된 이미지에서 BGRA 채널 분리
        alpha = ft_resized[:, :, 3]      # 알파 채널 (마스크로 사용)
        src_bgr = ft_resized[:, :, 0:3]  # BGR 채널

        mask_fg = alpha 
        mask_bg = cv2.bitwise_not(mask_fg)
        
        # 4. 합성할 영역(ROI: Region of Interest)을 원본 frame에서 추출
        # roi의 형태는 (h, w, 3)으로 마스크와 크기가 일치합니다.
        roi = frame[y:y+h, x:x+w]

        # 5. 전경 및 배경 추출
        # 5a. 전경 추출: 필터의 BGR 부분에 전경 마스크 적용
        # mask_fg는 1채널이므로 src_bgr (3채널)에 적용 시 브로드캐스팅됩니다.
        src_fg = cv2.bitwise_and(src_bgr, src_bgr, mask=mask_fg)

        # 5b. 배경 추출: ROI 영역에 배경 마스크 적용 (필터가 씌워질 공간을 비움)
        lena_bg = cv2.bitwise_and(roi, roi, mask=mask_bg)
        
        # 6. 최종 합성: 추출된 전경과 배경을 더함
        dst = cv2.add(src_fg, lena_bg)

        # 7. 원본 frame의 ROI 영역을 최종 합성 결과(dst)로 업데이트
        frame[y:y+h, x:x+w] = dst

    diff = cv2.absdiff(prev_gray, gray)

    _, diff_thresh = cv2.threshold(diff, 30, 255, cv2.THRESH_BINARY)

    cv2.imshow("Current Frame", frame)
    cv2.imshow("Frame Difference", diff)
    cv2.imshow("Threshold Movement", diff_thresh)

    prev_gray = gray.copy()
    
    if cv2.waitKey(10) == 27: 
        break

cap.release()
cv2.destroyAllWindows() 