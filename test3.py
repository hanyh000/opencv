# 가우시안 필터 직접 구현
import numpy as np
import cv2

img = cv2.imread('lena.jpg')
img = cv2.resize(img, (512,512)) 
rows, cols, ch = img.shape

pts1 = np.float32([[200,100],[400,100],[200,200]])
pts2 = np.float32([[200,300],[400,200],[200,400]])

# pts1의 좌표에 표시. Affine 변환 후 이동 점 확인.
cv2.circle(img, (200,100), 10, (255,0,0),-1)
cv2.circle(img, (400,100), 10, (0,255,0),-1)
cv2.circle(img, (200,200), 10, (0,0,255),-1)
 
M = cv2.getAffineTransform(pts1, pts2)

dst = cv2.warpAffine(img, M, (cols,rows))

cv2.imshow("Lena", img)
cv2.imshow("dst", dst)
cv2.waitKey()
cv2.destroyAllWindows()
# 1. cv2.filter2D() 함수란? / filter2D는 이미지에 **임의의 커널(=컨볼루션 필터)**을 적용하는 함수로, 블러링·샤프닝·에지 검출 등 다양한 작업을 수행할 수 있게 해줍니다.
# dst = cv2.filter2D(src, ddepth, kernel, anchor=(-1,-1), delta=0, borderType=cv2.BORDER_DEFAULT)

# 2. 커널(kernel)이란? / 커널은 픽셀 주변 영역을 어떠한 방식으로 조합해 새로운 픽셀 값을 만들지 결정하는 작은 행렬입니다. 예) 3×3, 5×5, 7×7 등(대부분 홀수 크기) / 이미지의 각 픽셀에 대해 커널을 슬라이드하며 컨볼루션(convolution) 연산을 수행합니다.

# 3. 커널 적용 원리 (컨볼루션) 예를 들어 커널이 다음과 같다면:
#[ a b c
#  d e f
#  g h i ]
# 특정 픽셀 중심으로 주변 3×3 영역과 곱하고 더하여 새 값 → 결과 이미지를 구성. / OpenCV의 filter2D()는 내부적으로 커널이 플립된(convolution) 형태로 적용됩니다(수학적 컨볼루션 공식에 따름).

# 4. 커널의 주요 속성
# 1) 크기 (Size):1×1 → 아무 변화 없음 / 3×3 → 빠르고 기본적 / 5×5 이상 → 더 부드러운 블러링 또는 강한 에지 검출 / 크기는 항상 홀수여야 중심(anchor)을 정확히 지정할 수 있음.
# 2) 값의 합(sum) 커널의 합은 출력 강도에 영향을 줍니다. / 합이 1 → 밝기 유지 예) 평균 블러 / 합이 0 → 에지 강조 예) 소벨(Sobel), 라플라시안(Laplacian) / 합이 >1 또는 <1 → 밝기 변화 가능 이를 보정하려면 delta 또는 커널 스케일링을 사용.
# 3) 중심점(anchor) / 기본값: (-1, -1) → 커널의 중앙 / 특정 방향으로만 필터링하고 싶다면 수동으로 설정 가능.

# 5. 대표적인 커널 예시
# 1) 평균 블러(Blur)
# kernel = np.ones((3,3), np.float32) / 9
# st = cv2.filter2D(img, -1, kernel)

# 2) 가우시안 블러(Gaussian)
# (직접 커널 생성도 가능하지만 보통 cv2.GaussianBlur() 사용) / 예:
# kernel = cv2.getGaussianKernel(5, 1) @ cv2.getGaussianKernel(5, 1).T

# 3) 샤프닝(Sharpening)
# kernel = np.array([[0, -1,  0],
#                    [-1, 5, -1],
#                    [0, -1,  0]])

# 4) 엠보싱(Emboss)
# kernel = np.array([[-2, -1, 0],
#                    [-1,  1, 1],
#                    [ 0,  1, 2]])

# 5) 에지 검출 (Edge Detection)
# 라플라시안:

# kernel = np.array([[0, 1, 0],
#                    [1,-4, 1],
#                    [0, 1, 0]])

# 6. ddepth의 의미 (출력 이미지 데이터 타입) / ddepth = -1 → 입력(src)와 동일한 깊이 / cv2.CV_32F 또는 CV_64F → 에지 검출 커널처럼 음수 결과를 다뤄야 할 때 유용 / 출력을 다시 디스플레이하려면 cv2.convertScaleAbs()로 변환해야 하는 경우도 많음.

# 7. 커널 설계 팁 / Tip 1) 에지 필터를 직접 만들기 / 예: x 방향만 강조하고 싶으면 / [-1, 0, 1] / Tip 2) 값의 합을 1로 정규화하면 밝기 변화를 최소화 / 블러 필터에서 흔히 사용. / Tip 3) 강도를 조절하고 싶다면 커널 전체를 스케일링 / kernel = kernel * alpha / 알파를 1.5, 2.0 등으로 조절 가능.

# 8. filter2D를 통한 커널 실험 예시 코드
# import cv2
# import numpy as np

# img = cv2.imread('image.jpg')

# 샤프닝 커널
# kernel = np.array([[0, -1,  0],
#                    [-1, 5, -1],
#                    [0, -1,  0]])

# sharpened = cv2.filter2D(img, -1, kernel)

# cv2.imshow('Original', img)
# cv2.imshow('Sharpened', sharpened)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# 요약
# 요소	        설명
# 커널	        필터링 규칙을 가진 작은 행렬
# 크기	        보통 홀수, 이미지의 어떤 범위를 참고하는지 결정
# 합	        밝기와 결과 강도에 영향
# 중심(anchor)  기본은 중앙, 방향성 필터에서 조정 가능
# ddepth        출력 데이터 타입 지정