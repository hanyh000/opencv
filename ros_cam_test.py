import roslibpy
import cv2
import numpy as np
import base64

HOST = '192.168.0.8'
PORT = 9090

client = roslibpy.Ros(host=HOST, port=PORT)
client.run()

frame = None

def callback(msg):
    global frame
    
    # Base64 디코딩
    try:
        img_raw = base64.b64decode(msg['data'])
    except Exception as e:
        print("Base64 decode error:", e)
        return

    # numpy 배열 변환
    img_bytes = np.frombuffer(img_raw, dtype=np.uint8)

    height = msg['height']
    width = msg['width']
    
    # encoding 확인 (일반적으로 'rgb8', 'bgr8', 'mono8' 등)
    encoding = msg.get('encoding', 'bgr8')

    try:
        if encoding == 'bgr8':
            frame = img_bytes.reshape((height, width, 3))
        elif encoding == 'rgb8':
            frame = img_bytes.reshape((height, width, 3))[:, :, ::-1]  # RGB→BGR 변환
        elif encoding == 'mono8':
            frame = img_bytes.reshape((height, width))
        else:
            print("지원하지 않는 encoding:", encoding)
    except Exception as e:
        print("reshape 실패:", e)


listener = roslibpy.Topic(client, '/img', 'sensor_msgs/msg/Image')
listener.subscribe(callback)

while True:
    if frame is not None:
        cv2.imshow("Image", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

listener.unsubscribe()
client.terminate()
cv2.destroyAllWindows()
