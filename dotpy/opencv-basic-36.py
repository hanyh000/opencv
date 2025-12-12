# 웹캠 화면 실시간 읽기 코드 
import cv2

# 웹캠 또는 동영상 연결 
# 웹캠 전달 시 : 웹캠 id 전달 
# 동영상 전달 시 : 동영상 주소 
cap = cv2.VideoCapture(0)

# 동영상이 잘 읽혔는지 확인 
if cap.isOpened() : 
    delay = int(1000 / cap.get(cv2.CAP_PROP_FPS)) # 한 프레임당 걸리는 시간 계산하기
    while True : 
        # ret : 프레임 반환 여부
        # img : 읽어들인 프레임 (배열)
        ret, img = cap.read()

        if ret : 
            cv2.imshow("img", img)
            key = cv2.waitKey(delay)
            if key == ord('q') :
                break
else :
    print("비디오를 읽어들일 수 없습니다.")

cap.release() # 동영상 연결 해제
cv2.destroyAllWindows()