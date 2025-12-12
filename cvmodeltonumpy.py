
import cv2
import numpy as np
import os
import matplotlib.pyplot as plt

path='C:/Users/202-15/Desktop/py_opencv/fruit'
labels = os.listdir(path)
img_list=[]
label_list=[]
for i in os.listdir(path):
    for j in os.listdir(os.path.join(path, i)):
        img = cv2.imread(os.path.join(path, i, j))
        img = cv2.resize(img, (60, 60))
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        img = img.astype(np.float32) / 255.0
        img_list.append(img)
        label_list.append(i)
img_array = np.array(img_list, dtype=np.float32)
label_array = np.array(label_list, dtype='U50') 

data = {
    "images": img_array,
    "labels": label_array
}

np.savez('C:/Users/202-15/Desktop/py_opencv/fruits', **data)
"""
import numpy as np

data = np.load('C:/Users/202-15/Desktop/py_opencv/fruits.npz', allow_pickle=True)

images = data['images']
labels = data['labels']

print("로드 완료!")
print("images shape:", images.shape)
print("labels shape:", labels.shape)
"""