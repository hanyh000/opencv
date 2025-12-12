import roslibpy
from ultralytics import YOLO
import matplotlib.pyplot as plt
import cv2
import numpy as np

HOST = '192.168.0.8' 
PORT = 9090

client = roslibpy.Ros(host=HOST, port=PORT)

print(f"ROS Bridge 서버에 연결 시도 중: ws://{HOST}:{PORT}")
client.run()

def callback(message):
    pass
pose_topic = roslibpy.Topic(client, '/laser_val/laserpub', 'laser_package_msgs/msg/Laser')
pose_topic.subscribe(callback)
