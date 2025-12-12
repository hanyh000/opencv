#참고 : https://bkshin.tistory.com/entry/OpenCV-14-%EC%9D%B4%EB%AF%B8%EC%A7%80-%EB%92%A4%ED%8B%80%EA%B8%B0%EC%96%B4%ED%95%80-%EB%B3%80%ED%99%98-%EC%9B%90%EA%B7%BC-%EB%B3%80%ED%99%98

import cv2          # OpenCV 라이브러리 불러오기 (이미지 처리, GUI 등)
import numpy as np  # NumPy 불러오기 (배열, 행렬 연산 등)

win_name = "scanning"               # GUI 창 이름 지정
img = cv2.imread("docu.jpg")        # 이미지 읽기
draw = img.copy()                    # 클릭 좌표 표시용 이미지 복사
pts_cnt = 0                          # 클릭한 좌표 개수 초기화
pts = []                             # 클릭한 좌표를 저장할 리스트 초기화

# -------------------------------
# 클릭한 4점을 top-left, top-right, bottom-right, bottom-left 순으로 정렬
# -------------------------------
def order_points(pts):
    pts = np.array(pts, dtype="float32")                # 리스트를 NumPy 배열로 변환
    pts_sorted = pts[np.argsort(pts[:,1]), :]           # y값 기준 정렬: 위쪽 2개, 아래쪽 2개
    top = pts_sorted[:2]                                # y값 작은 위쪽 2개
    bottom = pts_sorted[2:]                             # y값 큰 아래쪽 2개
    tl, tr = top[np.argsort(top[:,0])]                  # x값 기준: 왼쪽->오른쪽
    bl, br = bottom[np.argsort(bottom[:,0])]            # x값 기준: 왼쪽->오른쪽
    return np.array([tl, tr, br, bl], dtype="float32")  # 정렬된 좌표 반환

# -------------------------------
# 마우스 클릭 이벤트 콜백 함수
# -------------------------------
def onMouse(event, x, y, flags, param):
    global pts_cnt, pts

    if event == cv2.EVENT_LBUTTONDOWN:                   # 좌클릭 이벤트 감지
        cv2.circle(draw, (x,y), 8, (0,255,0), -1)      # 클릭 위치에 녹색 원 그리기
        cv2.imshow(win_name, draw)                     # 클릭 표시 반영

        pts.append([x,y])                              # 클릭 좌표 리스트에 추가
        pts_cnt += 1                                   # 클릭 카운트 증가

        if pts_cnt == 4:                               # 4점 클릭 완료 시
            pts1 = order_points(pts)                  # 좌표 순서 정렬
            tl, tr, br, bl = pts1                     # 각 좌표 변수에 저장

            # -------------------------------
            # 선택 영역 폭과 높이 계산
            # -------------------------------
            widthA = np.linalg.norm(br - bl)          # 아래쪽 좌우 거리
            widthB = np.linalg.norm(tr - tl)          # 위쪽 좌우 거리
            maxWidth = int(max(widthA, widthB))       # 폭 최대값

            heightA = np.linalg.norm(tr - br)         # 오른쪽 상하 거리
            heightB = np.linalg.norm(tl - bl)         # 왼쪽 상하 거리
            maxHeight = int(max(heightA, heightB))    # 높이 최대값

            # -------------------------------
            # 목적 좌표(dst) 정의: 직사각형
            # -------------------------------
            pts2 = np.float32([
                [0,0],                       # top-left
                [maxWidth-1,0],              # top-right
                [maxWidth-1,maxHeight-1],    # bottom-right
                [0,maxHeight-1]              # bottom-left
            ])

            # -------------------------------
            # 원근 변환 행렬 계산 및 적용
            # -------------------------------
            M = cv2.getPerspectiveTransform(pts1, pts2)       # 변환 행렬 계산
            result = cv2.warpPerspective(img, M, (maxWidth, maxHeight))  # 원근 변환 적용

            # -------------------------------
            # 회전 적용: 90도
            # -------------------------------
            center = (maxWidth//2, maxHeight//2)             # 회전 중심: 이미지 중앙
            angle = 90                                       # 회전 각도
            scale = 1                                        # 확대/축소 비율
            rot_mat = cv2.getRotationMatrix2D(center, angle, scale)  # 2D 회전 행렬 계산
            rotated = cv2.warpAffine(result, rot_mat, (maxWidth, maxHeight))  # 회전 적용

            # -------------------------------
            # 결과 출력
            # -------------------------------
            cv2.imshow('scanned', rotated)                  # 변환 + 회전 이미지 표시

# -------------------------------
# 메인 윈도우 생성 및 이벤트 등록
# -------------------------------
cv2.imshow(win_name, draw)                       # 원본 이미지 표시
cv2.setMouseCallback(win_name, onMouse)         # 마우스 이벤트 콜백 등록
cv2.waitKey(0)                                   # 키 입력 대기
cv2.destroyAllWindows()                          # 모든 창 종료
