import cv2

# IMREAD_UNCHANGED 플래그를 사용하여 이미지를 로드합니다.
ft = cv2.imread('filter.png', cv2.IMREAD_UNCHANGED)

# 이미지의 형태(Shape)를 출력합니다.
# 형태는 보통 (높이, 너비, 채널 수) 순서로 나옵니다.
print(f"이미지 배열의 형태 (Shape): {ft.shape}")