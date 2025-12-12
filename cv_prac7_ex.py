import cv2
import numpy as np
import random

def main():
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("웹캠 열기 실패 ㅠ.ㅠ")
        return

    ret, frame = cap.read()
    if not ret:
        print("첫 프레임 읽기 실패 ㅠ.ㅠ")
        return

    canvas = np.zeros_like(frame)

    prev_center = None

    lower_dark_green = np.array([40, 70, 20])
    upper_dark_green = np.array([80, 255, 120])

    kernel = np.ones((5, 5), np.uint8)

    print("키 입력 가이드 : 펜 지우기는 c, 펜 색상 바꾸기는 p, 종료는 q")

    pen_color = [random.randint(0, 255) for i in range(3)]

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        frame = cv2.flip(frame, 1)

        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        mask = cv2.inRange(hsv, lower_dark_green, upper_dark_green)

        mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel, iterations=1)
        mask = cv2.morphologyEx(mask, cv2.MORPH_DILATE, kernel, iterations=1)

        contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        center = None

        if contours:
            largest = max(contours, key=cv2.contourArea)
            area = cv2.contourArea(largest)

            if area > 500:
                M = cv2.moments(largest)
                if M["m00"] != 0:
                    cx = int(M["m10"] / M["m00"])
                    cy = int(M["m01"] / M["m00"])
                    center = (cx, cy)

                    # cv2.circle(frame, center, 7, (255, 0, 0), -1)

                    if prev_center is not None:
                        cv2.line(canvas, prev_center, center, pen_color, 5)

        prev_center = center

        output = cv2.addWeighted(frame, 0.7, canvas, 0.8, 0)

        cv2.imshow("Output", output)

        key = cv2.waitKey(1) & 0xFF
        if key == ord('q'):
            break
        elif key == ord('c'):
            canvas[:] = 0
            prev_center = None
        elif key == ord('p'):
            pen_color = [random.randint(0, 255) for i in range(3)]

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()