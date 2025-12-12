"""
#색상 따라 원점 이동하는지 테스트
import cv2 
import numpy as np 

cap = cv2.VideoCapture(0)

while cap.isOpened() :
    ret, frame = cap.read()
    if not ret : break
    height, width, channels = frame.shape

    lower_bound = np.array([0, 80, 80])
    upper_bound = np.array([10, 255, 255]) 

    mask = cv2.inRange(cv2.cvtColor(frame, cv2.COLOR_BGR2HSV), lower_bound, upper_bound)
    
    cv2.imshow("mask", mask)

    M = cv2.moments(mask)

    if M["m00"] != 0 :
        cX = int(M["m10"] / M["m00"])
        cY = int(M["m01"] / M["m00"])
    else :
        cX = 0
        cY = 0
    
    offset = width // 2 - cX
    print(offset)

    cv2.circle(frame, (cX, cY), 10, (0, 255, 0), -1)
    cv2.imshow("AI CAR Streaming", frame)

    key = cv2.waitKey(50)
    if key == 27 : break

cv2.destroyAllWindows()
"""
import cv2 
import roslibpy
import numpy as np 
import base64


HOST = '192.168.0.8' 
PORT = 9090

client = roslibpy.Ros(host=HOST, port=PORT)
print(f"ROS Bridge 서버에 연결 시도 중: ws://{HOST}:{PORT}")

client.run()
print("연결여부:", client.is_connected)

laser = None

def callback1(msg):
    global laser
    angle_min   = msg['angle_min']
    angle_max  = msg['angle_max']
    angle_increment   = msg['angle_increment']
    range_min   = msg['range_min']
    range_max = msg['range_max']
    ranges = np.array(msg['ranges'], dtype=float)
    intensities   = msg['intensities']
        
    laser = (angle_min, angle_max, angle_increment, range_min, range_max, ranges, intensities)

def callback2(msg):
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

listener1 = roslibpy.Topic(client, "/scan", "sensor_msgs/LaserScan")
listener1.subscribe(callback1)

listener2 = roslibpy.Topic(client, '/img/compressed', 'sensor_msgs/msg/CompressedImage')
listener2.subscribe(callback2)

talker = roslibpy.Topic(client, '/cmd_vel', 'geometry_msgs/msg/Twist')
frame = None
while True:
    if laser is None or frame is None:
        print("아직 센서 또는 영상 데이터가 없습니다.")
    else:
        try:
            angle_min, angle_max, angle_increment, range_min, range_max, ranges, intensities = laser
            height, width, channels = frame.shape

            lower_bound = np.array([124, 37, 15])
            upper_bound = np.array([194, 107, 75])
            mask = cv2.inRange(cv2.cvtColor(frame, cv2.COLOR_BGR2HSV), lower_bound, upper_bound)
            cv2.imshow("mask", mask)

            M = cv2.moments(mask)

            if M["m00"] != 0 :
                cX = int(M["m10"] / M["m00"])
                cY = int(M["m01"] / M["m00"])
            else :
                cX = 0
                cY = 0

            offset = width // 2 - cX
            print(offset)

            num_points = len(ranges)

            angles_ros = angle_min + np.arange(num_points) * angle_increment

            # 전방 ±10도 계산   
            front_angle = 0.0
            front_range = 30 * np.pi / 180
            front_mask = (angles_ros >= front_angle - front_range) & (angles_ros <= front_angle + front_range)
            front_dist = np.mean(ranges[front_mask])
            safe_dist = 0.5 

            if offset <= 120 and offset >= -120 :
                action = "go_forward"
            elif offset > 120:
                action = "turn_right"
            elif offset < -120:
                action = "turn_left"
            else:
                action = "go_back"

            if front_dist < safe_dist :
                action = "stop"

            if action == 'go_forward':
                
                talker = roslibpy.Topic(client, '/turtle1/cmd_vel', 'geometry_msgs/msg/Twist')
                message = roslibpy.Message({
                    'linear': {'x': 0.5, 'y': 0.0, 'z': 0.0},
                    'angular': {'x': 0.0, 'y': 0.0, 'z': 0.0}
                })
                talker.publish(message)
                
                print("action:", action)
            elif action == 'turn_left':
                
                talker = roslibpy.Topic(client, '/turtle1/cmd_vel', 'geometry_msgs/msg/Twist')
                message = roslibpy.Message({
                    'linear': {'x': 0.0, 'y': 0.0, 'z': 0.0},
                    'angular': {'x': 0.0, 'y': 0.0, 'z': 0.5}
                })
                talker.publish(message)
                
                print("action:", action)
            elif action == 'turn_right':
                
                talker = roslibpy.Topic(client, '/turtle1/cmd_vel', 'geometry_msgs/msg/Twist')
                message = roslibpy.Message({
                    'linear': {'x': 0.0, 'y': 0.0, 'z': 0.0},
                    'angular': {'x': 0.0, 'y': 0.0, 'z': -0.5}
                })
                talker.publish(message)
                
                print("action:", action)
            elif action == 'go_back':
                
                talker = roslibpy.Topic(client, '/turtle1/cmd_vel', 'geometry_msgs/msg/Twist')
                message = roslibpy.Message({
                    'linear': {'x': -0.5, 'y': 0.0, 'z': 0.0},
                    'angular': {'x': 0.0, 'y': 0.0, 'z': 0.0}
                })
                talker.publish(message)
                
                print("action:", action)
            elif action == 'stop':
                
                talker = roslibpy.Topic(client, '/turtle1/cmd_vel', 'geometry_msgs/msg/Twist')
                message = roslibpy.Message({
                    'linear': {'x': 0.0, 'y': 0.0, 'z': 0.0},
                    'angular': {'x': 0.0, 'y': 0.0, 'z': 0.0}
                })
                talker.publish(message)
                
                print("action:", action)

            cv2.circle(frame, (cX, cY), 10, (0, 255, 0), -1)

            cv2.imshow("Image", frame)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        except Exception as e:
            print("불러오기 실패:", e)
cv2.destroyAllWindows()