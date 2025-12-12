"""
# qr생성
import cv2
import qrcode

text = "https://chatgpt.com/"
qr = qrcode.QRCode(
    version=1, # 1~40 까지의 범위, 데이터 볼륨을 뜻함 
    box_size=10, # 블록(점)의 크기
    border=4 # 블록 당 여백 크기
)
qr.add_data(text)
qr.make()

img = qr.make_image(fill_color="black", back_color="white")
img.save("sample_qr.png")

img1 =cv2.imread("sample_qr.png")
cv2.imshow("img",img1)
cv2.waitKey(0)
cv2.destroyAllWindows()
"""

# 디코딩 파트 
from pyzbar import pyzbar
import cv2

# 일단 이미지 읽어들이기 
image = cv2.imread("sample_qr.png")
decoded = pyzbar.decode(image)

for result in decoded : 
    data = result.data.decode("utf-8")
    (x, y, w, h) = result.rect # 검출된 큐알코드의 좌표 및 크기 정보 
    cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)

    # 텍스트 표시
    cv2.putText(image, data, (x, y - 10),
                cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 1)

cv2.imshow("Decoded QR", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
