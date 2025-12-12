import os
import glob
import cv2
import numpy as np 
import matplotlib.pyplot as plt

folder_names = ["apples", "tomatoes"]
num_of_classes = len(folder_names)

X = [] # 데이터
Y = [] # 타겟

for i, folder in enumerate(folder_names) :
    image_dir = folder + '/' 
    files = glob.glob(image_dir + "*.jpeg")

    # print(len(files))

    for j, file in enumerate(files) :
        img = cv2.imread(file, cv2.IMREAD_GRAYSCALE)
        img = cv2.resize(img, (64, 64))
        img = 255 - img # 회색조 영상 리버스하기
        
        # 밑에는 해도 되고 안 해도 됨
        # scaled_img = img / 255.0 

        X.append(img)
        Y.append(i)

# 넘파이 배열로 변환
X = np.array(X)
Y = np.array(Y)

print(X.shape)
print(Y.shape)

plt.imshow(X[0], cmap="gray")
plt.show()