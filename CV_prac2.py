import cv2
import numpy as np

BLUR = 21
CANNY_THRESH_1 = 100
CANNY_THRESH_2 = 100
MASK_DILATE_ITER = 2
MASK_ERODE_ITER = 2

# 1) chroma 이미지 전처리
img = cv2.imread('chroma.jpg')
img = cv2.resize(img, (512,512))

lena = cv2.imread('lena.jpg')
lena = cv2.resize(lena, (512,512))  # <-- 컬러 그대로 사용

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 엣지 검출
edges = cv2.Canny(gray, CANNY_THRESH_1, CANNY_THRESH_2)
edges = cv2.dilate(edges, None)
edges = cv2.erode(edges, None)

# 가장 큰 contour 추출
contours, _ = cv2.findContours(edges, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)
max_contour = max(contours, key=cv2.contourArea)
# 2) 1채널 mask 생성
mask = np.zeros(edges.shape, np.uint8)
cv2.fillConvexPoly(mask, max_contour, 255)

mask = cv2.dilate(mask, None, iterations=MASK_DILATE_ITER)
mask = cv2.erode(mask, None, iterations=MASK_ERODE_ITER)
mask = cv2.GaussianBlur(mask, (BLUR, BLUR), 0)
# 3) 전경(foreground) 이미지 생성
foreground = cv2.copyTo(img, mask)
# 4) 배경은 컬러 레나
background = lena.copy()
# 5) 전경 + 배경 합성
mask_f = mask.astype('float32') / 255.0
mask_f = cv2.merge([mask_f, mask_f, mask_f])  # 3채널로 확장

result = (foreground * mask_f + background * (1 - mask_f)).astype(np.uint8)

cv2.imshow("result", result)
cv2.waitKey(0)
cv2.destroyAllWindows()