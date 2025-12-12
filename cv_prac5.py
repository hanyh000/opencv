import cv2
import numpy as np

img = cv2.imread("coin.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
blur = cv2.GaussianBlur(gray, (5, 5), 1)
edges = cv2.Canny(blur, 100, 200)

# 작은 노이즈 제거 (커널 크게 하면 원이 사라짐!)
kernel = np.ones((3, 3), np.uint8)
clean = cv2.morphologyEx(edges, cv2.MORPH_CLOSE, kernel)

contours, _ = cv2.findContours(clean, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

results = img.copy()
for cnt in contours:
    area = cv2.contourArea(cnt)
    if area < 200:  # 너무 작은 점 제거
        continue
    
    # 원형 여부 판단
    (x, y), radius = cv2.minEnclosingCircle(cnt)
    circle_area = np.pi * radius**2

    # 실제 면적과 원 면적 비교 → 원에 가깝다면 통과
    if 0.7 < (area / circle_area) < 1.3:
        cv2.circle(results, (int(x), int(y)), int(radius), (0, 255, 0), 2)
text = (f'Found {len(contours)} coins')
org = (440,490)
font = cv2.FONT_HERSHEY_COMPLEX_SMALL
cv2.putText(results,text, org, font, 1, (60,120,180), 2)

size, baseLine = cv2.getTextSize(text, font, 1, 2)

cv2.imshow("result", results)
cv2.waitKey(0)
cv2.destroyAllWindows()