"""
#numpy
import numpy as np 
import matplotlib.pyplot as plt 

# 각도 생성
angles_deg = np.linspace(0, 360, 360)

# 라디안 변환 : 넘파이는 각도를 라디안으로 이해하고 있다!
angles_rad =  np.deg2rad(angles_deg)

# 가짜 라이다 센싱 거리 채우기 
distance = np.full(360, 1.5)

# 극좌표계 구하는 공식 
x = distance * np.cos(angles_rad)
y = distance * np.sin(angles_rad)

# 그래프로 시각화 
plt.figure(figsize=(6, 6))
plt.scatter(0, 0, color="blue", label="turtlebot3")
plt.scatter(x, y, color="red", label="LiDar Points")
plt.legend()
plt.show()
"""
"""
#numpy_roi
import numpy as np 
import matplotlib.pyplot as plt 

# 각도 생성
angles_deg = np.linspace(0, 360, 360)

# 라디안 변환 : 넘파이는 각도를 라디안으로 이해하고 있다!
angles_rad =  np.deg2rad(angles_deg)

# 가짜 라이다 센싱 거리 채우기 
distance = np.full(360, 1.5)
distance[45:90] = 0.8

distance[210:240] = 3.5
# roi 설정: 기준은 거리와 각도
cond_dist = distance <= 3.5
cond_angle = (angles_deg >= 0) & (angles_deg <= 270)
cond_total = cond_dist & cond_angle

# 극좌표계 구하는 공식 
x = distance * np.cos(angles_rad)
y = distance * np.sin(angles_rad)

#데이터 필터링
filterd_x = x[cond_total]
filtered_y = y[cond_total]

# 그래프로 시각화 
plt.figure(figsize=(6, 6))
plt.scatter(0, 0, color="blue", label="turtlebot3")
plt.scatter(filterd_x, filtered_y, color="red", label="LiDar Points")
plt.legend()
plt.show()
"""
""""""
#ros_data_read_and_control
import roslibpy
import numpy as np 
import matplotlib.pyplot as plt 
import matplotlib.animation as animation

HOST = '192.168.0.8' 
PORT = 9090

client = roslibpy.Ros(host=HOST, port=PORT)
print(f"ROS Bridge 서버에 연결 시도 중: ws://{HOST}:{PORT}")

client.run()
print("연결여부:", client.is_connected)

laser = None

def callback(msg):
    global laser
    angle_min   = msg['angle_min']
    angle_max  = msg['angle_max']
    angle_increment   = msg['angle_increment']
    range_min   = msg['range_min']
    range_max = msg['range_max']
    ranges = np.array(msg['ranges'], dtype=float)
    intensities   = msg['intensities']
    laser = (angle_min, angle_max, angle_increment, range_min, range_max, ranges, intensities)

listener = roslibpy.Topic(client, "/scan", "sensor_msgs/LaserScan")
listener.subscribe(callback)

fig, ax = plt.subplots(figsize=(6,6))
ax.set_xlim(-4,4)
ax.set_ylim(-4,4)
ax.set_aspect('equal')
ax.scatter(0, 0, color='blue', label='turtlebot3')
line, = ax.plot([], [], 'ro', label='LiDAR Points')
ax.legend()

talker = roslibpy.Topic(client, '/cmd_vel', 'geometry_msgs/msg/Twist')

def update(frame):
    global laser, line
    if laser is None:
        return line,

    angle_min, angle_max, angle_increment, range_min, range_max, ranges, intensities = laser

    # NaN, Inf 처리
    ranges[np.isnan(ranges)] = 3.5
    ranges[np.isinf(ranges)] = 3.5

    num_points = len(ranges)
    angles_deg = np.linspace(0, 360, num_points, endpoint=False)
    angles_rad = np.deg2rad(angles_deg)
    distance = ranges

    # ROI 필터링
    cond_dist = distance <= 3.5
    cond_angle = (angles_deg >= 0) & (angles_deg <= 360)
    cond_total = cond_dist & cond_angle

    x = distance * np.cos(angles_rad)
    y = distance * np.sin(angles_rad)

    filterd_x = x[cond_total]
    filtered_y = y[cond_total]

    # 좌표 갱신
    line.set_data(filterd_x, filtered_y)

    # 전방 평균 거리 계산 (±10도)
    angles_ros = angle_min + np.arange(num_points) * angle_increment

    # 전방 ±10도 계산   
    front_angle = 0.0
    front_range = 30 * np.pi / 180
    front_mask = (angles_ros >= front_angle - front_range) & (angles_ros <= front_angle + front_range)
    front_dist = np.mean(ranges[front_mask])

    safe_dist = 0.5
    # 제어 로직
    if front_dist < safe_dist:
        action = 'stop'
        msg = roslibpy.Message({
            'linear': {'x': 0.0, 'y': 0.0, 'z': 0.0},
            'angular': {'x': 0.0, 'y': 0.0, 'z': 0.0}
        })
     
    else:
        action = 'go'
        msg = roslibpy.Message({
            'linear': {'x': 0.5, 'y': 0.0, 'z': 0.0},  # 예시: 앞으로 이동
            'angular': {'x': 0.0, 'y': 0.0, 'z': 0.0}
            
        })


    talker.publish(msg)
    print(f"action: {action}, front_dist: {front_dist:.2f}m")


    print(action)

    return line,

# 애니메이션 실행
ani = animation.FuncAnimation(fig, update, frames=None, interval=100, blit=True)
plt.show()

# 종료 시 정리
listener.unsubscribe()
client.terminate()